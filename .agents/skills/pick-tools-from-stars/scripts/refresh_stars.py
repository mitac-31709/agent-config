#!/usr/bin/env python3
"""Rebuild references/stars.csv and references/stars_by_list.md for a GitHub user.

Usage: python3 scripts/refresh_stars.py <login> [--out DIR]
Read-only. Needs the `gh` CLI logged in. Star-list names come from the GraphQL
`viewer.lists` API, so they're only filled in when gh is logged in as <login>;
otherwise every repo is marked "(unlisted)". Existing description_ja values are kept.
"""
import argparse, csv, datetime as dt, json, os, subprocess, sys

UN = "(unlisted)"
COLS = ["lists", "full_name", "url", "description", "description_ja", "language",
        "stars", "pushed_at", "archived", "license", "topics", "starred_at"]
TZ = dt.datetime.now().astimezone().tzinfo


def gh(*args):
    r = subprocess.run(["gh", *args], capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError(r.stderr.strip())
    return r.stdout


def paged_json(text):
    dec, i, out = json.JSONDecoder(), 0, []
    while i < len(text):
        while i < len(text) and text[i].isspace():
            i += 1
        if i >= len(text):
            break
        obj, i = dec.raw_decode(text, i)
        out += obj
    return out


def star_lists(login):
    try:
        me = json.loads(gh("api", "user"))["login"]
    except Exception:
        return {}
    if me.lower() != login.lower():
        return {}
    q = "query{viewer{lists(first:100){nodes{id name slug}}}}"
    nodes = json.loads(gh("api", "graphql", "-f", "query=" + q))["data"]["viewer"]["lists"]["nodes"]
    out = {}
    for l in nodes:
        repos, cur = [], None
        while True:
            q = ("query($id:ID!,$c:String){node(id:$id){... on UserList{items(first:100,after:$c)"
                 "{pageInfo{hasNextPage endCursor} nodes{... on Repository{nameWithOwner}}}}}}")
            args = ["api", "graphql", "-f", "query=" + q, "-F", "id=" + l["id"]]
            if cur:
                args += ["-F", "c=" + cur]
            d = json.loads(gh(*args))["data"]["node"]["items"]
            repos += [n["nameWithOwner"] for n in d["nodes"] if n]
            if not d["pageInfo"]["hasNextPage"]:
                break
            cur = d["pageInfo"]["endCursor"]
        out[l["name"]] = {"slug": l["slug"], "repos": repos}
    return out


def day(s):
    return dt.datetime.fromisoformat(s.replace("Z", "+00:00")).astimezone(TZ).strftime("%Y-%m-%d") if s else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("login")
    ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "references"))
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    csv_path = os.path.join(a.out, "stars.csv")
    old = {}
    if os.path.exists(csv_path):
        old = {r["full_name"].lower(): r.get("description_ja", "") for r in csv.DictReader(open(csv_path, encoding="utf-8"))}

    items = paged_json(gh("api", "--paginate", f"users/{a.login}/starred?per_page=100",
                          "-H", "Accept: application/vnd.github.star+json"))
    lists = star_lists(a.login)
    mem = {}
    for name, l in lists.items():
        for r in l["repos"]:
            mem.setdefault(r.lower(), []).append(name)

    now = dt.datetime.now(TZ)
    rows = []
    for it in items:
        r = it["repo"]
        k = r["full_name"].lower()
        pushed = r.get("pushed_at")
        rows.append(dict(
            lists=" | ".join(mem.get(k, [UN])), full_name=r["full_name"], url=r["html_url"],
            description=(r.get("description") or "").replace("\n", " ").strip(), description_ja=old.get(k, ""),
            language=r.get("language") or "", stars=r["stargazers_count"], pushed_at=day(pushed),
            archived=r["archived"], license=(r.get("license") or {}).get("spdx_id") or "",
            topics=" ".join(r.get("topics") or []), starred_at=day(it.get("starred_at")),
            inactive=(not pushed) or (now - dt.datetime.fromisoformat(pushed.replace("Z", "+00:00"))).days >= 730))

    order = sorted(lists, key=lambda n: -len(lists[n]["repos"])) + [UN]
    first = lambda x: order.index(x["lists"].split(" | ")[0])
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, COLS, extrasaction="ignore")
        w.writeheader()
        for x in sorted(rows, key=lambda x: (first(x), -x["stars"])):
            w.writerow(x)

    unl = sum(1 for x in rows if x["lists"] == UN)
    L = [f"# GitHub stars of {a.login}, grouped by star list\n",
         f"Snapshot: {now:%Y-%m-%d %H:%M} ({now:%Z}). Total {len(rows)} starred repos in {len(lists)} lists; {unl} not in any list yet.\n",
         "Sorted by stars within each list. 📦 = archived, 💤 = no push for 2+ years. "
         "Line format: `[owner/repo](url) ★stars · language · last push — description`.\n", "## Lists\n"]
    for n in order:
        c = sum(1 for x in rows if n in x["lists"].split(" | "))
        url = f" — https://github.com/stars/{a.login}/lists/{lists[n]['slug']}" if n in lists else ""
        L.append(f"- {n} ({c}){url}")
    L.append("")
    for n in order:
        xs = sorted([x for x in rows if n in x["lists"].split(" | ")], key=lambda x: -x["stars"])
        if not xs:
            continue
        L.append(f"## {n} ({len(xs)})\n")
        for x in xs:
            mark = (" 📦" if x["archived"] else "") + (" 💤" if x["inactive"] and not x["archived"] else "")
            d = " / ".join(s for s in (x["description_ja"], x["description"]) if s)
            L.append(f"- [{x['full_name']}]({x['url']}) ★{x['stars']} · {x['language'] or '-'} · {x['pushed_at']}{mark} — {d}")
        L.append("")
    open(os.path.join(a.out, "stars_by_list.md"), "w", encoding="utf-8").write("\n".join(L))
    print(f"{len(rows)} stars, {len(lists)} lists, {unl} unlisted -> {a.out}", file=sys.stderr)


if __name__ == "__main__":
    main()

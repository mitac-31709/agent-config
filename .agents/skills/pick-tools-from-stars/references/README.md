# references (optional)

This folder is where a local star snapshot can live. `stars.csv` and `stars_by_list.md` are personal and are not part of the public repository.

From this directory:

```bash
python3 ../scripts/refresh_stars.py <github-login>
```

The script only reads GitHub. Column layout, and when star-list names are filled in, are documented in `../SKILL.md`. Do not commit the snapshot files. The repository root `.gitignore` ignores `references/stars*` and `**/references/stars*`.

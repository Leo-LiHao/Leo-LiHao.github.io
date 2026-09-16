# CLAUDE.md

Hao Li's academic personal website — Jekyll (Academic Pages theme). GitHub Pages builds and deploys automatically on push to master; never build locally, just edit and push.

## Principles

- This is a stable personal site, not an app. Make minimal, surgical edits; no refactors or dependency changes unless asked.
- The source of truth for publications is the hand-maintained list in `_pages/about.md`. When editing it, match the formatting, numbering, and link style of neighboring entries exactly.
- The repo is a standard Jekyll site — discover structure by reading it rather than relying on documentation here.

## Non-obvious facts

- Publication links render as buttons only if the URL ends in `.pdf`/`.bib` or the link carries `{: .btn-pub}` (styled in `_sass/_custom-enhancements.scss`). arXiv PDF URLs don't end in `.pdf`, so they need the explicit class.
- Adding a paper: put the PDF and `.bib` in `files/`, add the entry to `_pages/about.md`, and add a stub in `_publications/`.
- CV is dual-format: edit `_pages/cv.md`, then run `./scripts/update_cv_json.sh` to regenerate `_data/cv.json`.
- `markdown_generator/` (TSV → markdown generators) is template leftover and unused — don't route content through it.

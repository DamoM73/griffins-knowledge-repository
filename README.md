# Griffins' Knowledge Repository

Build and programming tutorials for students competing in RoboCup Junior Australia challenges, plus lessons for the other robots used in class (ELECFREAKS PU Robot, XGO Robot Dog V2 and WuKong Manipulator).

Live site: <https://damom73.github.io/griffins-knowledge-repository/>

## Audience

Secondary students (Years 7–10). Pages are written at a Year 7/8 level.

## Preview locally

```
pip install -r requirements.txt
zensical serve
```

Then open <http://localhost:8000>.

## Checks

Run these before committing:

```
python scripts/make_starter_comments.py   # copy exercise wording into starter files
python scripts/build_glossary.py          # rebuild the Glossary from the Terminology callouts
python scripts/make_blocks_placeholders.py  # placeholder images for missing Blocks screenshots (needs Pillow)
python scripts/check_explanations.py      # expect: 0 issue(s) found
zensical build --clean                    # expect: No issues found
```

## Layout

```
zensical.toml                       site config and nav
docs/
  index.md                          home page
  onstage/ rescue-line/ rescue-maze/ soccer/ tips/   RoboCup Junior sections
  other-robots/                     Using MakeCode, PU Robot, XGO, WuKong lessons
  reference/glossary.md             built by scripts/build_glossary.py
  examples/other/<kit>/lesson_NN_<example>.py       MakeCode Python examples and exercise starters
  assets/blocks/<kit>/              Blocks screenshots (placeholders until replaced)
  stylesheets/extra.css             colour scheme and callout styles
scripts/                            check and build scripts
.github/workflows/docs.yml          deploys to GitHub Pages on push to main
```

## Licences

Content licensed under CC BY-NC-SA 4.0 (see [LICENSE-CONTENT.md](LICENSE-CONTENT.md)). Code licensed under GPLv3 (see [LICENSE](LICENSE)).

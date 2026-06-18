# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

Course content for **IST356: Programming Techniques for Data Analytics** (Syracuse iSchool, instructor Michael Fudge). It is teaching material, not an application — there is no single program to build or deploy. The audience is students who pull and run individual files. Edits are made by the instructor; students fork/pull only (`git reset --hard origin/main` to get updates, per `readme.md`).

## Setup

```bash
pip3 install -r requirements.txt
playwright install   # needed for 5-web scraping demos (pytest-playwright/playwright)
```

## Repository structure

Content is split into numbered topic modules, each a self-contained folder. The progression is the course progression:

- `0-intro/` — environment setup, GitHub, hello-world
- `1-python/` — Python fundamentals
- `2-ui/` — Streamlit widgets/interaction basics
- `3-data/` — pandas + Streamlit data apps
- `4-api/` — FastAPI (building APIs) and `requests` (consuming APIs)
- `5-web/` — web scraping (Playwright/requests) feeding Streamlit
- `6-viz/` — visualization (seaborn, plotly express, folium/geopandas maps)

Within each module the files follow a consistent convention:

- `N-*-slides.ipynb` — lecture slide decks (Jupyter notebooks, the primary teaching artifact)
- `N-*.py` — runnable demo scripts shown in lecture
- `data/` — sample datasets used by that module's demos
- `solutions/` — completed lab/exercise solutions, named `N-L-E.py` (module-lesson-exercise, e.g. `3-1-2.py`)

`dev/` holds in-progress modules not yet in the course sequence. `syllabus.md` and `TODO.md` track course logistics, not code.

## Running the demos

There is no test/build pipeline for most code — files are meant to be run individually. VS Code launch configs (`.vscode/launch.json`) are the canonical way to run them:

- **Streamlit apps** (`2-ui`, `3-data`, `5-web`, `6-viz`, and `streamlit-*.py` / `st-*.py` files): `streamlit run <file>` — or the "Streamlit Run: Current File" debug config.
- **FastAPI apps** (`4-api/fast*.py`): `fastapi dev <file> --reload` — or the "FastAPI Run: Current File" debug config.
- **Plain scripts / notebooks**: run directly with Python or the Jupyter kernel.

## Tests

Testing is itself a teaching topic, so test functions live *inside* the source files they exercise (pytest functions colocated with the code, e.g. `1-python/solutions/dateutils.py`), not in a separate test tree. The top-level `tests/` folder is mostly a stub.

```bash
pytest 1-python/solutions/dateutils.py        # run a single file's inline tests
```

`.vscode/settings.json` points the VS Code test runner at `1-python/solutions/dateutils.py`. Some solution files (e.g. `3-data/solutions/check_functions.py`) instead assert in a `if __name__ == '__main__':` block — run those directly with `python3 <file>`.

## Conventions for new content

- Match the module's existing file-naming scheme (`N-L-slides.ipynb`, demo `N-*.py`, solutions `N-L-E.py`).
- Demo scripts favor heavy explanatory inline comments — the code is read in lecture, so clarity over brevity.
- Put any new sample data in the module's own `data/` folder.

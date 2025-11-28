# Copilot Instructions

## Purpose
This repo contains a simple web app that allows a user to upload an Excel file (.xls/.xlsx), other then this you have multiplease features which are defined in sepcs/projectSpecs.md file 

## Read-first
Before generating any code, read files under /specs/ and treat them as canonical requirements.

## Project preferences & rules
- Tech stack: back end : Python, pandas, openpyxl , front-end : streamlit 
- Use simple, readable code and include docstrings for public functions.
- Add a minimal test under /tests/ using pytest.
- Add requirements.txt with explicit packages.
- Add a README.md with run instructions.
- Create a small GitHub Actions workflow under .github/workflows/ci.yml that runs pytest and flake8 (or black check).
- When generating code:
  - Create ASSUMPTIONS.md inside any newly created module to document assumptions made.
  - Do not include secrets or credentials in code. For config, generate `.env.example`.
  - Prefer defensive error handling (try/except) and user-friendly error messages in UI.

## Tests & Quality
- Provide at least one unit test that verifies reading a small sample Excel-like dataframe (you may mock file input).
- Keep tests fast and deterministic.
sim
## Output format
- When asked to scaffold the app, create the following files: `app.py`, `requirements.txt`, `README.md`, `tests/test_app.py`, `.github/workflows/ci.yml`, and `ASSUMPTIONS.md`.
- For any ambiguous requirement, ask one clarifying question. If cloning is not possible, assume default behaviors documented in ASSUMPTIONS.md.
- add a architecture.md file and write what all changes we have done and also create a full flow chart of the application in it.

## Guidelines
- Use Copilot to assist with code generation, refactoring, and documentation.
- Follow project-specific conventions and best practices.
- Review Copilot suggestions before committing code.

## Spec-Driven Development
- Refer to the `specs/` folder for initial specifications and requirements.
- Update specs as the project evolves.

## Collaboration
- Communicate changes and suggestions clearly in pull requests.
- Use Copilot to enhance productivity, not replace code reviews.

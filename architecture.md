# Architecture Overview: Spec Driven App 1

## Summary of Changes
- Scaffolded a FastAPI backend (`app.py`) for file upload, data processing, and CSV download.
- Created a static frontend (`static/index.html`, `static/style.css`, `static/script.js`) for user interaction.
- Added `requirements.txt` for dependencies: fastapi, uvicorn, pandas, openpyxl, pytest.
- Created basic unit test (`tests/test_app.py`) for Excel reading.
- Added CI workflow (`.github/workflows/ci.yml`) for linting and testing.
- Documented assumptions in `ASSUMPTIONS.md`.
- Provided `.env.example` for configuration.

## Application Flow Chart

```mermaid
flowchart TD
    A[User accesses web app] --> B[Frontend: index.html]
    B --> C[User uploads Excel file]
    C --> D[POST /upload (FastAPI)]
    D --> E[Backend: app.py reads file with pandas/openpyxl]
    E --> F{Validation}
    F -->|Valid| G[Return preview data (max 1000 rows)]
    F -->|Invalid| H[Return error message]
    G --> I[Frontend displays table]
    I --> J[User clicks Download CSV]
    J --> K[GET /download (FastAPI)]
    K --> L[Backend returns CSV]
    L --> M[User downloads CSV]
```

## Notes
- All static files are served from `/static/`.
- Backend handles validation, error messages, and data processing.
- CI ensures code quality and test coverage.
- Assumptions and config are documented for clarity.

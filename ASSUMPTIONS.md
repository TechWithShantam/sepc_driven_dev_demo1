# Assumptions for Spec Driven App 1

- Only .xls and .xlsx files are accepted for upload.
- The first sheet is read by default; user can select another if needed (future feature).
- Data preview is limited to 1000 rows for performance.
- No authentication or S3 upload required for demo.
- Friendly error messages are shown for invalid files or empty data.
- Frontend is static HTML/JS/CSS served by FastAPI.
- No secrets or credentials are included in code.

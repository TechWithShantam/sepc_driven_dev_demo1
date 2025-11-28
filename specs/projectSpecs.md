## todo steps
Build a minimal web app application where:
1. A user uploads an Excel file (.xlsx or .xls).
2. The app reads the first sheet by default (allow user to select a sheet if workbook has multiple).
3. The sheet's data is displayed in a scrollable table.
4. The user can download show data as CSV.
5. If reading fails, show a friendly error.

## Validation rules
- Only accept files with extensions csv xls or xlsx.
- If file is empty, show "No data found".
- Max preview rows: 1000 (if larger, show first 1000 and show a warning).
- Accept small files for the demo (no S3 upload required).

## Non-functional
- Include `requirements.txt` with  `pandas`, `openpyxl`, `pytest`.
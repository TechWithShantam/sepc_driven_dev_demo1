from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse, StreamingResponse
import pandas as pd
import io

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def index():
    with open("static/index.html") as f:
        return f.read()


@app.post("/upload")
def upload_excel(file: UploadFile = File(...)):
    if not file.filename.endswith((".xls", ".xlsx")):
        raise HTTPException(status_code=400, detail="Invalid file type.")
    try:
        df = pd.read_excel(file.file, sheet_name=0)
        if df.empty:
            return {"error": "No data found"}
        preview = df.head(1000)
        warning = "Preview limited to 1000 rows" if len(df) > 1000 else ""
        return {
            "columns": preview.columns.tolist(),
            "rows": preview.values.tolist(),
            "warning": warning
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/download")
def download_csv():
    # For demo, return a sample CSV
    df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    stream = io.StringIO()
    df.to_csv(stream, index=False)
    response = StreamingResponse(
        iter([stream.getvalue()]),
        media_type="text/csv"
    )
    response.headers["Content-Disposition"] = "attachment; filename=sample.csv"
    return response
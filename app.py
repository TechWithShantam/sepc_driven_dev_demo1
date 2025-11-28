
import streamlit as st
import pandas as pd
import openpyxl

st.set_page_config(page_title="Spec-driven app 1", layout="wide")
st.title("Spec-driven app 1")
st.caption("helping engineers code faster and Declarative to Deployment")

uploaded_file = st.file_uploader("Upload an Excel file (.xls, .xlsx)", type=["xls", "xlsx"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file, sheet_name=0)
        if df.empty:
            st.warning("No data found in the uploaded file.")
        else:
            preview = df.head(1000)
            st.write("Preview (max 1000 rows):")
            st.dataframe(preview)
            if len(df) > 1000:
                st.warning("Preview limited to 1000 rows.")
            csv = preview.to_csv(index=False).encode('utf-8')
            st.download_button("Download as CSV", csv, "preview.csv", "text/csv")
    except Exception as e:
        st.error(f"Error reading file: {e}")
else:
    st.info("Please upload an Excel file to begin.")
# src/loader.py
from pathlib import Path
import pandas as pd
from tkinter import Tk, filedialog

def select_excel_file() -> Path:
    Tk().withdraw()
    file_path = Path(filedialog.askopenfilename(
        title="Select Excel file",
        filetypes=[("Excel files", "*.xlsx *.xls")]
    ))
    if not file_path or not file_path.exists():
        raise FileNotFoundError("No valid file selected.")
    return file_path

def load_excel_data(path: Path) -> pd.DataFrame:
    ext = path.suffix.lower()
    if ext == ".xls":
        df = pd.read_excel(path, engine="xlrd")
    elif ext == ".xlsx":
        df = pd.read_excel(path, engine="openpyxl")
    else:
        raise ValueError("Unsupported file format. Use .xls or .xlsx.")
    return df

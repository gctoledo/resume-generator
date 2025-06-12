from pathlib import Path
import pandas as pd
from openpyxl import load_workbook
from .styles import apply_excel_styles

def save_dataframe_to_excel(df: pd.DataFrame, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_excel(output_path, index=False)
    wb = load_workbook(output_path)
    ws = wb.active
    apply_excel_styles(ws, df.columns.tolist())
    wb.save(output_path)

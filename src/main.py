# src/main.py
from datetime import datetime
from pathlib import Path
import os

from .loader import select_excel_file, load_excel_data
from .transformer import transform_sales_data
from .exporter import save_dataframe_to_excel

def main():
    input_path = select_excel_file()
    df = load_excel_data(input_path)
    final_table, ordered_months = transform_sales_data(df)

    base_name = input_path.stem
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    output_path = Path("reports") / f"Report-{base_name}-{timestamp}.xlsx"

    save_dataframe_to_excel(final_table, output_path)
    print(f"Report generated at: {output_path}")
    os.startfile(output_path)

if __name__ == "__main__":
    main()

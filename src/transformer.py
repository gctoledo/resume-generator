import pandas as pd

MONTHS_PT = {
    1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
    5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
    9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
}

def transform_sales_data(df: pd.DataFrame) -> tuple[pd.DataFrame, list]:
    df = df.dropna(subset=["Data"])
    df["Data"] = pd.to_datetime(df["Data"], dayfirst=True)
    df["Valor da Venda"] = (
        df["Valor da Venda"]
        .replace("[R$ ]", "", regex=True)
        .str.replace(".", "", regex=False)
        .str.replace(",", ".", regex=False)
        .astype(float)
    )
    df["MesAno"] = df["Data"].dt.to_period("M").dt.to_timestamp()
    df["NomeMes"] = df["Data"].dt.month.map(MONTHS_PT)

    official_names = df.groupby("Cód Cliente")["Cliente"].first()
    grouped = (
        df.groupby(["Cód Cliente", "NomeMes"])["Valor da Venda"]
        .sum()
        .reset_index()
    )
    grouped["Cliente"] = grouped["Cód Cliente"].map(official_names)
    grouped = grouped[["Cód Cliente", "Cliente", "NomeMes", "Valor da Venda"]]

    ordered_months = (
        df[["NomeMes", "MesAno"]]
        .drop_duplicates()
        .sort_values("MesAno")["NomeMes"]
        .tolist()
    )

    final_table = grouped.pivot_table(
        index=["Cód Cliente", "Cliente"],
        columns="NomeMes",
        values="Valor da Venda",
        aggfunc="sum"
    ).reset_index()

    columns_order = ["Cód Cliente", "Cliente"] + [m for m in ordered_months if m in final_table.columns]
    final_table = final_table[columns_order]

    return final_table, ordered_months

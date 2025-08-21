from datetime import date
import pandas as pd

def clean_headers(df: pd.DataFrame) -> pd.DataFrame:
    first_row = df.iloc[0].fillna("").astype(str)
    second_row = df.iloc[1].fillna("").astype(str)

    if (second_row.str.contains(r"[A-Za-z]").any()):
        headers = (first_row + " " + second_row).str.strip()
        df.columns = headers
        df = df.drop([0, 1]).reset_index(drop=True)
    else:
        headers = first_row.str.strip()
        df.columns = headers
        df = df.drop([0]).reset_index(drop=True)

    return df


def clean_data(df: pd.DataFrame):
    report_date = date.today()  
    structured_data = []

    if df is None or df.empty:
        return structured_data

    df = clean_headers(df)

    # Rename columns for clean keys
    df.rename(columns={
        "State's Control Area Generation (Net MU) Thermal": "Thermal",
        "State's Control Area Generation (Net MU) Hydro": "Hydro",
        "State's Control Area Generation (Net MU) Gas + Naptha + Diesel": "Gas_Naptha_Diesel",
        "State's Control Area Generation (Net MU) Solar": "Solar",
        "State's Control Area Generation (Net MU) Wind": "Wind",
        "State's Control Area Generation (Net MU) Others (Biomass, Cogen, etc.)": "Others_Biomass_Cogen",
        "State's Control Area Generation (Net MU) Total": "Total",
        "Drawal Schedule (MU)": "Drawal_Sch",
        "Actual Drawal (MU)": "Act_Drawal",
        "UI (MU)": "UI",
        "Requirement (MU)": "Requirement",
        "Shortage (-)/ Surplus(+) (MU)": "Shortage",
        "Consumption (MU)": "Consumption"
    }, inplace=True, errors="ignore")

    for i in range(len(df)):
        state = str(df.iloc[i, 0]).strip()

        if state.upper() in ("REGION", "TOTAL", ""):
            continue

        row_data = {"report_date": str(report_date), "State": state}

        # Add remaining columns
        for col in df.columns[1:]:
            raw_value = df.iloc[i][col]
            value = None if pd.isna(raw_value) else str(raw_value).strip()
            row_data[col] = value

        structured_data.append(row_data)

    return structured_data

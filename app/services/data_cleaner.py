from datetime import date
import pandas as pd

def clean_headers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans headers for the table.
    Detects if header is 1-row or 2-rows and assigns proper column names.
    """

    # Check if first two rows look like headers (strings, not numeric)
    first_row = df.iloc[0].fillna("").astype(str)
    second_row = df.iloc[1].fillna("").astype(str)

    if (second_row.str.contains(r"[A-Za-z]").any()):  
        # Probably 2-row header → join them
        headers = (first_row + " " + second_row).str.strip()
        df.columns = headers
        df = df.drop([0, 1]).reset_index(drop=True)
    else:
        # Use only first row
        headers = first_row.str.strip()
        headers = [h if h != "" else f"col_{i}" for i, h in enumerate(headers)]
        df.columns = headers
        df = df.drop([0]).reset_index(drop=True)

    return df


def clean_data(df: pd.DataFrame):
    report_date = date.today()  
    structured_data = []

    if df is None or df.empty:
        return structured_data

    df = clean_headers(df)

    for i in range(len(df)):
        state = str(df.iloc[i, 0]).strip()

        if state.upper() in ("REGION", "TOTAL", ""):
            continue

        for col in df.columns[1:]:
            key = str(col).strip() if col else None
            if not key or key.lower() in ["nan", "none"]:
                continue

            raw_value = df.iloc[i][col]
            if isinstance(raw_value, (pd.Series, pd.DataFrame)):
                raw_value = raw_value.values[0] if not raw_value.empty else None

            value = "" if pd.isna(raw_value) else str(raw_value).strip()

            structured_data.append({
                "report_date": report_date,  
                "state": state,
                "key": key,
                "value": value
            })

    return structured_data
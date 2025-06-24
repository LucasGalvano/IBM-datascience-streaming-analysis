import pandas as pd
import os
from pathlib import Path

def clean_data():
    project_root = Path(__file__).parent.parent
    data_dir = project_root / "data"
    
    data_dir.mkdir(exist_ok=True)

    for company in ["netflix", "amazon"]:
        raw_path = data_dir / f"{company}_raw.csv"
        
        df = pd.read_csv(raw_path, skipfooter=7, engine="python")
        
        df.columns = df.columns.str.strip()
        df["Volume"] = pd.to_numeric(df["Volume"].astype(str).str.replace(",", ""), errors="coerce")
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df.sort_values("Date", inplace=True)

        clean_path = data_dir / f"{company}_clean.csv"
        df.to_csv(clean_path, index=False)
        print(f"{company.title()} salvo em: {clean_path}")

clean_data()
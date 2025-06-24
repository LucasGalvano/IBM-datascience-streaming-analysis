import pandas as pd
import matplotlib.pyplot as plt
import os
from pathlib import Path

def compare_data():
    project_root = Path(__file__).parent.parent
    data_dir = project_root / "data"
    plots_dir = project_root / "plots"
    plots_dir.mkdir(exist_ok=True)

    netflix = pd.read_csv(data_dir / "netflix_clean.csv", parse_dates=["Date"])
    amazon = pd.read_csv(data_dir / "amazon_clean.csv", parse_dates=["Date"])


    netflix["Company"] = "Netflix"
    amazon["Company"] = "Amazon"

    combined = pd.concat([netflix, amazon], ignore_index=True)

    for company_df in [netflix, amazon]:
        company_df.sort_values("Date", inplace=True)
        company_df["Pct_Change"] = company_df["Close"].pct_change() * 100
        company_df["Return"] = (1 + company_df["Pct_Change"] / 100).cumprod()
        company_df.fillna(0, inplace=True)


    plt.figure(figsize=(12, 6))
    plt.plot(netflix["Date"], netflix["Return"], label="Netflix", linewidth=2, color='#E50914')
    plt.plot(amazon["Date"], amazon["Return"], label="Amazon", linewidth=2, color='#FF9900')
    plt.title("Accumulated Return: Netflix vs Amazon (2016-2021)", fontsize=14)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Investment Multiplier", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig(plots_dir / "accumulated_return.png", dpi=300)
    plt.close()


    plt.figure(figsize=(12, 6))
    plt.plot(netflix["Date"], netflix["High"] - netflix["Low"], label="Netflix", linewidth=1.5, color='#E50914', alpha=0.8)
    plt.plot(amazon["Date"], amazon["High"] - amazon["Low"], label="Amazon", linewidth=1.5, color='#FF9900', alpha=0.8)
    plt.title("Daily Volatily: Netflix vs Amazon (2016-2021)", fontsize=14)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Price Difference (High - Low)", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig(plots_dir / "volatility.png", dpi=300)
    plt.close()

    correlation = netflix["Pct_Change"].corr(amazon["Pct_Change"])
    print(f"Correlação entre os retornos: {correlation:.2f}")

compare_data()
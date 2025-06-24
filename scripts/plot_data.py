import pandas as pd
import matplotlib.pyplot as plt
import os
from pathlib import Path

def plot_data():
    project_root = Path(__file__).parent.parent
    data_dir = project_root / "data"
    plots_dir = project_root / "plots"
    
    plots_dir.mkdir(exist_ok=True)

    for company in ["netflix", "amazon"]:
        csv_path = data_dir / f"{company}_clean.csv"
        df = pd.read_csv(csv_path)
        
        df["Date"] = pd.to_datetime(df["Date"])

        plt.figure(figsize=(12, 6))
        plt.plot(df["Date"], df["Close"], label="Price", color="blue")
        plt.title(f"Closing Price - {company.title()}", fontsize=14)
        plt.xlabel("Date", fontsize=12)
        plt.ylabel("Price (USD)", fontsize=12)
        plt.grid(True, linestyle="--", alpha=0.7)
        plt.tight_layout()
        
        close_plot_path = plots_dir / f"{company}_close.png"
        plt.savefig(close_plot_path, dpi=300)
        plt.close()
        print(f"Price graph saved in: {close_plot_path}")

        plt.figure(figsize=(10, 5))
        plt.bar(df["Date"], df["Volume"], color="green", width=10, alpha=0.6, label="Volume")
        plt.title(f"Trading Volume - {company.title()}", fontsize=14)
        plt.xlabel("Date", fontsize=12)
        plt.ylabel("Volume", fontsize=12)
        plt.grid(True, linestyle="--", alpha=0.7)
        plt.tight_layout()
        
        volume_plot_path = plots_dir / f"{company}_volume.png"
        plt.savefig(volume_plot_path, dpi=300)
        plt.close()
        print(f"Saved volume graph in: {volume_plot_path}")

plot_data()
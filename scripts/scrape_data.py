import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
import warnings

def scrape_data():
    warnings.filterwarnings("ignore", category=FutureWarning)

    data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    data_dir = os.path.abspath(data_dir)
    
    os.makedirs(data_dir, exist_ok=True)

    print(f"Saving data in: {data_dir}")  # Debug

    netflix_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"
    amazon_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html"

    netflix_response = requests.get(netflix_url)
    amazon_response = requests.get(amazon_url)

    netflix_soup = BeautifulSoup(netflix_response.text, 'html.parser')
    amazon_soup = BeautifulSoup(amazon_response.text, 'html.parser')

    netflix_table = pd.read_html(str(netflix_soup))[0]
    amazon_table = pd.read_html(str(amazon_soup))[0]

    netflix_path = os.path.join(data_dir, "netflix_raw.csv")
    amazon_path = os.path.join(data_dir, "amazon_raw.csv")

    netflix_table.to_csv(netflix_path, index=False)
    amazon_table.to_csv(amazon_path, index=False)

    if os.path.exists(netflix_path) and os.path.exists(amazon_path):
        print("Data saved successefully!")
    else:
        print("Error: The files were not created.")

scrape_data()
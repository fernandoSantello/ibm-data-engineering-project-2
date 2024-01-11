import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract(url: str) -> pd.DataFrame:
    page = BeautifulSoup(requests.get(url=url).text, 'lxml')
    table = page.find('table', attrs={'class': 'wikitable'})
    df = pd.read_html(str(table))[0]
    return df

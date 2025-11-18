import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

titles = [item.get_text() for item in soup.select(".titleline > a")]

df = pd.DataFrame({"title": titles})
df.to_csv("titles.csv", index=False)

print("Hotovo! Data uložené v titles.csv")


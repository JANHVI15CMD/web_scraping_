import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Web_scraping"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.text)  # Wikipedia Page ka Title print karega

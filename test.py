import requests
# import re
from bs4 import BeautifulSoup


url = 'https://hh.ru/search/vacancy?L_is_autosearch=false&clusters=true&enable_snippets=true&text=python&area=1'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    vacancies = soup.find_all('div', class_='vacancy-serp-item')
print(response)

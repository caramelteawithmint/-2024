import requests
import re
from bs4 import BeautifulSoup

response = requests.get('https://api.hh.ru/vacancies')

vacancies_list = []
vacancies = response.json()['items']
for vacancy in vacancies:
    title = vacancy['name']
    vacancies_list.append(title)


vacancies_id_list = []
for vacancy_id in vacancies:
    title = vacancy['id']
    vacancies_id_list.append(title)
    

vacancies_id_list = []
for vacancy_id in vacancies:
    title = vacancy['id']
    vacancies_id_list.append(title)







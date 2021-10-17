from bs4 import BeautifulSoup as soup  # HTML data structure
import requests


page_url = 'https://www.instagram.com/kimkardashian/?hl=en'
source = requests.get(page_url).text

soup_html = soup(source,'html.parser')

print(soup_html.prettify())


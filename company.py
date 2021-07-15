import requests
from bs4 import BeautifulSoup

url=''

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

company_class = ''
company = soup.find('', class_=company_class)
print(soup,company)
from bs4 import BeautifulSoup
import requests

r = requests.get('https://mohsinweb.herokuapp.com/quotes/')

soup = BeautifulSoup(r.text, 'html.parser')

print(soup.prettify())

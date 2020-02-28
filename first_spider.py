from bs4 import BeautifulSoup
import requests
import json

r = requests.get('https://mohsinweb.herokuapp.com/quotes/')

soup = BeautifulSoup(r.text, 'lxml')

# print(soup.prettify())

title = soup.h1.text

quotesHTML = soup.findAll('div', {"class": "quotes"})

quotes = [
    {"quote": quote.findAll('p')[0].text.strip(),
     "author": quote.findAll('p')[1].text.strip()}
    for quote in quotesHTML]

# Ouverture du fichier en écriture
f = open("quote.json", "w")

# Insertion au format json de la liste 'quotes'
json.dump(quotes, f)

print(quotes)

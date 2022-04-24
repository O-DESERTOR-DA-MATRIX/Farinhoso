# Date and time structure
import requests
from bs4 import BeautifulSoup
from datetime import datetime

data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y | %H:%M')

# Request structure

headers = {'Mozilla/5.0'}

url_base = 'https://lista.mercadolivre.com.br/'

# product_name = input('Digite um produto para pesquisa de item')
product_name = 'galaxy note 20'

response = requests.get(url_base + product_name)

website = BeautifulSoup(response.text, 'html.parser')

# Web Scrapping Initializing
products = website.findAll('div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result'
                                                  ' ui-search-result--core andes-card--padding-default'})


# Condition for character formatting
for product in products:
    title = product.find('h2', attrs={'class': 'ui-search-item__title'})

    price = product.find(
        'div', attrs={'class': 'ui-search-price__second-line'})

    price_format = price.text
    p2 = price_format

    if len(price_format) == 12:
        p1 = price_format[0:3]
        p2 = price_format[0:3]

    if len(price_format) == 14:
        p1 = price_format[0:3]
        p2 = price_format[0:3]

    if len(price_format) == 17:
        p1 = price_format[12:17]
        p2 = price_format[12:17]

    if len(price_format) == 19:
        p1 = price_format[12:23]
        p2 = price_format[12:23]

    if len(price_format) == 21:
        p1 = price_format[11:14]
        p2 = price_format[11:14]

    if len(price_format) == 23:
        p1 = price_format[12:17]
        p2 = price_format[12:17]

    if len(price_format) == 24:
        p1 = price_format[12:17]
        p2 = price_format[12:17]

    if len(price_format) == 30 or len(price_format) == 32:
        p1 = price_format[24:32]
        p2 = price_format[24:32]

    if len(price_format) == 32:
        p1 = price_format[27:32]
        p2 = price_format[27:32]

    if len(price_format) == 34:
        p1 = price_format[28:34]
        p2 = price_format[28:34]

    if len(price_format) == 37:
        p1 = price_format[26:30]
        p2 = price_format[26:30]

    if len(price_format) == 38:
        p1 = price_format[27:32]
        p2 = price_format[27:32]

    if len(price_format) == 39:
        p1 = price_format[27:32]
        p2 = price_format[27:32]

    if len(price_format) == 40:
        p1 = price_format[27:34]
        p2 = price_format[27:34]

    if len(price_format) == 41:
        p1 = price_format[28:34]
        p2 = price_format[28:34]

# First step to the code printing
    link = product.find('a', attrs={'class': 'ui-search-link'})


# Arrays to manipulate

    # for a_title in title:
    # title_array = [a_title]
    # print(title_array)

    # Arrays to manipulate
    # for a_price in price:
    #  price_array = [a_price.text]
    #   print(price_array)

    # for a_link in link:
    # link_array = [a_link.text, link['href']]
    # print(link_array)

    print('Data e horário da consulta: {} \n Título do produto: {} \n Preço do produto: R$ {} \n Link do produto: {} \n'
          .format(data_e_hora_em_texto, title.text, p2, link['href']))

    # Character counter
    #t = len(price_format)
    # print(t)

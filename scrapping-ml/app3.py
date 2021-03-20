import requests as r
from bs4 import BeautifulSoup as soup

page = r.get('https://coleccionables.mercadolibre.com.ar/juegos-mesa-cartas-rpg/magic/_PublishedToday_YES')

page_soup = soup(page.content, "html.parser")
title = page_soup.select('div.ui-search-item__group ui-search-item__group--title h2.ui-search-item__title ui-search-item__group__element')
print(type(title))


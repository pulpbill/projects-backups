from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://coleccionables.mercadolibre.com.ar/juegos-mesa-cartas-rpg/magic/_PublishedToday_YES'

# opening up connection, grabbing the page 
uClient = uReq(my_url)

# offloading the content into a variable
page_html = uClient.read()

# Closing the connection
uClient.close()

# Calling soup on the html page to parse it
page_soup = soup(page_html, "html.parser")

# Grabs each product
#containers = page_soup.findAll("div", {"class": "andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default andes-card--animated"})
#containers = page_soup.findAll("div", {"class": "ui-search-results"})
#this
containers = page_soup.findAll("div", {"class": "ui-search"})
containerTitle = containers[0]

#Just the name of the article
#test = containerTitle.div.div.div.div.div.div.img["alt"]

# Test
#print(len(containerTitle))
#print(containerTitle)
containerTitle = page_soup.findAll("div", {"class": "slick-slide slick-active"})
#print(test)

for container in containerTitle:
    titles = container.findAll("img", {"class": "alt"})
#    titles = container.div.img["alt"]
    print(titles)
    print(type(titles))

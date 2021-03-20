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
containers = page_soup.findAll("div", {"class": "andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default andes-card--animated"})

containerTitle = containers[0]
test = containerTitle.div.div.div.div.div.div.img["alt"]

# Test
#print(len(containers))
#print(containers[0])
#print(containerTitle)

for container in containerTitle:
    print(test)

#print(test)
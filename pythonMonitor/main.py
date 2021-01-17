from bs4 import BeautifulSoup
import requests
import time
import datetime
from currency_converter import CurrencyConverter

c = CurrencyConverter()


# Supreme New York Shop supremeUrl
supremeUrl = 'https://www.supremenewyork.com/shop'

r = requests.get(supremeUrl)
supremeContent = r.content

# Supreme Shop Soup
supremeSoup = BeautifulSoup(supremeContent, 'html.parser')
supremeScroller = supremeSoup.find('ul', id='shop-scroller')

# All List Items In Scroller
listItems = supremeScroller.find_all('li')


for item in listItems:

    itemAnchor = item.find('a')
    itemLink = itemAnchor.get('href')

    # Product Link
    productLinkFinal = f"https://www.supremenewyork.com{itemLink}"

    productRequest = requests.get(productLinkFinal)
    productContent = productRequest.content

    # Product Link Soup
    productSoup = BeautifulSoup(productContent, 'html.parser')
    productHeadings = productSoup.find_all('h1')
    productIndex1 = productHeadings[1]

    # Product Title
    productTitle = productIndex1.get_text()

    findProductPrice = productSoup.find('p', class_='price')

    # Product Price
    productPrice = findProductPrice.text

    priceRemoveComma = productPrice.replace(',', '')
    priceRemoveYen = priceRemoveComma.replace('¥', '')
    productPriceUSD = c.convert(priceRemoveYen, 'JPY', 'USD')
    productPriceUSD = round(productPriceUSD, 2)

    productImages = productSoup.find_all('img')
    productImages1 = productImages[0]

    # Product Image Link
    images = productImages1.get('src')



    # Getting Current Date and Time
    now = datetime.datetime.utcnow()
    timeNow = now.strftime('%H:%M:%S UTC on %A, %B the %dth, %Y')


    print(f"""
    =====================================
    Supreme Monitors
    {productTitle}
    {productLinkFinal}
    Price: ${productPriceUSD}, {productPrice}
    Updated: {timeNow}
    © github.com/1nsaNeDynamic
    """)


    time.sleep(1)

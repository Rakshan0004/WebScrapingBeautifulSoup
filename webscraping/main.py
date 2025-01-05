from bs4 import BeautifulSoup

with open('C:/Projects/WebScrapingBeautifulSoup/webscraping/index.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    products_html_tags = soup.find_all('h2')
    for product in products_html_tags:
        print(product.text.strip())

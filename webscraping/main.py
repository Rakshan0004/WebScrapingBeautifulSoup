from bs4 import BeautifulSoup

with open('C:/Projects/WebScrapingBeautifulSoup/webscraping/index.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    # products_html_tags = soup.find_all('h2')
    # for product in products_html_tags:
    #     print(product.text)

    product_cards = soup.find_all('div', class_='section')

    product_list = []

    for product in product_cards:
        product_name = product.h2.text.strip()
        product_price = product.button.text.strip() 

        product_list.append({"name": product_name, "price": product_price})
    print(product_list)



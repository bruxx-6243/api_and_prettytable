from prettytable import PrettyTable
import requests
import json


def displayDataTable(api_url):
    response = requests.get(api_url)
    # print(response.status_code)

    data = response.text
    parse_json = json.loads(data)
    products = parse_json['products']

    table = PrettyTable()

    for product in products:
        title = product['title']
        category = product['category']
        brand = product['brand']
        rating = product['rating']
        stock = product['stock']
        price = product['price']

        table.field_names = ['title', 'brand', 'category', 'rating', 'stock', 'price']
        table.add_row([title, brand, category, rating, stock, price])

    return table

print(displayDataTable('https://dummyjson.com/products'))
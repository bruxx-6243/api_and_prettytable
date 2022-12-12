from prettytable import PrettyTable
import requests

api_url = 'https://dummyjson.com/products/'

def displayDataTable():
    response = requests.get(api_url)

    if(response.status_code != 200):
        return "Request failed with status code: ", + response.status_code
    else:
        data = response.json()
        products = data['products']

        #Create the table
        table = PrettyTable()

        for product in products:
            title = product['title']
            category = product['category']
            brand = product['brand']
            rating = product['rating']
            stock = product['stock']
            price = product['price']

            #Fill the table with the products
            table.field_names = ['title', 'brand', 'category', 'rating', 'stock', 'price']
            table.add_row([title, brand, category, rating, stock, price])

        return table

print(displayDataTable())
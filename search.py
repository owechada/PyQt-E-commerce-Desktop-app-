import requests
from product import Products
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QScrollArea, QMessageBox

from test import GroceryApp
import sys

class ProductSearch:
    def __init__(self, api_endpoint=None):
        self.api_endpoint = api_endpoint

    def editPrice(self, price):
        replacements = {
            "₹": "",
            ",": ""
        }
        for old, new in replacements.items():
            price = price.replace(old, new)
        return int(price)

    def search_products(self, query=None):

        self.ppp=[]
        headers = {
            "X-RapidAPI-Key": "463ef49b89msh3cf45c255bf0477p19d199jsnc90357348d2f",
            "X-RapidAPI-Host": "ecommerce-product-api1.p.rapidapi.com"
        }
        try:
            response = requests.get(self.api_endpoint, headers=headers, params=query)
            response.raise_for_status()  # Raise an exception if response status is not 200
            api_data = response.json()
            products = []
            for item in api_data:
                count=0
                if "title" and "image" and "price" in item:
                    product = Products(
                        image=item.get('image'),
                        title=item.get('title'),
                        price=self.editPrice(item.get('price')),
                        description=item.get('description'),id=count
                    )
                    products.append(product)
                    count=count+1
           
            # Create the app window and display products
            window = GroceryApp(products)
            print(len(products))
            window.setFixedHeight(600)
            window.setFixedWidth(850)
            window.show()
    #self.hide()
           
       
            return products
        except requests.exceptions.RequestException as e:
            print("Error fetching product data from the API:", e)
            return []


        return self.ppp

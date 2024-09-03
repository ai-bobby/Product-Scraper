from bs4 import BeautifulSoup
import requests
import json


class Base(object):
    # Read objects from a JSON file and return them as a list
    @staticmethod
    def read_objects_from_json_file(path):
        with open(path, 'r', encoding='utf-8') as file1:
            try:
                current_objects = json.load(file1)
            except:
                # If the file is empty or there's an error, return an empty list
                current_objects = []
        return current_objects

    # Write a list of objects to a JSON file
    @staticmethod
    def write_objects_to_json_file(path, objects):
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(objects, file, ensure_ascii=False, indent=4)

    # Add a new object to the JSON file
    @classmethod
    def add_object_to_json_file(cls, path, element):
        obj = cls.read_objects_from_json_file(path)
        obj.append(element)
        cls.write_objects_to_json_file(path, obj)


class Product(Base):
    # Initialize a Product object with a name and price
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Convert the Product object to a dictionary format
    def to_dict(self):
        return {
            'Name': self.name,
            'Price': self.price
        }

    # String representation of the Product object
    def __str__(self):
        return f"{self.name} - {self.price}"


def main():
    # URL of the website to scrape
    URL = "https://www.entekhabcenter.com/product-category/product/audio-video/television"
    # Path to the JSON file where products will be stored
    JSON_FILE = 'products.json'

    # Send a GET request to the URL
    response = requests.get(URL)
    # Get the HTML content of the page
    html = response.text

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    # CSS selector for the product container
    product_selector = "div.sec-2-p"
    # CSS selector for the product name
    name_selector = 'a>h5'
    # CSS selector for the product price
    price_selector = 'div.prodcut-price>ins'

    # Loop through each product on the page
    for item in soup.select(product_selector):
        # Extract the product name and price
        name = item.select_one(name_selector).text.strip()
        price = item.select_one(price_selector).text.strip()

        # Create a Product object with the extracted name and price
        product = Product(name, price)
        # Convert the Product object to a dictionary
        product_dict = product.to_dict()

        # Add the product dictionary to the JSON file
        Product.add_object_to_json_file(JSON_FILE, product_dict)

    # Read the products from the JSON file and print them
    products = Product.read_objects_from_json_file(JSON_FILE)
    for product in products:
        print(f"Name: {product['Name']}, Price: {product['Price']}")


if __name__ == "__main__":
    main()


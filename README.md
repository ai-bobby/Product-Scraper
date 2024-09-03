# Product Scraper

This Python script scrapes product information (name and price) from a specific webpage and stores it in a JSON file. The script is designed to fetch the HTML content of a webpage, parse it to extract product data, and then save this data in a structured format for further use.

## Features

- **Web Scraping**: The script uses the `requests` library to retrieve HTML content from a webpage.
- **HTML Parsing**: It employs `BeautifulSoup` from the `bs4` library to parse the HTML and extract specific data points (product name and price).
- **JSON Handling**: The script reads from and writes data to a JSON file, allowing persistent storage of the scraped product information.
- **OOP Design**: The code is structured using object-oriented programming (OOP) principles, making it modular and extensible.

## Prerequisites

Before running the script, ensure that the following Python libraries are installed:

- `requests`
- `beautifulsoup4`

You can install them using `pip`:

```bash
pip install requests beautifulsoup4
```
## How It Works

### Base Class
Provides methods for reading and writing JSON files.

- `read_objects_from_json_file(path)`: Reads and returns a list of objects from a specified JSON file.
- `write_objects_to_json_file(path, objects)`: Writes a list of objects to a specified JSON file.
- `add_object_to_json_file(path, element)`: Adds a new object to the existing list in the JSON file.

### Product Class
Inherits from the Base class and represents a product with a name and price.

- `to_dict()`: Converts the Product object into a dictionary format.
- `__str__()`: Returns a string representation of the Product object.

### Main Functionality

- The script targets a specific URL containing product listings.
- It parses the webpage to extract product names and prices using CSS selectors.
- The extracted data is stored as `Product` objects and then serialized into a JSON file (`products.json`).
- The script finally reads from the JSON file and prints the stored products.

## Usage

To run the script, simply execute it with Python:

```bash
python your_script_name.py

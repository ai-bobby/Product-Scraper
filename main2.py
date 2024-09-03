import logging
from functools import wraps
import requests
from bs4 import BeautifulSoup


# Configure logging settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# Decorator for logging
def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            # Log the function call with arguments
            logger.info(f"Function '{func.__name__}' called with args: {args} and kwargs: {kwargs}")

            # Execute the original function
            result = func(*args, **kwargs)

            # Log the result of the function
            logger.info(f"Function '{func.__name__}' returned {result}")

            return result
        except Exception as e:
            logger.error(f"Error in function '{func.__name__}': {e}")
            raise

    return wrapper


@log_decorator
def fetch_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {e}")
        return None


@log_decorator
def parse_product_info(html, product_selector, name_selector, price_selector):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        products = []
        for item in soup.select(product_selector):
            name = item.select_one(name_selector)
            price = item.select_one(price_selector)
            if name and price:  # Ensure that both name and price are found
                products.append({
                    'Name': name.text.strip(),
                    'Price': price.text.strip()
                })
        return products
    except Exception as e:
        logger.error(f"Failed to parse product info: {e}")
        return []


@log_decorator
def main():
    URL = "https://www.entekhabcenter.com/product-category/product/audio-video/television"
    JSON_FILE = 'products.json'

    html = fetch_webpage(URL)
    if html:
        product_selector = "div.sec-2-p"
        name_selector = 'a>h5'
        price_selector = 'div.prodcut-price>ins'
        products = parse_product_info(html, product_selector, name_selector, price_selector)
        if products:
            for product in products:
                product.add_object_to_json_file(JSON_FILE, product)


if __name__ == "__main__":
    main()

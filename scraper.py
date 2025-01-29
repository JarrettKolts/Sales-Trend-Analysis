import requests
from bs4 import BeautifulSoup

# product_url = "https://www.amazon.com/dp/B0979LYGMS?ref=ppx_yo2ov_dt_b_fed_asin_title"

# def get_product_data(product_url):
#     """
#     Scrapes product data from the provided URL.

#     Args:
#         product_url (str): The URL of the product page to scrape.

#     Returns:
#         list: A list of dictionaries containing product data.
#     """
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#         'Accept-Language': 'en-US,en;q=0.9',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Connection': 'keep-alive',
#         'Upgrade-Insecure-Requests': '1',
#     }

#     session = requests.Session()  # Using a session to maintain cookies
#     response = session.get(product_url, headers=headers)

#     # Check if the request was successful
#     if response.status_code != 200:
#         print(f"Error: Unable to fetch the webpage. Status code: {response.status_code}")
#         print(f"Response content: {response.content[:500]}")  # Print a snippet of the response content for debugging
#         return []

#     # Parse the HTML content
#     soup = BeautifulSoup(response.content, 'html.parser')

#     # Scraping product name, price, and rating
#     product_data = {}

#     product_name = soup.find("span", {"id": "productTitle"})
#     if product_name:
#         product_data["Name"] = product_name.text.strip()
#     else:
#         product_data["Name"] = "N/A"

#     price = soup.find("span", {"class": "a-price-whole"})
#     if price:
#         product_data["Price"] = price.text.strip()
#     else:
#         product_data["Price"] = "N/A"

#     rating = soup.find("span", {"class": "a-icon-alt"})
#     if rating:
#         product_data["Rating"] = rating.text.strip()
#     else:
#         product_data["Rating"] = "N/A"

#     # Return the product data
#     return [product_data]

# Call the function with the product_url
# scraped_data = get_product_data(product_url)


# scraper.py

def get_product_data():
    """
    Simulates scraping product data (currently hardcoded).
    
    Returns:
        list: A list of dictionaries containing product data.
    """
    product_data = [
        {
            "Name": "2021 Apple iMac",
            "Price": "$699.99",
            "Rating": "4.0 out of 5 stars"
        },
        {
            "Name": "2024 Apple iMac",
            "Price": "$1194.00",
            "Rating": "4.8 out of 5 stars"
        },
        {
            "Name": "Apple Studio Display",
            "Price": "$1439.00",
            "Rating": "4.6 out of 5 stars"
        }
    ]
    
    return product_data

# scraped_data = get_product_data()

# print(scraped_data)
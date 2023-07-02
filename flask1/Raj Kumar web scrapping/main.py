import requests
from bs4 import BeautifulSoup

# Function to scrape Flipkart page and extract product details
def scrape_flipkart(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }  # User-Agent header to mimic a browser

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find product details on the page
    products = soup.find_all("div", {"class": "_1AtVbE"})
    for product in products:
        title = product.find("a", {"class": "IRpwTa"}).text.strip()
        price = product.find("div", {"class": "_30jeq3 _1_WHN1"}).text.strip()
        rating = product.find("div", {"class": "_3LWZlK"}).text.strip()

        print("Title:", title)
        print("Price:", price)
        print("Rating:", rating)
        print("-" * 50)

# Main scraping function
def scrape_flipkart_pages():
    base_url = "https://www.flipkart.com/"  # Base URL of the Flipkart page
    page_number = 1
    while True:
        url = base_url + f"?page={page_number}"  # Append page number to the URL
        scrape_flipkart(url)

        # Move to the next page
        page_number += 1

        # Check if there are more pages available
        next_page_element = soup.find("a", {"class": "_1LKTO3"})
        if not next_page_element:
            break

# Call the main scraping function to start scraping
scrape_flipkart_pages()

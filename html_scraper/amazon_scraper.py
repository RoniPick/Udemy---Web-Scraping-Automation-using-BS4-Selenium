from datetime import datetime
import requests
import csv
import bs4 

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Crome/96.0.4664.45 Safari/537.36' 
REQUEST_HEADER = {'User-Agent': USER_AGENT,  # Device and browser details
                  'Accept-Language': 'en-US,en;q=0.5'} # Language details


# Get the HTML from the URL
def get_html(url):
    res = requests.get(url=url, headers=REQUEST_HEADER) # Get the HTML from the URL
    return res.text

# Extract the product info from the HTML
def extract_product_info(url):
    product_info = {}
    print(f'Scrapping URL: {url}')
    html = get_html(url=url) # Get the HTML from the URL
    print(html)


if __name__ == "__main__":
    with open('amazon_products_urls.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            url = row[0]
            print(extract_product_info(url))
    
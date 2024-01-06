from datetime import datetime
import requests
import csv
import bs4 

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
REQUEST_HEADER = {'User-Agent': USER_AGENT,  # Device and browser details
                  'Accept-Language': 'en-US,en;q=0.5'} # Language details


# Get the HTML from the URL
def get_html(url):
    res = requests.get(url=url, headers=REQUEST_HEADER) # Get the HTML from the URL
    return res.text


# Get the product price from the HTML
def get_product_price(soup):
    main_price_span = soup.find('span', attrs={
        'class': 'a-price a-text-price a-size-medium apexPriceToPay'
    })
    if main_price_span is not None:
        price_spans = main_price_span.find_all('span')
        for span in price_spans:
            price = span.text.strip().replace('$', '').replace(',', '')
            try:
                return float(price)
            except ValueError:
                print("Value Obtained Fot Price Could Not Be Converted To Float.")
    else:
        print("Price information not found.")


# Get the product title from the HTML
def get_product_title(soup):
    product_title = soup.find('span', id='productTitle')
    if product_title is not None:
        return product_title.text.strip()
    else:
        print("Title information not found.")
        return None  # or return a default value if you prefer


# Get the product rating from the HTML
def get_product_rating(soup):
    product_ratings_div = soup.find('div', attrs={
        'id': 'averageCustomerReviews'
    })
    if product_ratings_div is None:
        print("Rating information not found.")
        return None
    else:
        product_rating_section = product_ratings_div.find(
            'i', attrs={'class': 'a-icon-star'})
        if product_rating_section is None:
            print("Rating information not found.")
            return None
        else:
            product_rating_span = product_rating_section.find('span')
            try:
                rating = product_rating_span.text.strip().split()
                return float(rating[0])
            except ValueError:
                print("Value Obtained For Rating Could Not Be Parsed")
                exit()


# Get the product technical details from the HTML
def get_product_technical_details(soup):
    details = {}
    technical_details_section = soup.find('div', id='prodDetails')
    
    if technical_details_section is not None:
        data_tables = technical_details_section.findAll(
            'table', class_='prodDetTable')
        
        for table in data_tables:
            table_rows = table.find_all('tr')
            for row in table_rows:
                row_key = row.find('th').text.strip()
                row_value = row.find('td').text.strip().replace('\u200e', '')
                details[row_key] = row_value
    
    return details









# Extract the product info from the HTML
def extract_product_info(url):
    product_info = {}
    print(f'Scrapping URL: {url}')
    html = get_html(url=url) # Get the HTML from the URL
    soup = bs4.BeautifulSoup(html, 'lxml') # Create a BeautifulSoup object
    
    product_info['price'] = get_product_price(soup)  # Get the product price from the HTML
    product_info['title'] = get_product_title(soup)  # Get the product title from the HTML
    product_info['rating'] = get_product_rating(soup)   # Get the product rating from the HTML
    product_info.update(get_product_technical_details(soup)) # Get the product technical details from the HTML
    print(product_info)


if __name__ == "__main__":
    with open('amazon_products_urls.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            url = row[0]
            extract_product_info(url)
    
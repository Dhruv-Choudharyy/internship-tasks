import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape Amazon search results
def scrape_amazon(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = []

    # Extracting product information
    for product in soup.find_all('div', {'data-component-type': 's-search-result'}):
        try:
            name = product.find('span', {'class': 'a-size-base-plus a-color-base a-text-normal'}).text.strip()
        except AttributeError:
            name = 'Not available'

        try:
            price = product.find('span', {'class': 'a-price'}).find('span', {'class': 'a-offscreen'}).text.strip()
        except AttributeError:
            price = 'Not available'

        try:
            rating = product.find('span', {'class': 'a-icon-alt'}).text.split(' ')[0]
        except AttributeError:
            rating = 'Not available'

        products.append({
            'Name': name,
            'Price': price,
            'Rating': rating
        })

    return products

# Main function to execute scraping and save data to CSV
# Main function to execute scraping and save data to CSV
def main():
    url = 'https://www.amazon.com/s?k=phone&crid=305C9YI4X4XH8&sprefix=phon%2Caps%2C295&ref=nb_sb_noss_1'
    products = scrape_amazon(url)

    # Saving to CSV file
    csv_filename = 'amazon_phones.csv'
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Name', 'Price', 'Rating']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for product in products:
            writer.writerow(product)
            print(f"Name: {product['Name']}, Price: {product['Price']}, Rating: {product['Rating']}")

    print(f'Scraping and CSV creation complete. Saved as {csv_filename}')

if __name__ == '__main__':
    main()

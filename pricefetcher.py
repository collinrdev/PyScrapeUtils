import requests
from bs4 import BeautifulSoup
import re

# Get URL
url = input("Enter the URL to scrape for product prices: ")

try:
    # Fetch page content
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    # Define price regex
    price_pattern = re.compile(r'(\$\s?\d+(?:,\d{3})*(?:\.\d{2})?)')

    # Scan all text-containing elements (spans, divs, etc.)
    matches = []

    for tag in soup.find_all(['div', 'span', 'p', 'li']):
        text = tag.get_text(separator=' ', strip=True)
        prices = price_pattern.findall(text)
        if prices:
            # Clean surrounding text
            context = text.strip()
            for price in prices:
                matches.append((price, context))

    # Show results
    unique = list(set(matches))
    if unique:
        print("\n📦 Price Matches with Context:\n")
        for price, context in unique:
            # Try to shorten the context if too long
            snippet = context if len(context) <= 150 else context[:140] + '...'
            print(f"{price} → {snippet}")
    else:
        print("No prices found.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching the page: {e}")
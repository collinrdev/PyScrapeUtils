import requests
from bs4 import BeautifulSoup
import re
import csv

# Get user input
url = input("Enter the URL to scrape: ")
filename = input("Enter a name for your output CSV file (e.g., prices.csv): ")

try:
    # Fetch the page
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    # Define price regex
    price_pattern = re.compile(r'(\$\s?\d+(?:,\d{3})*(?:\.\d{2})?)')

    results = []

    # Search common containers for prices and context
    for tag in soup.find_all(['div', 'span', 'p', 'li']):
        text = tag.get_text(separator=' ', strip=True)
        prices = price_pattern.findall(text)
        if prices:
            for price in prices:
                # Save both price and trimmed context
                snippet = text if len(text) <= 200 else text[:200] + '...'
                results.append((price, snippet))

    # Deduplicate
    results = list(set(results))

    if not results:
        print("No prices found.")
    else:
        # Write to CSV
        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Price', 'Associated Text'])
            for price, context in results:
                writer.writerow([price, context])

        print(f"\n✅ {len(results)} price entries saved to '{filename}'")

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
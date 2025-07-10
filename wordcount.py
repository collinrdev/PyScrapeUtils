import requests
from bs4 import BeautifulSoup

# Retrieve user input
url = input("Enter the URL: ")
search_string = input("Enter the string to search for: ").lower()

try:
    # Send HTTP request
    response = requests.get(url)
    response.raise_for_status()  # Raise error for bad response

    # Parse HTML content and extract visible text
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text().lower()  # Convert to lowercase for case-insensitive search

    # Count occurrences of search_string
    count = text.count(search_string)

    # Output number of search_string
    print(f"\nThe string '{search_string}' appears {count} times on the page.")
except requests.exceptions.RequestException as e:
    print(f"Error fetching page: {e}")
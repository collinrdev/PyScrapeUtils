import requests
from bs4 import BeautifulSoup

def count_string_occurrences():
    url = input("Enter the URL: ")
    search_string = input("Enter the string to search for: ").lower()

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text().lower()
        count = text.count(search_string)
        print(f"\nThe string '{search_string}' appears {count} times on the page.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
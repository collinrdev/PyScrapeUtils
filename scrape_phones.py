import requests
from bs4 import BeautifulSoup
import re

def scrape_phone_numbers():
    url = input("Enter the URL to scan for phone numbers: ")

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        text = soup.get_text(separator=' ', strip=True)

        # Regex to match various phone number formats
        phone_pattern = re.compile(
            r'(\+?\d{1,2}[-.\s]?)?(\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}'
        )

        matches = phone_pattern.findall(text)

        # Clean and deduplicate numbers
        phones = set()
        for match in matches:
            number = ''.join(match)
            cleaned = re.sub(r'\D', '', number)
            if len(cleaned) >= 10:
                phones.add(cleaned)

        if phones:
            print("\n Phone numbers found:\n")
            for phone in sorted(phones):
                formatted = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}" if len(phone) == 10 else phone
                print(f"• {formatted}")
        else:
            print("No phone numbers found.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
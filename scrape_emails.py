import re
import requests
from bs4 import BeautifulSoup

def scrape_emails_from_url(url):
    """
    Scrapes and returns a list of unique email addresses from the given URL.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"[!] Error fetching URL: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()

    # Regex pattern for matching emails
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)

    return list(set(emails))
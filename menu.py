from count_occurrences import count_string_occurrences
from scrape_prices import scrape_prices_to_csv
from scrape_emails import scrape_emails_from_url  # <- New import

def main_menu():
    while True:
        print("\n📋 MENU")
        print("1. Count a specific string on a web page")
        print("2. Scrape prices and export to CSV")
        print("3. Scrape emails from a web page")  # <- New option
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            count_string_occurrences()
        elif choice == '2':
            scrape_prices_to_csv()
        elif choice == '3':
            url = input("Enter a URL to scrape for emails: ").strip()
            emails = scrape_emails_from_url(url)

            if emails:
                print(f"✅ Found {len(emails)} email(s):")
                for email in emails:
                    print(" -", email)
            else:
                print("❌ No emails found or an error occurred.")
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
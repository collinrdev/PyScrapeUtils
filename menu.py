from count_occurrences import count_string_occurrences
from scrape_prices import scrape_prices_to_csv

def main_menu():
    while True:
        print("\n📋 MENU")
        print("1. Count a specific string on a web page")
        print("2. Scrape prices and export to CSV")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            count_string_occurrences()
        elif choice == '2':
            scrape_prices_to_csv()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
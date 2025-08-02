import requests
from bs4 import BeautifulSoup

def scrape_opentable(restaurant_name, date, time):
    """
    Scrapes OpenTable for available reservation slots for a given restaurant, date, and time.

    Args:
        restaurant_name (str): Name of the restaurant to search for.
        date (str): Date in YYYY-MM-DD format.
        time (str): Time in HH:MM format (24-hour clock).

    Returns:
        list: A list of available reservation times.
    """
    base_url = "https://www.opentable.com"
    search_url = f"{base_url}/search"

    # Parameters for the search query
    params = {
        "covers": 2,  # Number of people
        "dateTime": f"{date}T{time}",
        "term": restaurant_name,
    }

    # Send a GET request to OpenTable's search page
    response = requests.get(search_url, params=params)

    if response.status_code != 200:
        print("Failed to fetch data from OpenTable.")
        return []

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find available reservation times (example: adjust based on actual HTML structure)
    slots = []
    for slot in soup.find_all("button", class_="time-button"):  # Adjust class name as needed
        slots.append(slot.text.strip())

    return slots

def main():
    print("OpenTable Reservation Scraper")
    restaurant_name = input("Enter the restaurant name: ").strip()
    date = input("Enter the date (YYYY-MM-DD): ").strip()
    time = input("Enter the time (HH:MM, 24-hour format): ").strip()

    slots = scrape_opentable(restaurant_name, date, time)

    if slots:
        print("Available reservation slots:")
        for slot in slots:
            print(f"  - {slot}")
    else:
        print("No available slots found.")

if __name__ == "__main__":
    main()

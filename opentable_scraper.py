from urllib.parse import urlencode

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright

# OpenTable's search results are rendered client-side by JS, so a plain HTTP
# GET (the previous requests/BeautifulSoup approach) never sees the actual
# time-slot buttons — only the pre-render page shell. This drives a real
# (headless) browser instead and waits for the slots to render before reading
# the DOM.
#
# SLOT_SELECTOR is a placeholder: this environment's network policy blocks
# opentable.com, so it could not be verified against the live site. To find
# the real one: open a restaurant search on opentable.com, right-click a
# reservation time button, "Inspect", and copy its selector here.
SLOT_SELECTOR = "button[data-test='time-slot']"


def scrape_opentable(restaurant_name: str, date: str, time: str) -> list[str]:
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
    params = {
        "covers": 2,  # Number of people
        "dateTime": f"{date}T{time}",
        "term": restaurant_name,
    }
    search_url = f"{base_url}/search?{urlencode(params)}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            page = browser.new_page(user_agent="Mozilla/5.0")
            try:
                page.goto(search_url, timeout=15000)
                page.wait_for_selector(SLOT_SELECTOR, timeout=10000)
            except PlaywrightTimeoutError:
                print("No reservation slots appeared (the page may not have "
                      "loaded, or SLOT_SELECTOR is out of date).")
                return []
            return [el.inner_text().strip() for el in page.query_selector_all(SLOT_SELECTOR)]
        finally:
            browser.close()

def main() -> None:
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

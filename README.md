# Restaurant Seats Checker

A simple command-line application for checking restaurant seat openings for specific days or the next available times. Designed for family use.

## How to Use

1. Run the app:
   ```
   python restaurant_seats.py
   ```
2. Choose to check openings for a specific day or see the next available times.
3. Follow the prompts.

## Customization
- Edit `restaurants.json` to add or update restaurant data.

## OpenTable Scraper
`opentable_scraper.py` is a separate, standalone tool for looking up live
availability on OpenTable (it does not feed into `restaurant_seats.py`).
It uses Playwright to render the page in a headless browser, since
OpenTable's search results are rendered by JavaScript.

1. Install dependencies: `pip install -r requirements.txt`
2. Install the browser binary (one-time): `playwright install chromium`
3. Run: `python opentable_scraper.py`

`SLOT_SELECTOR` in that file is a placeholder and may need updating to match
OpenTable's current markup — inspect a reservation time button in your
browser's devtools and copy its selector in if it stops finding slots.

## Requirements
- Python 3.7+ (only needed for `restaurant_seats.py`; the scraper needs
  Playwright — see above)

## Privacy
This app is intended for private, family use. No data is sent or stored externally.

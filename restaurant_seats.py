import datetime
import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "restaurants.json"


def load_restaurants() -> dict:
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        print(f"Failed to load {DATA_FILE.name}: {e}")
        raise SystemExit(1)


def check_openings_for_day(restaurants: dict, day: str) -> None:
    print(f"Openings for {day}:")
    found = False
    for name, info in restaurants.items():
        times = info["openings"].get(day, [])
        if times:
            print(f"  {name}: {', '.join(times)}")
            found = True
        else:
            print(f"  {name}: No openings")
    if not found:
        print("No openings found for any restaurant on this day.")

def check_next_available(restaurants: dict) -> None:
    print("Next available openings:")
    today = datetime.date.today()
    found = False
    for name, info in restaurants.items():
        next_day = None
        next_times = None
        for day in sorted(info["openings"].keys()):
            day_date = datetime.datetime.strptime(day, "%Y-%m-%d").date()
            if day_date >= today:
                next_day = day
                next_times = info["openings"][day]
                break
        if next_day:
            print(f"  {name}: {next_day} - {', '.join(next_times)}")
            found = True
        else:
            print(f"  {name}: No upcoming openings")
    if not found:
        print("No upcoming openings found for any restaurant.")

def main() -> None:
    restaurants = load_restaurants()
    print("Restaurant Openings Checker")
    print("1. Check openings for a specific day")
    print("2. Check next available openings")
    choice = input("Enter your choice (1/2): ").strip()
    if choice == "1":
        day = input("Enter date (YYYY-MM-DD): ").strip()
        check_openings_for_day(restaurants, day)
    elif choice == "2":
        check_next_available(restaurants)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()

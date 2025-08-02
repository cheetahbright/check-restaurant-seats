import datetime

# Sample restaurant data
restaurants = {
    "Pizza Place": {
        "openings": {
            "2025-08-01": ["18:00", "19:00", "20:00"],
            "2025-08-02": ["17:00", "18:30"],
        }
    },
    "Sushi Bar": {
        "openings": {
            "2025-08-01": ["17:30", "19:30"],
            "2025-08-03": ["18:00", "20:00"],
        }
    },
    "Burger Joint": {
        "openings": {
            "2025-08-02": ["18:00", "19:00"],
            "2025-08-03": ["17:00", "18:30", "20:00"],
        }
    }
}

def check_openings_for_day(day):
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

def check_next_available():
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

def main():
    print("Restaurant Openings Checker")
    print("1. Check openings for a specific day")
    print("2. Check next available openings")
    choice = input("Enter your choice (1/2): ").strip()
    if choice == "1":
        day = input("Enter date (YYYY-MM-DD): ").strip()
        check_openings_for_day(day)
    elif choice == "2":
        check_next_available()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()

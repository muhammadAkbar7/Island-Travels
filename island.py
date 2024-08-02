from datetime import datetime, timedelta
import random

def show_welcome_screen():
    print("-" * 52)
    print("|{:^50}|".format("Welcome"))
    print("|{:^50}|".format("Island Selection:"))
    print("|{:>10} {:<38}|".format("a)", "Maui"))
    print("|{:>10} {:<38}|".format("b)", "Oahu"))
    print("|" + " " * 50 + "|")
    print("|{:^50}|".format("(Type the indicated letter to"))
    print("|{:^50}|".format("choose an island and press"))
    print("|{:^50}|".format("Enter to go to the main page)"))
    print("|" + " " * 50 + "|")
    print("|{:^50}|".format("(Please choose an island for your"))
    print("|{:^50}|".format("upcoming travels as you can use the"))
    print("|{:^50}|".format("information found in this program to plan and prepare."))
    print("|" + " " * 50 + "|")
    print("-" * 52)

def show_island_page(island_name, email=None):
    print("-" * 52)
    print("|{:^50}|".format(f"Main Page: {island_name}"))
    print("|" + " " * 50 + "|")
    if email:
        print(f"| E-mail: {email:<39}|")
    else:
        print("|{:^50}|".format("E-mail address or not"))
        print("|{:>10} {:<38}|".format("y)", "enter email"))
        print("|{:>10} {:<38}|".format("n)", "don't enter email"))
    print("|" + " " * 50 + "|")
    print("|{:^50}|".format("Actions:"))
    print("|{:^50}|".format("Go to:"))
    print("|{:>10} {:<38}|".format("w)", "Weather"))
    print("|{:>10} {:<38}|".format("l)", "Local Events"))
    print("|{:>10} {:<38}|".format("s)", "Safety"))
    print("|" + " " * 50 + "|")
    print("|{:^50}|".format("Deletion:"))
    print("|{:>10} {:<38}|".format("d)", "Delete current email"))
    print("|" + " " * 50 + "|")
    print("|{:^50}|".format("(Type the indicated letter and"))
    print("|{:^50}|".format("press Enter to proceed)"))
    print("-" * 52)

def generate_safety_alerts():
    # Example mock data for safety alerts
    types_of_alerts = ["Natural Disaster", "Shark Attack", "Flood", "Fire", "Landslide"]
    severity_levels = ["!!!", "!!", "!"]
    alerts = []

    # Generate random alerts
    for _ in range(5):
        alert_type = random.choice(types_of_alerts)
        severity = random.choice(severity_levels)
        date = (datetime.now() - timedelta(days=random.randint(1, 30))).strftime('%b %d, %Y')
        alerts.append({"type": alert_type, "severity": severity, "date": date})

    return alerts

def categorize_alerts(alerts, category):
    if category == 't':
        # Sort by type
        return sorted(alerts, key=lambda x: x['type'])
    elif category == '!':
        # Sort by severity (most severe first)
        severity_levels = ["!!!", "!!", "!"]
        return sorted(alerts, key=lambda x: severity_levels.index(x['severity']))
    elif category == 'r':
        # Sort by most recent date
        return sorted(alerts, key=lambda x: datetime.strptime(x['date'], '%b %d, %Y'), reverse=True)
    else:
        return alerts

def show_safety_page(island_name, alerts, category=None):
    print("-" * 52)
    print("|{:^50}|".format(f"Safety and Danger Page - {island_name}"))
    print("-" * 52)
    print("| Current Safety Information for [{}] |".format(datetime.now().strftime('%b %d, %Y')))
    print("|{:^50}|".format("[Safety Information Display]"))
    print("-" * 52)

    if category:
        alerts = categorize_alerts(alerts, category)

    for alert in alerts:
        print(f"| {alert['type']:<15} Severity: {alert['severity']} Date: {alert['date']} |")

    print("-" * 52)
    print("| Categorize by:                              |")
    print("|{:>10} {:<38}|".format("t)", "Type"))
    print("|{:>10} {:<38}|".format("!", "Severity"))
    print("|{:>10} {:<38}|".format("r)", "Most Recent"))
    print("|                                              |")
    print("| * then a --> Enter Arrow Mode                |")
    print("-" * 52)
    print("| Local Navigation:                            |")
    print("|{:>10} {:<38}|".format("l)", "Local Events"))
    print("|{:>10} {:<38}|".format("w)", "Weather"))
    print("|{:>10} {:<38}|".format("s)", "Safety (current page)"))
    print("-" * 52)
    print("| Save Options:                                |")
    print("|{:>10} {:<38}|".format("ss)", "Save current safety info to file"))
    print("|{:>10} {:<38}|".format("u)", "Undo the most recent save"))
    print("-" * 52)
    print("| Navigation:                                  |")
    print("|{:>10} {:<38}|".format("b)", "Back to main menu"))
    print("-" * 52)
    print("|{:^50}|".format("[Enter the indicated letter]"))

def get_weather_forecast(start_date, end_date):
    # Simulated weather data
    weather_conditions = ["Sunny", "Partly Cloudy", "Rain", "Windy", "Overcast", "Showers", "Thunderstorms"]
    weather_forecast = {}
    current_date = start_date
    while current_date <= end_date:
        forecast = f"{weather_conditions[current_date.day % len(weather_conditions)]}, {78 + current_date.day % 10}°F"
        weather_forecast[current_date.strftime('%b %d')] = forecast
        current_date += timedelta(days=1)
    return weather_forecast

def show_weather_page(island_name, date_range=None):
    while True:
        print("-" * 52)
        print(f"|{'Weather Page':^50}|")
        print("|" + " " * 50 + "|")

        if date_range:
            try:
                start_date_str, end_date_str = date_range.split(' - ')
                start_date = datetime.strptime(start_date_str.strip(), "%m/%d/%Y")
                end_date = datetime.strptime(end_date_str.strip(), "%m/%d/%Y")
                if start_date > end_date:
                    raise ValueError("Start date cannot be after end date.")
                weather_forecast = get_weather_forecast(start_date, end_date)

                print(f"| Weather forecast for {island_name:<35}|")
                print(f"| from {start_date.strftime('%b %d')} – {end_date.strftime('%b %d')}: |")
                for date, forecast in weather_forecast.items():
                    print(f"| {date}: {forecast:<37}|")
                print("| ...                                          |")
                print(f"| {end_date.strftime('%b %d')}: {weather_forecast[end_date.strftime('%b %d')]:<37}|")
            except ValueError as ve:
                print(f"| Error: {str(ve):<44}|")
                print("| Invalid date range format.                    |")
        else:
            weather = "Sunny, 85°F" if island_name == "Maui" else "Partly Cloudy, 78°F"
            print(f"| Current weather for today: {weather:<24}|")

        print("|" + " " * 50 + "|")
        print("| Date Range for Vacation?                     |")
        print("|{:>10} {:<38}|".format("y)", "enter date"))
        print("|{:>10} {:<38}|".format("n)", "close prompt"))
        print("|" + " " * 50 + "|")
        print("|{:^50}|".format("Actions:"))
        print("| local navigation:                            |")
        print("|{:>10} {:<38}|".format("l)", "Local Events"))
        print("|{:>10} {:<38}|".format("w)", "Weather"))
        print("|{:>10} {:<38}|".format("s)", "Safety"))
        print("|" + " " * 50 + "|")
        print("|{:>10} {:<38}|".format("ss)", "save"))
        print("|{:>10} {:<38}|".format("u)", "undo the most recent save"))
        print("|{:>10} {:<38}|".format("b)", "back to main menu"))
        print("|" + " " * 50 + "|")
        print("|{:^50}|".format("(Type the indicated letter and"))
        print("|{:^50}|".format("press Enter to proceed)"))
        print("-" * 52)

        action_choice = input("Enter your action (y/n/u): ").lower()

        if action_choice == 'y':
            date_range = show_date_range_prompt()
        elif action_choice == 'u':
            print("Weather has been reset. Please enter a new date range.")
            date_range = None
        elif action_choice == 'n':
            break
        else:
            print("Invalid action. Please select a valid option.")
            continue

def show_date_range_prompt():
    print("-" * 52)
    print("|{:^50}|".format("Enter Date Range"))
    print("|" + " " * 50 + "|")
    print("| Please enter your vacation date range        |")
    print("| (e.g., 08/31/2024 - 09/10/2024):             |")
    print("|" + " " * 50 + "|")
    date_range = input("| Enter date range: ").strip()
    print("-" * 52)
    return date_range

def arrow_mode(alerts, island_name):
    categories = ['t', '!', 'r']
    category_labels = {'t': 'Type', '!': 'Severity', 'r': 'Most Recent'}
    current_index = 0
    while True:
        category = categories[current_index]
        print("-" * 52)
        print(f"Current Selection: {category_labels[category]}")
        arrow_choice = input("Use l (left) or r (right) arrow keys to scroll, c to confirm, q to quit: ").lower()
        if arrow_choice == 'l':
            current_index = (current_index - 1) % len(categories)
        elif arrow_choice == 'r':
            current_index = (current_index + 1) % len(categories)
        elif arrow_choice == 'c':
            show_safety_page(island_name, alerts, category)
            break
        elif arrow_choice == 'q':
            break
        else:
            print("Invalid input. Use l, r, c, or q.")

def confirm_deletion():
    print("+" + "-" * 48 + "+")
    print("|{:^48}|".format("Confirm Deletion"))
    print("+" + "-" * 48 + "+")
    print("|" + " " * 48 + "|")
    print("|{:^48}|".format("Are you sure you want"))
    print("|{:^48}|".format("to delete the current"))
    print("|{:^48}|".format("email associated with"))
    print("|{:^48}|".format("this session?"))
    print("|" + " " * 48 + "|")
    print("|{:^48}|".format("(Warning: Deleting"))
    print("|{:^48}|".format("this email will delete"))
    print("|{:^48}|".format("all the current data"))
    print("|{:^48}|".format("that was procured"))
    print("|{:^48}|".format("during that session.)"))
    print("|" + " " * 48 + "|")
    print("|{:>10} {:<38}|".format("y)", "Yes"))
    print("|{:>10} {:<38}|".format("n)", "No"))
    print("+" + "-" * 48 + "+")

def main():
    while True:
        show_welcome_screen()
        choice = input("Enter your choice (a/b): ").lower()

        if choice == 'a':
            island_name = "Maui"
            break
        elif choice == 'b':
            island_name = "Oahu"
            break
        else:
            print("Invalid choice. Please select either 'a' for Maui or 'b' for Oahu.")
            continue

    email = None
    show_island_page(island_name)

    while True:
        action_choice = input("Enter your action (y/n/w/l/s/d/t/!/r/a/ss/u/b): ").lower()

        if action_choice == 'y':
            while True:
                email_input = input("Please enter your email: ")
                if "@" in email_input:
                    email = email_input
                    break
                else:
                    print("Invalid email address. Please enter a valid email with '@'.")
            show_island_page(island_name, email)
        elif action_choice == 'n':
            show_island_page(island_name)
        elif action_choice == 'w':
            show_weather_page(island_name)
        elif action_choice == 'l':
            print(f"Showing {action_choice} information for {island_name}.")
            show_island_page(island_name, email)
        elif action_choice == 's':
            alerts = generate_safety_alerts()
            show_safety_page(island_name, alerts)
        elif action_choice in ['t', '!', 'r']:
            alerts = generate_safety_alerts()
            show_safety_page(island_name, alerts, action_choice)
        elif action_choice == 'a':
            alerts = generate_safety_alerts()
            arrow_mode(alerts, island_name)
        elif action_choice == 'ss':
            print("Safety information saved to file (simulated).")
        elif action_choice == 'u':
            print("Undo the most recent save (simulated).")
        elif action_choice == 'd':
            confirm_deletion()
            confirm_choice = input("Enter your choice (y/n): ").lower()
            if confirm_choice == 'y':
                email = None
                print("Email has been deleted.")
            show_island_page(island_name, email)
        elif action_choice == 'b':
            show_island_page(island_name, email)
        else:
            print("Invalid action. Please select a valid option.")
            continue

# Run the main function
main()

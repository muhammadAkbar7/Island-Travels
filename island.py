import requests
from datetime import datetime

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

def show_city_selection(island_name):
    cities = {
        "Maui": ["Kahului", "Lahaina", "Hana"],
        "Oahu": ["Honolulu", "Kailua", "Waianae"]
    }

    if island_name not in cities:
        print("Invalid island selection.")
        return None

    print("-" * 52)
    print(f"| Select a City on {island_name:<34}|")
    for index, city in enumerate(cities[island_name], start=1):
        print(f"| {index}) {city:<46}|")
    print("-" * 52)

    while True:
        city_choice = input(f"Enter the number of your chosen city (1-{len(cities[island_name])}): ")
        if city_choice.isdigit() and 1 <= int(city_choice) <= len(cities[island_name]):
            return cities[island_name][int(city_choice) - 1]
        else:
            print("Invalid choice. Please select a valid city number.")

def show_island_page(island_name, city_name, email=None):
    print("-" * 52)
    print("|{:^50}|".format(f"Main Page: {island_name} - {city_name}"))
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
    print("|{:>10} {:<38}|".format("p)", "Park Alerts"))
    print("|{:>10} {:<38}|".format("s)", "Safety"))
    print("|{:>10} {:<38}|".format("c)", "Currency Conversion"))
    print("|{:>10} {:<38}|".format("es)", "Emergency Services"))
    print("|" + " " * 50 + "|")
    print("|{:^50}|".format("Deletion:"))
    print("|{:>10} {:<38}|".format("d)", "Delete current email"))
    print("|" + " " * 50 + "|")
    print("|{:^50}|".format("(Type the indicated letter and"))
    print("|{:^50}|".format("press Enter to proceed)"))
    print("-" * 52)

def show_weather_page(city_name, date_range=None):
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

                # Make a request to your Flask server
                response = requests.get(f"http://127.0.0.1:5000/weather?location={city_name}&days={(end_date - start_date).days + 1}")
                
                if response.status_code == 200:
                    weather_data = response.json()
                    current_weather = weather_data['current_weather']
                    forecast = weather_data['forecast']

                    print(f"| Current Weather for {city_name:<35}|")
                    print(f"| {current_weather['date']} {current_weather['time']}: {current_weather['weather_description'].capitalize()}, {current_weather['temperature']}°F |")
                    print("-" * 52)
                    print(f"| Weather forecast from {start_date.strftime('%b %d')} – {end_date.strftime('%b %d')}: |")
                    for date, details in forecast.items():
                        print(f"| {details['date']} ({date}): {details['weather_description'].capitalize()}, {details['temperature']}°F |")
                else:
                    print(f"| Error: Failed to fetch weather data ({response.status_code}) |")
            except ValueError as ve:
                print(f"| Error: {str(ve):<44}|")
                print("| Invalid date range format.                    |")
            except requests.exceptions.RequestException as e:
                print(f"| Error: Failed to connect to server ({str(e)}) |")
        else:
            print(f"| Current weather for today: [No Date Range Provided] |")

        print("|" + " " * 50 + "|")
        print("| Date Range for Vacation?                     |")
        print("|{:>10} {:<38}|".format("y)", "enter date"))
        print("|{:>10} {:<38}|".format("n)", "close prompt"))
        print("|" + " " * 50 + "|")
        print("|{:^50}|".format("Actions:"))
        print("| local navigation:                            |")
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

def show_park_alerts():
    try:
        response = requests.get(f"http://127.0.0.1:5001/park-alerts")
        if response.status_code == 200:
            data = response.json()
            print("-" * 52)
            print(f"| Alerts for {data['park']}:")
            if data['alerts']:
                for alert in data['alerts']:
                    print(f"| Title: {alert['title']}")
                    print(f"| Description: {alert['description']}")
                    print(f"| Category: {alert['category']}")
                    print(f"| More info: {alert['url']}")
                    print("-" * 52)
            else:
                print("| No current alerts for this park.")
                print("-" * 52)
        else:
            print(f"| Error: Failed to fetch park alerts ({response.status_code})")
            print("-" * 52)
    except requests.exceptions.RequestException as e:
        print(f"| Error: Failed to connect to server ({str(e)})")
        print("-" * 52)

def show_currency_conversion():
    print("-" * 52)
    print("|{:^50}|".format("Currency Conversion"))
    print("|" + " " * 50 + "|")
    
    from_currency = input("| Enter the currency to convert from (e.g., USD): ").upper()
    to_currency = input("| Enter the currency to convert to (e.g., EUR): ").upper()
    
    while True:
        try:
            amount = float(input("| Enter the amount to convert: "))
            break
        except ValueError:
            print("| Invalid amount. Please enter a numeric value.")

    try:
        response = requests.get(f"http://127.0.0.1:5005/convert?from={from_currency}&to={to_currency}&amount={amount}")
        if response.status_code == 200:
            data = response.json()
            print("-" * 52)
            print(f"| {amount} {from_currency} is equal to {data['converted_amount']} {to_currency}")
            print(f"| Conversion Rate: 1 {from_currency} = {data['rate']} {to_currency}")
            print("-" * 52)
        else:
            print(f"| Error: Failed to convert currency ({response.status_code})")
            print("-" * 52)
    except requests.exceptions.RequestException as e:
        print(f"| Error: Failed to connect to server ({str(e)})")
        print("-" * 52)

def show_emergency_services():
    print("-" * 52)
    print("|{:^50}|".format("Emergency Services in Lahaina"))
    print("|" + " " * 50 + "|")
    
    service_type = input("| Enter the type of service (e.g., hospital, police): ").lower()

    try:
        response = requests.get(f"http://127.0.0.1:5007/emergency-services?type={service_type}")
        if response.status_code == 200:
            services = response.json()
            print("-" * 52)
            for service in services:
                print(f"| Name: {service['name']}")
                print(f"| Address: {service['address']}")
                print(f"| Rating: {service['rating']}")
                print(f"| Open Now: {service['open_now']}")
                print("-" * 52)
        else:
            print(f"| Error: Failed to retrieve services ({response.status_code})")
            print("-" * 52)
    except requests.exceptions.RequestException as e:
        print(f"| Error: Failed to connect to server ({str(e)})")
        print("-" * 52)

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

def main():
    while True:
        show_welcome_screen()
        choice = input("Enter your choice (a/b): ").lower()

        if choice == 'a':
            island_name = "Maui"
            break
        elif choice == 'b':
            print("Oahu is not yet supported in this program.")
            continue
        else:
            print("Invalid choice. Please select either 'a' for Maui or 'b' for Oahu.")
            continue

    city_name = show_city_selection(island_name)
    email = None
    show_island_page(island_name, city_name)

    while True:
        action_choice = input("Enter your action (y/n/w/p/c/es/s/d/ss/u/b): ").lower()

        if action_choice == 'y':
            while True:
                email_input = input("Please enter your email: ")
                if "@" in email_input:
                    email = email_input
                    break
                else:
                    print("Invalid email address. Please enter a valid email with '@'.")
            show_island_page(island_name, city_name, email)
        elif action_choice == 'n':
            show_island_page(island_name, city_name)
        elif action_choice == 'w':
            show_weather_page(city_name)
        elif action_choice == 'p':
            show_park_alerts()
        elif action_choice == 'c':
            show_currency_conversion()
        elif action_choice == 'es':
            show_emergency_services()
        elif action_choice == 's':
            alerts = generate_safety_alerts()
            show_safety_page(island_name, alerts)
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
            show_island_page(island_name, city_name, email)
        elif action_choice == 'b':
            show_island_page(island_name, city_name, email)
        else:
            print("Invalid action. Please select a valid option.")
            continue

# Run the main function
main()

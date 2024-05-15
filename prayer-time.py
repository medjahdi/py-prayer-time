import requests
import json

def get_prayer_times(location):

    base_url = "http://muslimsalat.com/"
    try:
        response = requests.get(f"{base_url}{location}.json")
        response.raise_for_status()  # Raise exception for bad responses (4xx, 5xx)
        data = response.json()

        # Error handling for missing location data
        if not data.get('items'):
            raise ValueError(f"No prayer data found for {location}.")

        prayer_info = data['items'][0]
        date = prayer_info['date_for']

        print(f"\nPrayer Times for {location} | {date} |")
        print("-" * 40)
        print(f"Fajr:      {prayer_info['fajr']}")
        print(f"Sunrise:   {prayer_info['shurooq']}")
        print(f"Dhuhr:     {prayer_info['dhuhr']}")
        print(f"Asr:       {prayer_info['asr']}")
        print(f"Maghrib:   {prayer_info['maghrib']}")
        print(f"Isha:      {prayer_info['isha']}")
        print("-" * 40)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except ValueError as e:
        print(e)
    except KeyError as e:
        print(f"Missing data in response: {e}")

while True:
    location = input("Enter city name (or 'quit' to exit): ")
    if location.lower() == 'quit':
        break
    
    if not location.isalpha():
        print("Invalid input. Please enter letters only.")
        continue

    get_prayer_times(location)

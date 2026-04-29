import requests
import os
from dotenv import load_dotenv


# load the API keys from the .env file
load_dotenv()

MAPBOX_API_KEY = os.getenv('MAPBOX_API_KEY')
MBTA_API_KEY = os.getenv('MBTA_API_KEY')

# function to get the coordinates of a place using the Mapbox Geocoding API
def get_coordinates(place_name):
    place_name = place_name.replace(" ", "%20")

    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{place_name}.json?access_token={MAPBOX_API_KEY}"

    response = requests.get(url)
    data = response.json()

    if data['features']:
        coordinates = data['features'][0]['center']
        longitude = coordinates[0]
        latitude = coordinates[1]
        return latitude, longitude
    else:
        return None

# function to get the nearest MBTA station using the MBTA API
def get_nearest_station(latitude, longitude):
    url = f"https://api-v3.mbta.com/stops?filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance&api_key={MBTA_API_KEY}"

    response = requests.get(url)
    data = response.json()

    if data['data']:
        stop = data['data'][0]
        nearest_station = stop['attributes']['name']
        wheelchair_accessible = stop['attributes']['wheelchair_boarding']
        stop_latitude = stop['attributes']['latitude']
        stop_longitude = stop['attributes']['longitude']

        return nearest_station, wheelchair_accessible, stop_latitude, stop_longitude
    else:
        return None

# simple function to show if the stop is wheelchair accessible, inaccessible, or if there is no information available
def accessibility(s):
    if s == 1:
        return "Accessible"
    elif s == 2:
        return "Inaccessible"
    elif s == 0:
        return "No information"
    else:
        return "Unknown"

# main function to find the nearest MBTA stop and its accessibility status for a given place name
def find_stop_near(place_name):
    coordinates = get_coordinates(place_name)

    if coordinates is None:
        return None

    latitude, longitude = coordinates
    stop_info = get_nearest_station(latitude, longitude)

    if stop_info is None:
        return None

    stop_name, wheelchair_accessible, stop_latitude, stop_longitude = stop_info

    return stop_name, accessibility(wheelchair_accessible), latitude, longitude, stop_latitude, stop_longitude


# main function to run the program in terminal
def main():
    place_name = input("Enter a place name or address: ")

    result = find_stop_near(place_name)

    if result is None:
        print("Could not find a nearby MBTA stop.")
    else:
        stop_name, wheelchair_status = result
        print("Nearest stop:", stop_name)
        print("Wheelchair accessible:", wheelchair_status)


if __name__ == "__main__":
    main()
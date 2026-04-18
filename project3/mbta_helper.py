import requests
import os
from dotenv import load_dotenv

load_dotenv()

MAPBOX_API_KEY = os.getenv('MAPBOX_API_KEY')
MBTA_API_KEY = os.getenv('MBTA_API_KEY')


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


def get_nearest_station(latitude, longitude):
    url = f"https://api-v3.mbta.com/stops?filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance&api_key={MBTA_API_KEY}"

    response = requests.get(url)
    data = response.json()

    if data['data']:
        nearest_station = data['data'][0]['attributes']['name']
        wheelchair_accessible = data['data'][0]['attributes']['wheelchair_boarding']
        return nearest_station, wheelchair_accessible
    else:
        return None


def accessibility(s):
    if s == 1:
        return "Accessible"
    elif s == 2:
        return "Inaccessible"
    elif s == 0:
        return "No information"
    else:
        return "Unknown"


def find_stop_near(place_name):
    coordinates = get_coordinates(place_name)

    if coordinates is None:
        return None

    latitude, longitude = coordinates
    stop_info = get_nearest_station(latitude, longitude)

    if stop_info is None:
        return None

    stop_name, wheelchair_accessible = stop_info
    return stop_name, accessibility(wheelchair_accessible)


def main():
    place_name = input("Enter a place name or address: ")

    result = find_stop_near(place_name)

    if result is None:
        print("Could not find a nearby MBTA stop.")
    else:
        stop_name, wheelchair_status = result
        print("Nearest stop:", stop_name)
        print("Wheelchair accessible:", wheelchair_status)


main()
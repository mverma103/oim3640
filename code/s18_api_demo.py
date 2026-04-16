import requests
import os
from dotenv import load_dotenv

"""
# response = requests.get("https://oim.108122.xyz/words/random")

response = requests.get(
    "https://oim.108122.xyz/mass",
    headers={"X-Token": "manavmanav"}
             )
data = response.json()

print(len(data))
print(data.keys())
print(type(data['data']))


print(data['name'])
print(data['governor'])

towns = data['data']
print(type(towns))

print(len(towns))

#for town in data['data'][:5]:
    #print(f"{town['name']}: pop {town['population']:,}")

requests.post('https://oim.108122.xyz/message',
              json={"message": "Hello from Manav!"},
              headers={"X-Token": "manavmanav"})"""


"""
url = 'https://api.open-notify.org/astros.json'
data = requests.get(url).json()
print(f"{data['number']} people are currently in space:")
for p in data['people']:
    print(f"{p['name']} on {p['craft']}")"""




load_dotenv()
API_KEY = os.getenv('OPENWEATHER_API_KEY')

url = (f'https://api.openweathermap.org/data/2.5/weather?q=Boston&appid={API_KEY}&units=imperial')

print(url)
data = requests.get(url).json()

print(f"Boston: {data['main']['temp']} degrees F")


# doing it again for wellesley
url2 = (f'https://api.openweathermap.org/data/2.5/weather?q=Wellesley&appid={API_KEY}&units=imperial')

data2 = requests.get(url2).json()
print(f"Wellesley: {data2['main']['temp']} degrees F")
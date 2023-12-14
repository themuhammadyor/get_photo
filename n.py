import requests
from pprint import pprint

url = 'https://randomuser.me/api/'
data = requests.get(url).json()
pprint(data)
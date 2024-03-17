import requests
import json
from config import url


def get_rates():
    response = requests.get(url)
    if response.status_code == 200:
        json_object = json.loads(response)

def archive(timestamp, rates):
    with open(timestamp.json , 'w') as json_file:


if __name__ == "__main__":


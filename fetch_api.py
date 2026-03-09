import requests

def get_atm_data():

    url = "https://api.example.com/atm_feed"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching ATM data")
        return None

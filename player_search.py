import requests 
from team_names import TEAM_NAMES

def load_players():

    url = "http://api.sleeper.app/v1/players/nfl"
    response = requests.get(url, timeout=30)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()
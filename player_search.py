import requests 
from team_names import TEAM_NAMES

def load_players():

    url = "http://api.sleeper.app/v1/players/nfl"
    response = requests.get(url, timeout=30)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

def find_players(all_players, search_text):
    matches = []
    for player_id, player_info in all_players.items():
        full_name = f"{info.get('first_name')} {info.get('last_name')}"
        if search_text.lower() in full_name.lower() and info.get("active"):
            
import requests

from team_names import TEAM_NAMES

url = "http://api.sleeper.app/v1/players/nfl"
response = requests.get(url)
all_players = response.json()

search_name = "Lamar Jackson"

for player_id, info in all_players.items():
    full_name = f"{info.get('first_name')} {info.get('last_name')}"
    if full_name == search_name:
        print(f"name: {full_name}")
        team_code = info.get("team")
        print(f"team: {TEAM_NAMES.get(team_code, 'Unknown Team')}")
        print(f"position: {info.get('position')}")
        print(f"status: {info.get('status')}")
        print(f"Injuries status: {info.get('injury_status')}")
        break


# Hello WOrld

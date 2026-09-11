import requests

team_names = {
    "ARI": "Arizona Cardinals", "ATL": "Atlanta Falcons", "BAL": "Baltimore Ravens",
    "BUF": "Buffalo Bills", "CAR": "Carolina Panthers", "CHI": "Chicago Bears",
    "CIN": "Cincinnati Bengals", "CLE": "Cleveland Browns", "DAL": "Dallas Cowboys",
    "DEN": "Denver Broncos", "DET": "Detroit Lions", "GB": "Green Bay Packers",
    "HOU": "Houston Texans", "IND": "Indianapolis Colts", "JAX": "Jacksonville Jaguars",
    "KC": "Kansas City Chiefs", "LV": "Las Vegas Raiders", "LAC": "Los Angeles Chargers",
    "LAR": "Los Angeles Rams", "MIA": "Miami Dolphins", "MIN": "Minnesota Vikings",
    "NE": "New England Patriots", "NO": "New Orleans Saints", "NYG": "New York Giants",
    "NYJ": "New York Jets", "PHI": "Philadelphia Eagles", "PIT": "Pittsburgh Steelers",
    "SF": "San Francisco 49ers", "SEA": "Seattle Seahawks", "TB": "Tampa Bay Buccaneers",
    "TEN": "Tennessee Titans", "WAS": "Washington Commanders"
}

url = "http://api.sleeper.app/v1/players/nfl"
response = requests.get(url)
all_players = response.json()

search_name = "Lamar Jackson"

for player_id, info in all_players.items():
    full_name = f"{info.get('first_name')} {info.get('last_name')}"
    if full_name == search_name:
        print(f"name: {full_name}")
        team_code = info.get('team')
        print(f"team: {team_names.get(team_code, 'Unknown Team')}")
        print(f"position: {info.get('position')}")
        print(f"status: {info.get('status')}")
        print(f"Injuries status: {info.get('injury_status')}")
        break


# Hello WOrld
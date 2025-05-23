import requests

base_url = "https://rickandmortyapi.com/api"

def get_episode_name(ep_name):
    url = f"{base_url}/episode/?name={ep_name}"
    responde = requests.get(url)

    if responde.status_code == 200:
        data = responde.json()

        character = data['results'][0]
        print(f"Data: {character['air_date']}")
        print(f"Número: {character['episode']}")
    else:
        print("Failed to retrieve data. Error: ", responde.status_code)
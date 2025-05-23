import requests

base_url = "https://rickandmortyapi.com/api"

def get_episode_id(ep_id):
    url = f"{base_url}/episode/{ep_id}"
    responde = requests.get(url)

    if responde.status_code == 200:
        data = responde.json()

        print(f"Nome: {data['name']}")
        print(f"Data: {data['air_date']}")
        print(f"Número: {data['episode']}")
    else:
        print("Failed to retrieve data. Error: ", responde.status_code)
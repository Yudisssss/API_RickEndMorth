import requests

base_url = "https://rickandmortyapi.com/api"

def get_character_by_name(name):
    url = f"{base_url}/character/?name={name}"
    responde = requests.get(url)

    if responde.status_code == 200:
        data = responde.json()

        character = data['results'][0]
        print(f"Status: {character['status']}")
        print(f"Species: {character['species']}")
        print(f"Type: {character['type'] if character['type'] else 'Unknown'}")
    else:
        print("Failed to retrieve data. Error: ", responde.status_code)
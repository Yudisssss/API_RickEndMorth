import requests

base_url = "https://rickandmortyapi.com/api"

def get_locale_name(locale_name):
    url = f"{base_url}/location/?name={locale_name}"
    responde = requests.get(url)

    if responde.status_code == 200:
        data = responde.json()

        character = data['results'][0]
        print(f"Dimension: {character['dimension']}")
        print(f"Type: {character['type'] if character['type'] else 'Unknown'}")
    else:
        print("Failed to retrieve data. Error: ", responde.status_code)
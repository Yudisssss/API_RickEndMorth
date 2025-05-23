import requests 

base_url = "https://rickandmortyapi.com/api"

def get_locale_id(loc_id):
    url = f"{base_url}/location/{loc_id}"
    response = requests.get(url)

    if response.status_code == 200:
        character_data = response.json()
        print(f"Name: {character_data['name']}")
        print(f"Type: {character_data['type']}") 
        print(f"Dimension: {character_data['dimension']}")
        if 'type' == "":
            print("Type: Unknown")
    else:
        print("Failed to retireve data. Error: ", response.status_code)
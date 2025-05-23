import requests 

base_url = "https://rickandmortyapi.com/api"

def get_character_by_id(id):
    url = f"{base_url}/character/{id}"
    response = requests.get(url)

    if response.status_code == 200:
        character_data = response.json()
        print(f"Name: {character_data['name']}")
        print(f"Status: {character_data['status']}")
        print(f"Species: {character_data['species']}")
        print(f"Type: {character_data['type']}") 
        if 'type' == "":
            print("Type: Unknown")
    else:
        print("Failed to retireve data. Error: ", response.status_code)
        

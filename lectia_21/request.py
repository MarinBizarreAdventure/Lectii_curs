import requests



base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print("failed to retrieve data")


pokemon_info = get_pokemon_info("pikachu")
if pokemon_info:
    print("Pokemon stats:")
    print(f"name: {pokemon_info["name"]}")
    print(f"id: {pokemon_info["id"]}")
    print(f"height: {pokemon_info["height"]}")
    


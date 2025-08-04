import requests
import json

BASE_URL = "https://pokeapi.co/api/v2"


def demo_basic_get_request():
    response= requests.get(f"{BASE_URL}/pokemon/pikachu")
    if response.status_code == 200:
        pokemon_data = response.json()
        print(f"success got data for {pokemon_data["name"]}")
        print(f"Height: {pokemon_data["height"]}")
        print(f"Weight: {pokemon_data['weight']}")
    else:
        print(f"Error: {response.status_code}")


def demo_request_with_params():
    params = {
        'limit': 5,
        'offset': 20
    }

    response = requests.get(f"{BASE_URL}/pokemon", params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"got {len(data['results'])} pokemon(limit: {params['limit']}, offset: {params['offset']})")
        for pokemon in data["results"]:
            print(f"- {pokemon['name']}: {pokemon["url"]}")
        
    print(f"final url: {response.url}")
    print('-'*50)


def demo_headers_and_error_handling():
    headers = {
        "User-Agent":"Pokemon-Tutorial-App/1.0",
        'Accept': "application/json",
        "Accept-Language": "en-US"
    }
    
    response = requests.get(f"{BASE_URL}/pokemon/nonexistent",headers=headers)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 404:
        print("pokemon not found")

    try:
        response = requests.get(f"{BASE_URL}/pokemon/charizard")
        response.raise_for_status()
        pokemon_data = response.json()
        print(f"successfully got {pokemon_data["name"]}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

    print("-"*50)

def demo_session_usage():
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Pokemon-Session-App/1.0'
    })
    pokemon_names = ['bulbasaur', 'charmander', 'squirtle']

    for name in pokemon_names:
        try:
            response = requests.get(f"{BASE_URL}/pokemon/{name}")
            response.raise_for_status()
            pokemon_data = response.json()
            types = [t['type']['name'] for t in pokemon_data['types']]
            print(f"{pokemon_data['name'].title()}: {', '.join(types)} type(s)")
        except requests.exceptions.RequestException as e:
            print(f"failed to get {name}: {e}")

    session.close()
    print("-"*50)


def demo_advanced_features():
    response = requests.get(f"{BASE_URL}/pokemon/ditto")

    if response.status_code == 200:
        pokemon_data = response.json()
        name = pokemon_data["name"]
        abilities = [ability['ability']['name'] for ability in pokemon_data["abilities"]]
        stats = {stat['stat']['name']: stat["base_stat"] for stat in pokemon_data['stats']}

        for stat_name, stat_value in stats.items():
            print(f"    {stat_name}: {stat_value}")


def demo_nested_api_calls():
    response = requests.get(f"{BASE_URL}/pokemon/mewtwo")

    if response.status_code == 200:
        pokemon_data = response.json()
        species_url = pokemon_data["species"]['url']
        species_response = requests.get(species_url)
        if species_response.status_code == 200:
            species_data = species_response.json()
            flavor_texts = species_data.get("flavor_text_entries", [])
            english_flavor = next(
                (entry['flavor_text'] for entry in flavor_texts
                 if entry['language']['name'] == 'en'), 'no description available'


            )
        print(f"descriptions: {english_flavor.replace(chr(12), ' ')}")
        print()



def demo_error_scenarios():
    """
    Demonstrates various error scenarios and how to handle them
    """
    print("=== ERROR HANDLING SCENARIOS ===")
    
    # 1. Network timeout
    print("1. Testing timeout...")
    try:
        response = requests.get(f"{BASE_URL}/pokemon/pikachu", timeout=0.001)  # Very short timeout
    except requests.exceptions.Timeout:
        print("   ⏰ Timeout occurred (expected)")
    except requests.exceptions.RequestException as e:
        print(f"   ❌ Other error: {e}")
    
    # 2. Invalid URL
    print("2. Testing invalid URL...")
    try:
        response = requests.get("https://invalid-url-that-doesnt-exist.com")
    except requests.exceptions.ConnectionError:
        print("   🔌 Connection error (expected)")
    except requests.exceptions.RequestException as e:
        print(f"   ❌ Other error: {e}")
    
    # 3. HTTP error status
    print("3. Testing HTTP error status...")
    response = requests.get(f"{BASE_URL}/pokemon/nonexistent-pokemon")
    print(f"   Status: {response.status_code} (404 Not Found)")
    
    # Using raise_for_status()
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"   ❌ HTTP Error caught: {e}")
    
    print("-" * 50)

def demo_response_formats():
    """
    Demonstrates different ways to handle response data
    """
    print("=== RESPONSE FORMATS ===")
    
    response = requests.get(f"{BASE_URL}/pokemon/eevee")
    
    if response.status_code == 200:
        # Different ways to access response data
        print("📄 Response data formats:")
        
        # 1. JSON (most common for APIs)
        json_data = response.json()
        print(f"  JSON: {json_data['name']} (type: {type(json_data)})")
        
        # 2. Raw text
        text_data = response.text
        print(f"  Text: First 100 chars: {text_data[:100]}...")
        
        # 3. Raw bytes
        bytes_data = response.content
        print(f"  Bytes: {len(bytes_data)} bytes")
        
        # 4. Check if JSON is valid
        try:
            json.loads(response.text)
            print("  ✅ Valid JSON response")
        except json.JSONDecodeError:
            print("  ❌ Invalid JSON response")
    
    print("-" * 50)


def main():
    demo_basic_get_request()
    demo_request_with_params()
    demo_headers_and_error_handling()
    demo_session_usage()
    demo_advanced_features()
    # demo_nested_api_calls()
    # demo_error_scenarios()
    # demo_response_formats()

    pass



if __name__ == "__main__":
    main()
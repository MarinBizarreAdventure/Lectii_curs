import requests
import json
from typing import Dict, List, Optional

# Base URL for PokéAPI
BASE_URL = "https://pokeapi.co/api/v2"

def demo_basic_get_request():
    """
    Demonstrates basic GET request to fetch a single Pokémon
    """
    print("=== BASIC GET REQUEST ===")
    
    # Simple GET request
    response = requests.get(f"{BASE_URL}/pokemon/pikachu")
    
    # Check if request was successful
    if response.status_code == 200:
        pokemon_data = response.json()
        print(f"✅ Success! Got data for {pokemon_data['name']}")
        print(f"Height: {pokemon_data['height']}")
        print(f"Weight: {pokemon_data['weight']}")
        print(f"Base Experience: {pokemon_data['base_experience']}")
    else:
        print(f"❌ Error: {response.status_code}")
    
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Headers: {dict(response.headers)}")
    print("-" * 50)

def demo_request_with_params():
    """
    Demonstrates GET request with query parameters
    """
    print("=== GET REQUEST WITH PARAMETERS ===")
    
    # Using query parameters for pagination
    params = {
        'limit': 5,
        'offset': 20
    }
    
    response = requests.get(f"{BASE_URL}/pokemon", params=params)
    
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Got {len(data['results'])} Pokémon (limit: {params['limit']}, offset: {params['offset']})")
        for pokemon in data['results']:
            print(f"  - {pokemon['name']}: {pokemon['url']}")
    
    # Show the actual URL that was constructed
    print(f"Final URL: {response.url}")
    print("-" * 50)

def demo_headers_and_error_handling():
    """
    Demonstrates custom headers and proper error handling
    """
    print("=== HEADERS AND ERROR HANDLING ===")
    
    # Custom headers
    headers = {
        'User-Agent': 'Pokemon-Tutorial-App/1.0',
        'Accept': 'application/json',
        'Accept-Language': 'en-US'
    }
    
    # Try to get a non-existent Pokémon
    response = requests.get(f"{BASE_URL}/pokemon/nonexistent", headers=headers)
    
    print(f"Request with custom headers:")
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 404:
        print("❌ Pokémon not found (expected)")
    
    # Proper error handling with try-except
    try:
        response = requests.get(f"{BASE_URL}/pokemon/charizard", 
                              headers=headers, 
                              timeout=10)  # 10 second timeout
        response.raise_for_status()  # Raises an HTTPError for bad responses
        
        pokemon_data = response.json()
        print(f"✅ Successfully got {pokemon_data['name']}")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")
    
    print("-" * 50)

def demo_session_usage():
    """
    Demonstrates using sessions for multiple requests
    """
    print("=== USING SESSIONS ===")
    
    # Create a session to reuse connections and settings
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Pokemon-Session-App/1.0'
    })
    
    # List of Pokémon to fetch
    pokemon_names = ['bulbasaur', 'charmander', 'squirtle']
    
    for name in pokemon_names:
        try:
            response = session.get(f"{BASE_URL}/pokemon/{name}")
            response.raise_for_status()
            
            pokemon_data = response.json()
            types = [t['type']['name'] for t in pokemon_data['types']]
            print(f"✅ {pokemon_data['name'].title()}: {', '.join(types)} type(s)")
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Failed to get {name}: {e}")
    
    # Don't forget to close the session
    session.close()
    print("-" * 50)

def demo_advanced_features():
    """
    Demonstrates advanced features like response parsing and data extraction
    """
    print("=== ADVANCED FEATURES ===")
    
    # Get detailed information about a Pokémon
    response = requests.get(f"{BASE_URL}/pokemon/ditto")
    
    if response.status_code == 200:
        pokemon_data = response.json()
        
        # Extract specific information
        name = pokemon_data['name']
        abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]
        stats = {stat['stat']['name']: stat['base_stat'] for stat in pokemon_data['stats']}
        
        print(f"🔍 Detailed info for {name.title()}:")
        print(f"  Abilities: {', '.join(abilities)}")
        print(f"  Stats:")
        for stat_name, stat_value in stats.items():
            print(f"    {stat_name}: {stat_value}")
    
    # Demonstrate response metadata
    print(f"\n📊 Response metadata:")
    print(f"  Response time: {response.elapsed.total_seconds():.2f} seconds")
    print(f"  Content length: {len(response.content)} bytes")
    print(f"  Encoding: {response.encoding}")
    print("-" * 50)

def demo_nested_api_calls():
    """
    Demonstrates making nested API calls based on response data
    """
    print("=== NESTED API CALLS ===")
    
    # First, get a random Pokémon
    response = requests.get(f"{BASE_URL}/pokemon/mewtwo")
    
    if response.status_code == 200:
        pokemon_data = response.json()
        print(f"🎯 Analyzing {pokemon_data['name'].title()}...")
        
        # Get the species information (nested call)
        species_url = pokemon_data['species']['url']
        species_response = requests.get(species_url)
        
        if species_response.status_code == 200:
            species_data = species_response.json()
            
            # Find English flavor text
            flavor_texts = species_data.get('flavor_text_entries', [])
            english_flavor = next(
                (entry['flavor_text'] for entry in flavor_texts 
                 if entry['language']['name'] == 'en'), 
                'No description available'
            )
            
            print(f"📖 Description: {english_flavor.replace(chr(12), ' ')}")
            print(f"🏠 Habitat: {species_data.get('habitat', {}).get('name', 'Unknown')}")
            print(f"🎨 Color: {species_data.get('color', {}).get('name', 'Unknown')}")
    
    print("-" * 50)

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
    """
    Run all demonstration functions
    """
    print("🚀 Python Requests Library Tutorial with PokéAPI")
    print("=" * 60)
    
    # Run all demonstrations
    demo_basic_get_request()
    demo_request_with_params()
    demo_headers_and_error_handling()
    demo_session_usage()
    demo_advanced_features()
    demo_nested_api_calls()
    demo_error_scenarios()
    demo_response_formats()
    
    print("🎉 Tutorial completed!")
    print("\n💡 Key takeaways:")
    print("- Always check status codes before processing data")
    print("- Use response.json() for JSON APIs")
    print("- Handle exceptions with try-except blocks")
    print("- Use sessions for multiple requests")
    print("- Set appropriate timeouts")
    print("- Use raise_for_status() for automatic error handling")

if __name__ == "__main__":
    main()

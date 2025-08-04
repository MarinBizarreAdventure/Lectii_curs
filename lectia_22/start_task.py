import requests

def get_random_fact():
    """Obține un fapt aleatoriu despre pisici"""
    
    # TODO: Fă un GET request la această adresă:
    url = "https://catfact.ninja/fact"
    
    # TODO: Folosește requests.get() pentru a face request-ul
    response = requests.get(url)
    
    # TODO: Verifică dacă request-ul a fost cu succes (status_code == 200)
    if response.status_code == 200:
        data = response.json()
        return data["fact"]    
    else:
        return f"error {response.status_code}"
    

def get_weather(city):
    """Obține vremea pentru un oraș (fără API key)"""
    
    # TODO: Construiește URL-ul cu parametrii
    url = "https://wttr.in/" + city
    
    # TODO: Adaugă parametrii pentru format JSON
    params = {
        'format': 'j1'  # JSON format
    }
    
    # TODO: Fă request-ul cu parametrii
    response = requests.get(url, params=params)
    
    # TODO: Dacă e OK, returnează temperatura curentă
    if response.status_code == 200:
        data = response.json()
        temp = data['current_condition'][0]['temp_C']
        return f"{temp}°C"
    
    return "Nu s-a putut obține vremea" + response.status_code

def main():
    """Funcția principală"""
    
    print("🐱 API Test Simplu")
    print("=" * 20)
    
    # TODO: Apelează get_random_fact() și afișează rezultatul
    print("📰 Fapt aleatoriu despre pisici:")
    fact = get_random_fact()
    print(fact)
    
    print("\n" + "=" * 20)
    
    # TODO: Cere utilizatorului să introducă un oraș
    city = input("Introdu numele unui oraș: ")
    
    # TODO: Apelează get_weather(city) și afișează rezultatul
    weather = get_weather(city)
    print(f"🌤️ Vremea în {city}: {weather}")

if __name__ == "__main__":
    main()

# TODO: După ce completezi codul:
# 1. Rulează programul: python simple_homework.py
# 2. Testează cu orașe diferite
# 3. Verifică că requirements.txt conține "requests"
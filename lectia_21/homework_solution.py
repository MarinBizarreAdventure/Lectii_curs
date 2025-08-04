# Soluția Temei pentru Acasă - Lecția 22: PIP, Virtual Environments și API Requests

"""
🎯 SOLUȚIA COMPLETĂ:
Implementare completă a Pokemon Info Client folosind PokéAPI

📋 COMENZI BASH PENTRU SETUP:
```bash
# Creează proiectul
mkdir pokemon_client
cd pokemon_client

# Creează și activează virtual environment
python -m venv .venv

# Windows:
.venv\Scripts\activate

# Linux/Mac:
source .venv/bin/activate

# Instalează dependențe
pip install requests
pip freeze > requirements.txt

# Verifică instalarea
pip list
```

🚀 FUNCȚIONALITĂȚI IMPLEMENTATE:
- ✅ Căutare pokémon după nume
- ✅ Căutare pokémoni după tip
- ✅ Pokémon aleatoriu (BONUS)
- ✅ Formatare frumoasă a informațiilor
- ✅ Gestionarea erorilor
- ✅ Cache simplu (BONUS)
"""

import requests
import json
import random
import os
from typing import Dict, Optional, List
from datetime import datetime

class PokemonClient:
    """Client pentru interacțiunea cu PokéAPI"""
    
    def __init__(self):
        # URL-ul de bază pentru PokéAPI
        self.base_url = "https://pokeapi.co/api/v2"
        
        # Creează o sesiune requests pentru performanță mai bună
        self.session = requests.Session()
        
        # Setează un User-Agent header
        self.session.headers.update({
            'User-Agent': 'PythonPokemonClient/1.0'
        })
        
        # BONUS: Cache simplu
        self.cache_file = "pokemon_cache.json"
        self.cache = self._load_cache()
    
    def _load_cache(self) -> Dict:
        """Încarcă cache-ul din fișier"""
        try:
            if os.path.exists(self.cache_file):
                with open(self.cache_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            print(f"⚠️ Eroare la încărcarea cache-ului: {e}")
        return {}
    
    def _save_cache(self):
        """Salvează cache-ul în fișier"""
        try:
            with open(self.cache_file, 'w', encoding='utf-8') as f:
                json.dump(self.cache, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"⚠️ Eroare la salvarea cache-ului: {e}")
    
    def get_pokemon_info(self, pokemon_name: str) -> Optional[Dict]:
        """
        Obține informații despre un pokémon după nume
        
        Args:
            pokemon_name: Numele pokémonului (ex: "pikachu", "charmander")
            
        Returns:
            Dict cu informații despre pokémon sau None dacă nu există
        """
        pokemon_name = pokemon_name.lower().strip()
        
        # Verifică cache-ul
        if pokemon_name in self.cache:
            print(f"📁 Cache hit pentru {pokemon_name}")
            return self.cache[pokemon_name]
        
        try:
            print(f"🌐 Căutăm {pokemon_name} pe PokéAPI...")
            
            # Fă request-ul
            response = self.session.get(
                f"{self.base_url}/pokemon/{pokemon_name}",
                timeout=10
            )
            
            if response.status_code == 404:
                print(f"❌ Pokémonul '{pokemon_name}' nu a fost găsit!")
                return None
            
            response.raise_for_status()  # Aruncă excepție pentru alte erori
            
            # Procesează răspunsul
            pokemon_data = response.json()
            
            # Extrage informațiile importante
            pokemon_info = {
                'name': pokemon_data['name'].title(),
                'id': pokemon_data['id'],
                'height': pokemon_data['height'] / 10,  # Convertește la metri
                'weight': pokemon_data['weight'] / 10,  # Convertește la kg
                'types': [t['type']['name'] for t in pokemon_data['types']],
                'abilities': [a['ability']['name'] for a in pokemon_data['abilities']],
                'stats': {
                    stat['stat']['name']: stat['base_stat'] 
                    for stat in pokemon_data['stats']
                },
                'sprite': pokemon_data['sprites']['front_default']
            }
            
            # Salvează în cache
            self.cache[pokemon_name] = pokemon_info
            self._save_cache()
            
            return pokemon_info
            
        except requests.exceptions.Timeout:
            print("⏰ Request timeout! Încearcă din nou.")
            return None
        except requests.exceptions.RequestException as e:
            print(f"🌐 Eroare de rețea: {e}")
            return None
        except Exception as e:
            print(f"❌ Eroare neașteptată: {e}")
            return None
    
    def search_pokemon_by_type(self, pokemon_type: str) -> Optional[List[str]]:
        """
        Caută pokémoni după tip
        
        Args:
            pokemon_type: Tipul pokémonului (ex: "fire", "water", "electric")
            
        Returns:
            Listă cu numele pokémonilor de acel tip sau None dacă tipul nu există
        """
        pokemon_type = pokemon_type.lower().strip()
        
        # Verifică cache-ul pentru tipuri
        cache_key = f"type_{pokemon_type}"
        if cache_key in self.cache:
            print(f"📁 Cache hit pentru tipul {pokemon_type}")
            return self.cache[cache_key]
        
        try:
            print(f"🌐 Căutăm pokémoni de tipul {pokemon_type}...")
            
            # Fă request-ul
            response = self.session.get(
                f"{self.base_url}/type/{pokemon_type}",
                timeout=10
            )
            
            if response.status_code == 404:
                print(f"❌ Tipul '{pokemon_type}' nu a fost găsit!")
                return None
            
            response.raise_for_status()
            
            # Procesează răspunsul
            type_data = response.json()
            
            # Extrage numele pokémonilor (primii 20 pentru simplitate)
            pokemon_list = [
                pokemon['pokemon']['name'].title()
                for pokemon in type_data['pokemon'][:20]
            ]
            
            # Salvează în cache
            self.cache[cache_key] = pokemon_list
            self._save_cache()
            
            return pokemon_list
            
        except requests.exceptions.Timeout:
            print("⏰ Request timeout! Încearcă din nou.")
            return None
        except requests.exceptions.RequestException as e:
            print(f"🌐 Eroare de rețea: {e}")
            return None
        except Exception as e:
            print(f"❌ Eroare neașteptată: {e}")
            return None
    
    def get_random_pokemon(self) -> Optional[Dict]:
        """
        BONUS: Obține un pokémon aleatoriu
        
        Returns:
            Dict cu informații despre un pokémon aleatoriu
        """
        # Generează un ID aleatoriu (1-1010 sunt pokémoni valizi)
        random_id = random.randint(1, 1010)
        
        print(f"🎲 Căutăm pokémon aleatoriu cu ID {random_id}...")
        
        # Folosește get_pokemon_info cu ID-ul
        return self.get_pokemon_info(str(random_id))
    
    def get_pokemon_species_info(self, pokemon_name: str) -> Optional[str]:
        """
        BONUS: Obține descrierea pokémonului
        
        Args:
            pokemon_name: Numele pokémonului
            
        Returns:
            Descrierea pokémonului în engleză
        """
        try:
            response = self.session.get(
                f"{self.base_url}/pokemon-species/{pokemon_name.lower()}",
                timeout=10
            )
            
            if response.status_code == 200:
                species_data = response.json()
                
                # Caută descrierea în engleză
                for entry in species_data['flavor_text_entries']:
                    if entry['language']['name'] == 'en':
                        return entry['flavor_text'].replace('\n', ' ').replace('\f', ' ')
                
        except Exception:
            pass
        
        return None

def format_pokemon_info(pokemon_data: Dict) -> str:
    """
    Formatează informațiile despre pokémon pentru afișare
    
    Args:
        pokemon_data: Datele pokémonului de la API
        
    Returns:
        String formatat pentru afișare
    """
    # Emoji-uri pentru tipuri
    type_emojis = {
        'fire': '🔥', 'water': '💧', 'grass': '🌱', 'electric': '⚡',
        'psychic': '🔮', 'ice': '❄️', 'dragon': '🐉', 'dark': '🌙',
        'fairy': '🧚', 'fighting': '👊', 'poison': '☠️', 'ground': '🌍',
        'flying': '🦅', 'bug': '🐛', 'rock': '🪨', 'ghost': '👻',
        'steel': '⚔️', 'normal': '⚪'
    }
    
    # Formatează tipurile cu emoji-uri
    types_with_emojis = [
        f"{type_emojis.get(t, '❓')} {t.title()}"
        for t in pokemon_data['types']
    ]
    
    # Formatează statisticile
    stats_formatted = []
    for stat_name, stat_value in pokemon_data['stats'].items():
        stat_display = stat_name.replace('-', ' ').title()
        stats_formatted.append(f"   {stat_display}: {stat_value}")
    
    # Construiește string-ul final
    info = f"""
🐾 ===== {pokemon_data['name'].upper()} ===== 🐾
📊 ID: #{pokemon_data['id']}
📏 Înălțime: {pokemon_data['height']} metri
⚖️ Greutate: {pokemon_data['weight']} kg
🏷️ Tipuri: {', '.join(types_with_emojis)}
🎯 Abilități: {', '.join(pokemon_data['abilities'])}

📈 Statistici:
{chr(10).join(stats_formatted)}

🖼️ Sprite: {pokemon_data['sprite'] or 'Nu este disponibil'}
"""
    
    return info

def display_pokemon_list(pokemon_list: List[str], pokemon_type: str):
    """
    Afișează lista de pokémoni de un anumit tip
    
    Args:
        pokemon_list: Lista cu numele pokémonilor
        pokemon_type: Tipul pokémonilor
    """
    print(f"\n🔍 Pokémoni de tipul {pokemon_type.title()}:")
    print("=" * 50)
    
    # Afișează în coloane de câte 4
    for i in range(0, len(pokemon_list), 4):
        row = pokemon_list[i:i+4]
        print("   ".join(f"{name:<15}" for name in row))
    
    print(f"\n📊 Total găsite: {len(pokemon_list)} pokémoni")

def main():
    """Funcția principală - interfața utilizatorului"""
    
    print("🐾 Bun venit la Pokemon Info Client!")
    print("=" * 40)
    print("📱 Powered by PokéAPI (https://pokeapi.co/)")
    print("🔄 Cu cache local pentru performanță mai bună")
    
    # Creează instanța clientului
    client = PokemonClient()
    
    while True:
        print("\n📋 Opțiuni disponibile:")
        print("1. 🔍 Caută pokémon după nume")
        print("2. 🏷️ Caută pokémoni după tip")
        print("3. 🎲 Pokémon aleatoriu")
        print("4. 🗑️ Curăță cache-ul")
        print("5. 👋 Ieșire")
        
        choice = input("\nAlege o opțiune (1-5): ").strip()
        
        if choice == '1':
            # Căutare după nume
            pokemon_name = input("Introdu numele pokémonului: ").strip()
            
            if not pokemon_name:
                print("❌ Te rog introdu un nume valid!")
                continue
            
            pokemon_info = client.get_pokemon_info(pokemon_name)
            
            if pokemon_info:
                print(format_pokemon_info(pokemon_info))
                
                # BONUS: Încearcă să obții și descrierea
                description = client.get_pokemon_species_info(pokemon_name)
                if description:
                    print(f"📝 Descriere: {description}")
            else:
                print(f"❌ Nu s-au găsit informații pentru '{pokemon_name}'")
        
        elif choice == '2':
            # Căutare după tip
            pokemon_type = input("Introdu tipul pokémonului (ex: fire, water, electric): ").strip()
            
            if not pokemon_type:
                print("❌ Te rog introdu un tip valid!")
                continue
            
            pokemon_list = client.search_pokemon_by_type(pokemon_type)
            
            if pokemon_list:
                display_pokemon_list(pokemon_list, pokemon_type)
                
                # Opțiune de a căuta detalii despre un pokémon din listă
                detail_choice = input(f"\nVrei să vezi detalii despre un pokémon din listă? (y/n): ").lower()
                if detail_choice == 'y':
                    pokemon_name = input("Introdu numele pokémonului: ").strip()
                    pokemon_info = client.get_pokemon_info(pokemon_name)
                    if pokemon_info:
                        print(format_pokemon_info(pokemon_info))
            else:
                print(f"❌ Nu s-au găsit pokémoni de tipul '{pokemon_type}'")
        
        elif choice == '3':
            # Pokémon aleatoriu
            print("🎲 Căutăm un pokémon aleatoriu...")
            pokemon_info = client.get_random_pokemon()
            
            if pokemon_info:
                print("🎉 Uite ce pokémon interesant am găsit!")
                print(format_pokemon_info(pokemon_info))
                
                # BONUS: Descrierea
                description = client.get_pokemon_species_info(pokemon_info['name'])
                if description:
                    print(f"📝 Descriere: {description}")
            else:
                print("❌ Nu s-a putut obține un pokémon aleatoriu")
        
        elif choice == '4':
            # Curăță cache-ul
            try:
                if os.path.exists(client.cache_file):
                    os.remove(client.cache_file)
                    client.cache = {}
                    print("🗑️ Cache-ul a fost curățat cu succes!")
                else:
                    print("📁 Cache-ul este deja gol!")
            except Exception as e:
                print(f"❌ Eroare la curățarea cache-ului: {e}")
        
        elif choice == '5':
            print("👋 La revedere! Mult noroc cu pokémonii!")
            print("🎮 Sper că ai învățat ceva nou despre API-uri și virtual environments!")
            break
        
        else:
            print("❌ Opțiune invalidă. Te rog alege 1-5.")

if __name__ == "__main__":
    main()

# 🧪 TESTARE SUGERATĂ:
# 1. Testează cu pokémoni populari: pikachu, charmander, bulbasaur, squirtle
# 2. Testează cu pokémoni mai puțin cunoscuți: gengar, alakazam, machamp
# 3. Testează tipurile: electric, fire, water, grass, psychic, ghost
# 4. Testează pokémonul aleatoriu de mai multe ori
# 5. Verifică că cache-ul funcționează (a doua căutare e mai rapidă)

# 📋 REQUIREMENTS.TXT (generat cu pip freeze):
"""
certifi==2023.11.17
charset-normalizer==3.3.2
idna==3.6
requests==2.31.0
urllib3==2.1.0
"""
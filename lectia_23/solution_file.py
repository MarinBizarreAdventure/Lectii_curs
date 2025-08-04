# Soluția temei de casă: Lucrul cu fișiere în Python

"""
SOLUȚII COMPLETE PENTRU TOATE EXERCIȚIILE
"""

# ===============================================
# EXERCIȚIUL 1: Crearea și scrierea într-un fișier
# ===============================================

print("=== EXERCIȚIUL 1: Crearea fișierului ===")

# Deschide fișierul pentru scriere
f = open('info_personal.txt', 'w')

# Scrie informațiile personale
f.write("Ana Popescu\n")  # numele (înlocuiește cu numele tău)
f.write("20\n")           # vârsta (înlocuiește cu vârsta ta)
f.write("Cititul\n")      # hobby-ul (înlocuiește cu hobby-ul tău)

# Închide fișierul
f.close()

print("Fișierul 'info_personal.txt' a fost creat cu succes!")

# ===============================================
# EXERCIȚIUL 2: Citirea unui fișier
# ===============================================

print("\n=== EXERCIȚIUL 2: Citirea fișierului ===")

# Deschide fișierul pentru citire
f = open('info_personal.txt', 'r')

# Citește conținutul
continut = f.read()

# Afișează conținutul
print("Conținutul fișierului:")
print(continut)

# Închide fișierul
f.close()

# ===============================================
# EXERCIȚIUL 3: Utilizarea modulului os
# ===============================================

print("=== EXERCIȚIUL 3: Modulul os ===")

import os

# Afișează directorul curent
print(f"Directorul curent: {os.getcwd()}")

# Afișează lista fișierelor
print(f"Fișierele din directorul curent: {os.listdir()}")

# Verifică dacă fișierul există
if os.path.exists('info_personal.txt'):
    print("Fișierul 'info_personal.txt' există!")
else:
    print("Fișierul 'info_personal.txt' nu există!")

# ===============================================
# EXERCIȚIUL 4: Lucrul cu JSON
# ===============================================

print("\n=== EXERCIȚIUL 4: Lucrul cu JSON ===")

import json

# Creează dicționarul cu informații personale
info_dict = {
    "nume": "Ana Popescu",
    "varsta": 20,
    "hobby": "Cititul",
    "limbaje_programare": ["Python", "JavaScript"]
}

# Salvează dicționarul într-un fișier JSON
with open('info.json', 'w') as f:
    json.dump(info_dict, f, indent=4)

print("Datele au fost salvate în 'info.json'")

# Citește datele din fișierul JSON
with open('info.json', 'r') as f:
    date_citite = json.load(f)

# Afișează datele citite
print("Datele citite din JSON:")
for cheie, valoare in date_citite.items():
    print(f"{cheie}: {valoare}")

# ===============================================
# BONUS: Funcția info_fisier
# ===============================================

print("\n=== BONUS: Funcția info_fisier ===")

def info_fisier(nume_fisier):
    """
    Verifică dacă un fișier există și afișează informații despre el
    """
    if os.path.exists(nume_fisier):
        dimensiune = os.path.getsize(nume_fisier)
        print(f"Fișierul '{nume_fisier}' există!")
        print(f"Dimensiunea: {dimensiune} bytes")
    else:
        print(f"Fișierul '{nume_fisier}' nu există!")

# Testează funcția
info_fisier('info_personal.txt')
info_fisier('fisier_inexistent.txt')

# ===============================================
# EXEMPLE SUPLIMENTARE CU 'with' STATEMENT
# ===============================================

print("\n=== EXEMPLU CU 'with' (RECOMANDAT) ===")

# Metoda recomandată pentru lucrul cu fișiere
# Nu trebuie să închizi manual fișierul

# Scriere cu 'with'
with open('test_with.txt', 'w') as f:
    f.write("Acest fișier a fost creat cu 'with' statement\n")
    f.write("Fișierul se închide automat!\n")

# Citire cu 'with'
with open('test_with.txt', 'r') as f:
    continut = f.read()
    print("Conținutul fișierului 'test_with.txt':")
    print(continut)

print("Toate exercițiile au fost completate cu succes!")
# SOLUȚII START TASK - Fișiere, OS și JSON

import os
import json

print("🚀 START TASK - Soluții Complete\n")

# ===== EXERCIȚIUL 1: Crearea fișierului text =====
print("📝 Exercițiul 1: Crearea fișierului despre_mine.txt")

# Datele mele (înlocuiește cu datele tale!)
nume = "Marin Negai"
varsta = 22
oras = "Chisinau"
hobby1 = "programare"
hobby2 = "citit"

# Creăm și scriem în fișier
with open("despre_mine.txt", "w", encoding="utf-8") as f:
    f.write(f"Nume: {nume}\n")
    f.write(f"Vârsta: {varsta} ani\n")
    f.write(f"Orașul: {oras}\n")
    f.write(f"Hobby 1: {hobby1}\n")
    f.write(f"Hobby 2: {hobby2}\n")

print("✅ Fișierul 'despre_mine.txt' a fost creat cu succes!")
print("-" * 50)

# ===== EXERCIȚIUL 2: Citirea fișierului =====
print("📖 Exercițiul 2: Citirea și afișarea conținutului")

try:
    with open("despre_mine.txt", "r", encoding="utf-8") as f:
        continut = f.read()
    
    print("📄 Conținutul fișierului:")
    print(continut)
except FileNotFoundError:
    print("❌ Fișierul nu a fost găsit!")

print("-" * 50)

# ===== EXERCIȚIUL 3: Folosirea modulului OS =====
print("🗂️ Exercițiul 3: Verificarea cu modulul OS")

nume_fisier = "despre_mine.txt"

# Verificăm dacă fișierul există
if os.path.exists(nume_fisier):
    print(f"✅ Fișierul '{nume_fisier}' există!")
    
    # Obținem dimensiunea fișierului
    dimensiune = os.path.getsize(nume_fisier)
    print(f"📏 Dimensiunea fișierului: {dimensiune} bytes")
else:
    print(f"❌ Fișierul '{nume_fisier}' nu există!")

print("-" * 50)

# ===== EXERCIȚIUL 4: Crearea și salvarea JSON =====
print("📦 Exercițiul 4: Salvarea datelor în JSON")

# Creăm dicționarul cu datele
date_personale = {
    "nume": nume,
    "varsta": varsta,
    "oras": oras,
    "hobby_uri": [hobby1, hobby2]
}

# Salvăm în fișier JSON
with open("date.json", "w", encoding="utf-8") as f:
    json.dump(date_personale, f, indent=4, ensure_ascii=False)

print("✅ Datele au fost salvate în 'date.json'!")
print("-" * 50)

# ===== EXERCIȚIUL 5: Citirea și afișarea JSON =====
print("📊 Exercițiul 5: Încărcarea și afișarea datelor JSON")

try:
    with open("date.json", "r", encoding="utf-8") as f:
        date_incarcate = json.load(f)
    
    print("🎯 Datele încărcate din JSON:")
    print(f"👤 Nume: {date_incarcate['nume']}")
    print(f"🎂 Vârsta: {date_incarcate['varsta']} ani")
    print(f"🏙️ Orașul: {date_incarcate['oras']}")
    print(f"🎨 Hobby-uri: {', '.join(date_incarcate['hobby_uri'])}")
    
except FileNotFoundError:
    print("❌ Fișierul JSON nu a fost găsit!")
except json.JSONDecodeError:
    print("❌ Eroare la citirea fișierului JSON!")

print("\n" + "=" * 50)
print("🎉 START TASK COMPLETAT CU SUCCES!")
print("📁 Fișiere create: despre_mine.txt, date.json")

# ===== BONUS: Comparația între fișiere =====
print("\n🏆 BONUS: Comparația dimensiunilor")

if os.path.exists("despre_mine.txt") and os.path.exists("date.json"):
    dim_txt = os.path.getsize("despre_mine.txt")
    dim_json = os.path.getsize("date.json")
    
    print(f"📄 Fișier TXT: {dim_txt} bytes")
    print(f"📦 Fișier JSON: {dim_json} bytes")
    
    if dim_json > dim_txt:
        print("💡 JSON-ul este mai mare din cauza formatării!")
    else:
        print("💡 TXT-ul este mai mare!")

print("\n🎯 Concepte practicate:")
print("   • Scrierea în fișiere cu 'w' mode")
print("   • Citirea din fișiere cu 'r' mode")
print("   • Modulul os: exists(), getsize()")
print("   • JSON: dump(), load()")
print("   • Gestionarea erorilor cu try/except")
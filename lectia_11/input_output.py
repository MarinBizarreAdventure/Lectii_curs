print("🎯 TIPURI DE FUNCȚII DUPĂ INPUT/OUTPUT")
print("=" * 45)

# 1. Funcție fără parametri, fără return
def saluta():
    """Funcție simplă care doar afișează un mesaj"""
    print("Bună ziua! Bine ați venit!")

# 2. Funcție cu parametri, fără return
def afiseaza_info(nume, varsta):
    """Funcție care primește date dar nu returnează nimic"""
    print(f"Numele: {nume}")
    print(f"Vârsta: {varsta} ani")
                

# 3. Funcție fără parametri, cu return
def obtine_data_curenta():
    """Funcție care returnează o valoare fără să primească parametri"""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d")

# 4. Funcție cu parametri și cu return
def calculeaza_arie_cerc(raza):
    """Funcție completă: primește input și returnează output"""
    import math
    arie = math.pi * raza ** 2
    return arie

# Demonstrații
print("1. Funcție fără parametri, fără return:")
saluta()

print("\n2. Funcție cu parametri, fără return:")
afiseaza_info("Ana", 25)

print("\n3. Funcție fără parametri, cu return:")
data = obtine_data_curenta()
print(f"Data curentă: {data}")

print("\n4. Funcție cu parametri și cu return:")
arie = calculeaza_arie_cerc(5)
print(f"Aria cercului cu raza 5: {arie:.2f}")
print("🔄 TIPURI DE RETURN STATEMENTS")
print("=" * 35)

# Return condiționat
def verifica_paritate(numar):
    """Returnează diferite valori în funcție de condiții"""
    if numar % 2 == 0:
        return "par"
    else:
        return "impar"

# Return multiple în aceeași linie
def calcule_matematice(a, b):
    """Returnează multiple valori ca tuplu"""
    suma = a + b
    diferenta = a - b
    produs = a * b
    return suma, diferenta, produs  # Returnează tuplu

# Return early pentru validare
def impartire_sigura(a, b):
    """Returnează rezultatul împărțirii cu validare"""
    if b == 0:
        return "Eroare: Împărțire la zero!"
    return a / b

# Demonstrații
print("1. Return condiționat:")
print(f"8 este {verifica_paritate(8)}")
print(f"6 este {verifica_paritate(6)}")

print("\n2. Return multiple:")
s, d, p = calcule_matematice(10, 3)
print(f"Suma: {s}, Diferența: {d}, Produsul: {p}")



print("\n4. Funcție fără return explicit:")
def fara_return():
    x = 5 + 5

rezultat_none = fara_return()
print(f"Funcția fără return returnează: {rezultat_none}")
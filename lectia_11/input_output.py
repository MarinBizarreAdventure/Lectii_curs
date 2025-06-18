

# Funcția ca o "cutie neagră" care procesează date
"""
    INPUT (Parametri/Argumente)
           ↓
    ┌─────────────────┐
    │   FUNCȚIA f:    │  ← Procesarea datelor
    │   (logica)      │
    └─────────────────┘
           ↓
    OUTPUT f(x) (Valoarea returnată)
"""

def proceseaza_numere(a, b):
    """
    Primește două numere ca INPUT
    Procesează datele (le adună și le înmulțește cu 2)
    Returnează rezultatul ca OUTPUT
    """
    suma = a + b
    rezultat = suma * 2
    return rezultat

# Demonstrarea fluxului
print("INPUT: a=5, b=3")
output = proceseaza_numere(5, 3)
print(f"OUTPUT: {output}")

print(f"\n🔍 PROCESUL PAS CU PAS:")
print(f"1. INPUT: a=5, b=3")
print(f"2. PROCESARE: suma = 5 + 3 = 8")
print(f"3. PROCESARE: rezultat = 8 * 2 = 16")
print(f"4. OUTPUT: return 16")
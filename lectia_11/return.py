print("🔙 COMPORTAMENTUL RETURN STATEMENT")
print("=" * 40)

def demonstrare_return(nr):
    """Demonstrează că codul după return nu se execută"""
    print(f"Înainte de return: nr = {nr}")
    return nr * 2
    print("Această linie NU se va executa niciodată!")  # Dead code
    nr += 100
    print(f"Nici această linie: nr = {nr}")

# Testare
rezultat = demonstrare_return(5)
print(f"Rezultatul returnat: {rezultat}")

print("\n⚠️ IMPORTANT:")
print("• Codul după 'return' nu se execută NICIODATĂ!")
print("• 'return' oprește execuția funcției imediat")
print("• Funcția poate avea multiple 'return' statements")
print("• Dacă nu specifici 'return', funcția returnează 'None'")
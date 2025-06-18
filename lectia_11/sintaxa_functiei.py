print("🔍 ANATOMIA UNEI FUNCȚII")
print("=" * 30)

# 1. def keyword    2. function name    3. parameters
def     add        (    x,    y    ):
    """
    4. Documentația funcției
    Adună două numere și returnează rezultatul
    """
    print(f'arguments are {x} and {y}')  # 5. function body
    suma = x +y 
    return suma                        # 6. return statement

# 7. Apelarea funcției
rezultat = add(5, 3)
print(f"Rezultatul: {rezultat}")

# Explicații pentru fiecare componentă
print("\n📋 COMPONENTELE FUNCȚIEI:")
print("1. 'def' - cuvântul cheie pentru definirea funcției")
print("2. 'add' - numele funcției (trebuie să fie descriptiv)")
print("3. '(x, y)' - parametrii funcției")
print('4. \"\"\"..."""" - documentația (docstring)')
print("5. Corpul funcției - codul care se execută")
print("6. 'return' - returnează o valoare")
print("7. 'add(5, 3)' - apelarea funcției cu argumente")
# START TASK - Lecția 5.4 Funcții Avansate (Lambda, Decoratori, Closures)
# Timp estimat: 25 minute
# Branch: start-task-lesson-5-4

# Exercițiul 1: Decoratorul simplu
# Creați un decorator care printează "Înainte de funcție" și "După funcție"
def decorator_simplu(func):
    def wrapper():
        print("Înainte de funcție")
        func()
        print("După funcție")
    return wrapper

# Aplicați decoratorul pe această funcție:
@decorator_simplu
def spune_buna():
    print("Bună ziua!")

# Testare:
spune_buna()
# Output așteptat:
# Înainte de funcție
# Bună ziua!
# După funcție


# Exercițiul 2: Lambda cu map
# Folosiți lambda cu map pentru a ridica la pătrat toate numerele din listă
numere = [1, 2, 3, 4, 5]

# CODUL TĂU AICI - folosește map și lambda
# patrate = 
# print(list(patrate))  # [1, 4, 9, 16, 25]


# Exercițiul 3: Decorator care numără apelurile
# Creați un decorator care numără de câte ori a fost apelată o funcție
def numarator_apeluri(func):
    def wrapper(*args, **kwargs):
        # CODUL TĂU AICI:
        # 1. Incrementează un counter (folosiți wrapper.count)
        # 2. Printează "Apelul nr. X pentru funcția 'nume_functie'"
        # 3. Apelează funcția originală
        # 4. Returnează rezultatul funcției
        pass
    
    # Inițializăm counter-ul
    wrapper.count = 0
    return wrapper

# Aplicați decoratorul:
# @numarator_apeluri
def spune_mesaj(mesaj="Salut!"):
    print(f"Mesajul este: {mesaj}")
    return "Mesaj trimis"

# Testare:
# rezultat1 = spune_mesaj("Prima dată")
# rezultat2 = spune_mesaj("A doua oară") 
# rezultat3 = spune_mesaj()
# print(f"Funcția a fost apelată {spune_mesaj.count} ori")


# Exercițiul 4: Closure - Generator de validatori
# Creați o funcție care generează validatori pentru diferite limite minime
def creeaza_validator_minim(minim):
    def validator(valoare):
        # CODUL TĂU AICI - returnează True dacă valoare >= minim
        pass
    return validator

# Testare:
# validator_18 = creeaza_validator_minim(18)
# validator_21 = creeaza_validator_minim(21)
# print(validator_18(20))  # True
# print(validator_18(16))  # False
# print(validator_21(20))  # False


# Exercițiul 5: Funcție cu *args și **kwargs + decorator
# Creați un decorator care printează argumentele primite de o funcție
def afiseaza_argumente(func):
    def wrapper(*args, **kwargs):
        print(f"Argumentele poziționale: {args}")
        print(f"Argumentele cu cuvinte cheie: {kwargs}")
        # CODUL TĂU AICI - apelează funcția originală cu argumentele primite
        pass
    return wrapper

# Aplicați decoratorul:
# @afiseaza_argumente
def functie_flexibila(*args, **kwargs):
    print("Funcția a fost apelată!")
    return "Rezultat"

# Testare:
# functie_flexibila(1, 2, 3, nume="Ana", varsta=25)
# Output așteptat:
# Argumentele poziționale: (1, 2, 3)
# Argumentele cu cuvinte cheie: {'nume': 'Ana', 'varsta': 25}
# Funcția a fost apelată!


# Exercițiul 6: Recursie, faceti un simplu exemplu de recursie, care calculeaza numerele fibonaci

def fibonaci(n):
    pass


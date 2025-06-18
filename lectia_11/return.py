print("🔢 EXERCIȚIUL 1: CALCULATOR AVANSAT")
print("=" * 40)

def adunare(a, b):
    """Adună două numere"""
    return a + b

def scadere(a, b):
    """Scade două numere"""
    return a - b

def inmultire(a, b):
    """Înmulțește două numere"""
    return a * b

def impartire(a, b):
    """Împarte două numere cu validare"""
    if b == 0:
        return "Eroare: Împărțire la zero!"
    return a / b

def putere(a, b):
    """Ridică un număr la o putere"""
    return a ** b

def modulo(a, b):
    """Calculează restul împărțirii"""
    if b == 0:
        return "Eroare: Împărțire la zero!"
    return a % b

def calculator(operatie, a, b):
    """
    Calculator universal care folosește funcțiile de mai sus
    
    Args:
        operatie: operația de efectuat ('+', '-', '*', '/', '**', '%')
        a, b: numerele de calculat
    
    Returns:
        Rezultatul operației sau mesaj de eroare
    """
    operatii = {
        '+': adunare,
        '-': scadere,
        '*': inmultire,
        '/': impartire,
        '**': putere,
        '%': modulo
    }
    
    if operatie in operatii:
        return operatii[operatie](a, b)
    else:
        return f"Operația '{operatie}' nu este suportată"




# Testarea calculatorului
teste_calculator = [
    ('+', 10, 5),
    ('-', 10, 3),
    ('*', 4, 7),
    ('/', 15, 3),
    ('/', 10, 0),
    ('**', 2, 8),
    ('%', 17, 5),
    ('&', 5, 3)  # Operație invalidă
]

print("Testarea calculatorului:")
for op, num1, num2 in teste_calculator:
    rezultat = calculator(op, num1, num2)
    print(f"  {num1} {op} {num2} = {rezultat}")
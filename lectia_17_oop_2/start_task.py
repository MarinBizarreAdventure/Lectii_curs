# Exercițiul 3: Clasa Calculator Simplu
# Creează o clasă "Calculator" cu:
# - Un atribut "rezultat" (inițial 0)
# - Metode: aduna(numar), scade(numar), afiseaza_rezultat()

class Calculator:
    def __init__(self):
        self.rezultat = 0
    
    def aduna(self, numar):
        self.rezultat += numar
    
    def scade(self, numar):
        self.rezultat -= numar
    
    def afiseaza_rezultat(self):
        print(f"Rezultatul: {self.rezultat}")

# Testare Exercițiul 3:
# calc = Calculator()
# calc.aduna(10)
# calc.aduna(5)
# calc.scade(3)
# calc.afiseaza_rezultat()  # Ar trebui să afișeze: 12


# Exercițiul 4: Clasa Carte
# Creează o clasă "Carte" cu:
# - Atribute: titlu, autor, numar_pagini
# - Metode: afiseaza_info(), este_groasa() (returnează True dacă are >300 pagini)

class Carte:
    def __init__(self, titlu, autor, numar_pagini):
        self.titlu = titlu
        self.autor = autor
        self.numar_pagini = numar_pagini
    
    def afiseaza_info(self):
        print(f"Cartea:{self.titlu} Autor:{self.autor} Numar Pagini { self.numar_pagini}")

    
    def este_groasa(self):
        return self.numar_pagini > 300

# Testare Exercițiul 4:
carte1 = Carte("1984", "George Orwell", 350)
carte1.afiseaza_info()
print(f"Este o carte groasă? {carte1.este_groasa()}")
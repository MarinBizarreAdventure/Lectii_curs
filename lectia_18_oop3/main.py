import math 
from abc import ABC, abstractmethod
class FormaGeometrica:
    def __init__(self, nume):
        self.nume = nume

    @abstractmethod
    def calculeaza_aria(self):
        pass
    
    def descrie(self):
        return f"sunt o forma geometrica {self.nume}"
    

class Dreptunghi(FormaGeometrica):
    def __init__(self, lungime, latime):
        super().__init__("Dreptunghi")
        self.lungime = lungime
        self.latime = latime

    def calculeaza_aria(self):
        return self.latime * self.lungime
    
    def descrie(self):
        return super().descrie() + f" cu lungimea {self.lungime} si latimea {self.latime}"


class Cerc(FormaGeometrica):
    def __init__(self, raza):
        super().__init__("Cerc")
        self.raza = raza

    def calculeaza_aria(self):
        return math.pi * self.raza**2

    def descrie(self):
        return super().descrie() + f" cu raza {self.raza}"
    

class Triunghi(FormaGeometrica):
    def __init__(self, baza, inaltimea):
        super().__init__("Triunghi")
        self.baza = baza
        self.inaltimea = inaltimea

    def calculeaza_aria(self):
        return (self.baza * self.inaltimea) /2 
    
    def descrie(self):
        return super().descrie() + f" cu baza {self.baza} si cu inaltimea {self.inaltimea}"
    

class Patrat(Dreptunghi):
    def __init__(self, latura):
        super().__init__(latura, latura)
        self.nume = "Patrat"
        self.latura = latura

    def descrie(self):
        return f"Sunt un patrat cu latura {self.latura}"
    

def main():
    # Creăm o listă cu forme geometrice diferite
    forme_geometrice = [
        Dreptunghi(5, 3),
        Cerc(4),
        Triunghi(6, 8),
        Patrat(4),
        Cerc(2.5),
        Dreptunghi(10, 2)
    ]
    
    print("=== DEMONSTRAȚIA POLIMORFISMULUI ===\n")
    
    # Iterăm prin lista de forme și apelăm metodele
    for i, forma in enumerate(forme_geometrice, 1):
        print(f"Forma {i}:")
        print(f"  {forma.descrie()}")
        print(f"  Aria: {forma.calculeaza_aria():.2f}")
        print("-" * 40)
    
    # Calculăm aria totală
    aria_totala = sum(forma.calculeaza_aria() for forma in forme_geometrice)
    print(f"\n🎯 ARIA TOTALĂ A TUTUROR FORMELOR: {aria_totala:.2f}")
    
    # Găsim forma cu cea mai mare arie
    forma_maxima = max(forme_geometrice, key=lambda f: f.calculeaza_aria())
    print(f"🏆 FORMA CU ARIA CEA MAI MARE:")
    print(f"   {forma_maxima.descrie()}")
    print(f"   Aria: {forma_maxima.calculeaza_aria():.2f}")

# Rulăm exemplul
if __name__ == "__main__":
    main()



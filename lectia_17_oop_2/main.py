"""
Sistem de Comenzi Restaurant

Creați o clasă Comanda care gestionează comenzile dintr-un restaurant folosind un stoc global.
Stocul conține produse cu nume, preț și cantitate disponibilă.

Clasa trebuie să:
1. Permită adăugarea produselor cu verificarea stocului
2. Actualizeze automat stocul la adăugarea produselor
3. Calculeze și afișeze nota de plată

Exemplu:
# >>> cmd = Comanda(1)
# >>> cmd.adauga_produs("Pizza Margherita", 2)  # True
# >>> cmd.adauga_produs("Suc", 1)               # True
# >>> cmd.adauga_produs("Pizza Margherita", 4)  # False (stoc insuficient)
#
# >>> cmd.afiseaza_nota()
Nota masa 1:
Pizza Margherita x2: 70 lei
Suc x1: 8 lei
Total: 78.00 lei
"""


stoc = [
   {"produs": "Pizza Margherita", "pret": 35, "cantitate": 5},
   {"produs": "Pizza Quattro", "pret": 40, "cantitate": 3},
   {"produs": "Paste", "pret": 30, "cantitate": 10},
   {"produs": "Suc", "pret": 8, "cantitate": 15},
   {"produs": "Tiramisu", "pret": 25, "cantitate": 7},
   {"produs": "Panna Cotta", "pret": 20, "cantitate": 10},
   {"produs": "Cheesecake", "pret": 30, "cantitate": 5},
   {"produs": "Clătite cu Nutella", "pret": 18, "cantitate": 12},
   {"produs": "Înghețată", "pret": 10, "cantitate": 20},
   {"produs": "Tort de ciocolată", "pret": 35, "cantitate": 6}
]



class Comanda:
    def __init__(self, nr_mesei, stoc):
        self.nr_mesei = nr_mesei
        self.stoc = stoc
        self.produse = []
        self.pret = 0

    
    def adauga_produs(self, nume_produs, cantitate):
        produs = self.verificare_stoc(nume_produs, cantitate)
        if produs:
            self.actualizeaza_stoc(nume_produs, cantitate)

            self.produse.append((produs, cantitate))
            self.pret += cantitate* produs["pret"]



    def verificare_stoc(self, nume_produs, cantitate):
        for produs in self.stoc:
            if produs["produs"] == nume_produs and produs["cantitate"] >=cantitate:
                return produs
        return None
    
    def actualizeaza_stoc(self, nume_produs, cantitate):
        for produs in self.stoc:
            if produs["produs"] == nume_produs:
                produs["cantitate"] -= cantitate


    def __str__(self):
        res = f"Nota Mesei {self.nr_mesei}: \n\n"
        for tuple_produs in self.produse:
            res += f"{tuple_produs[0]["produs"]} X {tuple[1]} \n"

        res += f"Total: {self.pret}"
        return res


cmd = Comanda(3,stoc)
cmd.adauga_produs("Pizza Margherita", 2)
cmd.adauga_produs("Suc", 1)
cmd.adauga_produs("Pizza Margherita", 4)  # Va eșua - stoc insuficient
cmd.adauga_produs("Pizza Margherita", 1)
cmd.adauga_produs("Tiramisu", 2)
cmd.adauga_produs("Înghețată", 3)
print(cmd)
class Motor:
    def __init__(self, putere):
        self.__putere = putere  # atribut privat

    def descrie_motor(self):
        return f"Motor de {self.__putere} CP"


class Sofer:
    def __init__(self, nume):
        self.nume = nume  # atribut public

    def __verifica_permis(self):  # metodă privată
        return True

    def poate_conduce(self):  # metodă publică care folosește metoda privată
        return self.__verifica_permis()


class Masina:
    def __init__(self, marca, sofer):
        self.__marca = marca  # atribut privat
        self.sofer = sofer    # agregare: șoferul este dat din exterior
        self.motor = Motor(100)  # compoziție: motorul este creat în interior

    def porneste(self):
        if self.sofer.poate_conduce():
            print(f"Mașina {self.__marca} pornește.")
            print(f"{self.motor.descrie_motor()}")
        else:
            print("Șoferul nu are permis. Mașina nu poate porni.")


# Exemplu de utilizare:
if __name__ == "__main__":
    sofer = Sofer("Maria")
    masina = Masina("Dacia", sofer)
    masina.porneste()

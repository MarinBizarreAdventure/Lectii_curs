class Persoana:
    def __init__(self, nume, varsta, email):
        if not nume or not isinstance(nume, str):
            raise ValueError("numele trebuie sa fie un string nevid")
        if not isinstance(varsta, int) or varsta < 0:
            raise ValueError("Varsta trebuie sa fie numar pozitiv")
        self.valideaza_email(email)
        self.email = email
        
        self.nume = nume
        self.varsta = varsta

    def valideaza_email(self, email):
        if "@" not in email:
            raise ValueError("Email invalid")


Per1 = Persoana("ion", 22, "iongmail.com")
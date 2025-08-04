"""
Task: Sistem de Management al unei Biblioteci

Timp alocat: 15-20 minute

Creați următoarele clase pentru a gestiona o bibliotecă:

1. Clasa Book:
   - Atribute: title, author, year, isbn
   - Metodele __str__ și __repr__
   - O staticmethod care validează ISBN-ul (trebuie să aibă 13 cifre)

2. Clasa Library:
   - Moștenește o clasă de bază Building (cu atribute: address, floors)
   - Atribute adiționale: books (listă), staff (listă)
   - Metode pentru:
     * adăugare carte
     * căutare carte după ISBN
     * afișare toate cărțile unui autor

Bonus:
- Implementați o metodă de sortare a cărților după anul publicării
- Adăugați management al erorilor pentru ISBN invalid

Test data:
book1 = Book("Amintiri din copilărie", "Ion Creangă", 1892, "1234567890123")
book2 = Book("Luceafărul", "Mihai Eminescu", 1883, "9876543210123")
"""


class Book:
    def __init__(self, title, author, year, isbn):
        self.title =title
        self.author = author
        self.year = year
        self.isbn = isbn

    def __str__(self):
        return f"Cartea {self.title} este scrisa de {self.author} in anul {self.year}"

    def __repr__(self):
        return f"Book=({self.title},{self.author}, {self.year}, {self.isbn})"
    
    @staticmethod
    def validate_isbn(isbn):
        isbn = str(isbn)
        return len(isbn) == 13 and isbn.isdigit()
    


# 2. Clasa Library:
#  
#  
#    - Metode pentru:
#      * adăugare carte
#      * căutare carte după ISBN
#      * afișare toate cărțile unui autor

class Building:
    def __init__(self, address, floors):
        self.address = address
        self.floors = floors

    
class Library(Building):
    def __init__(self, address, floors, books=None, staff=None):
        super().__init__(address, floors)
        self.books = books if books is not None else []
        self.staff = staff if staff is not None else []

    
    def adaugare_carte(self, carte):
        if isinstance(carte, Book):
            if Book.validate_isbn(carte.isbn):
                for carte_in_library in self.books:
                    if carte_in_library.isbn == carte.isbn:
                        return "Aceasta carte deja exista in biblioteca noastra"
                    
                self.books.append(carte)
                print(f"Cartea {carte.title} a fost adaugata cu succes")

    
    def cauta_carte_dupa_isbn(self, isbn):
        if not Book.validate_isbn(isbn):
            return f"isbn invalid!!"
        
        for carte in self.books:
            if carte.isbn == isbn:
                return carte.__str__()
            
        return f"Cartea cu isbnul: {isbn} nu a fost gasita"
    

    def afisare_carti_autor(self, autor):
        lista_carti = []

        for carte in self.books:
            if carte.author == autor:
                lista_carti.append(carte)
        
        if len(lista_carti) == 0:
            return ["autorul nu are carti in biblioteca"]
        return lista_carti
    

book1 = Book("Amintiri din copilărie", "Ion Creangă", 1892, "1234567890123")
book2 = Book("Luceafărul", "Mihai Eminescu", 1883, "9876543210123")
librarie = Library("stefan cel mare", 4,[book1,book2])
print(librarie.books)
print(librarie.afisare_carti_autor("Mihai Eminescu"))
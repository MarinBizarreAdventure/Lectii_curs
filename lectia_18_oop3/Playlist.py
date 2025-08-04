"""
Temă: Implementarea unui Sistem de Playlist-uri Muzicale

Creați o clasă Playlist care va gestiona o colecție de melodii.
Clasa trebuie să suporte operațiile de bază pentru gestionarea unui playlist muzical.

Pentru fiecare melodie trebuie să păstrați:
- Titlul
- Artistul
- Durata (în secunde)

Implementați obligatoriu:
__str__ pentru afișarea frumoasă a playlist-ului
__repr__ pentru afișarea tehnică a tuturor detaliilor
@staticmethod pentru validări și conversii de timp

Bonus pentru:
1. Sortare melodii (după artist, titlu sau durată)
2. Căutare melodii
3. Filtrare melodii (ex: doar melodii sub 4 minute)
4. Statistici (ex: artist cu cele mai multe melodii)

Se evaluează:
1. Folosirea corectă a __str__ și __repr__
2. Implementarea metodelor statice
3. Validări implementate
4. Organizarea codului
5. Claritatea implementării
"""

import random 

class Playlist:
    def __init__(self, nume):
        self.nume = nume
        self.melodii = []

    def __str__(self):
        durata_totala = self.converteste_durata(self.durata_totala())
        return f"Playlist: {self.nume} | {len(self.melodii)} melodii  | Durata totala: {durata_totala}"
        

    def __repr__(self):
        rezultat = f'Playlist("{self.nume}") \n'
        for i, melodie in enumerate(self.melodii):
            durata_str = self.converteste_durata(melodie["durata"])
            rezultat += f"{i}. {melodie['artist']} - {melodie["titlu"]} ({durata_str})\n"

        return rezultat

    
    @staticmethod
    def valideaza_melodie(artist, titlu, durata):
        if len(artist) <2:
            return False, "Artistul trebuie sa aiba mai mult de 2 caractere" 
        if len(titlu) < 3:
            return False, "Titlu trebuie sa fie mai lung de 3 caractere"
        if not (30<=durata <= 600):
            return False, "Durata trebuie sa fie intre 30 si 600 de secunde"
        return True, "Valid"
    
    
    @staticmethod
    def converteste_durata(secunde):
        minute = secunde // 60
        secunde_ramase = secunde % 60
        return f"{minute}:{secunde_ramase}"

    def adauga_melodie(self, artist, titlu, durata):
        valid, mesaj = self.valideaza_melodie(artist, titlu, durata)

        if not valid:
            print(f"Eroare: {mesaj}")
            return
        
        melodie ={
            "artist" : artist,
            "titlu":titlu,
            "durata":durata
        }
        self.melodii.append(melodie)
        print(f"Melodia {titlu} a fost adaugata!")


    def sterge_melodie(self, titlu):
        for i, melodie in enumerate(self.melodii):
            if melodie["titlu"] == titlu:
                self.melodii.pop(i)
                print(f'Melodia {titlu} a fost stearsa!')
                return
        print(f"melodia {titlu} nu a fost gasita in playlist")


    def amesteca(self):
        random.shuffle(self.melodii)
        print(f"Playlistul {self.name} a fost amestecat")

    def durata_totala(self):
        return sum(melodie["durata"] for melodie in self.melodii)
    

    def sorteaza(self, criteriu="titlu"):
        if criteriu == "titlu":
            self.melodii.sort(key= lambda x: x["titlu"])
        elif criteriu == "artist":
            self.melodii.sort(key= lambda x: x["artist"])
        elif criteriu == "durata":
            self.melodii.sort(key= lambda x: x["durata"])
        print(f"Playlistul a fost sortat dupa criteriul {criteriu}")



if __name__  == "__main__":
    playlist = Playlist("Summer Hits")

    playlist.adauga_melodie("Queen", "boheian Rhapsody", 354)
    playlist.adauga_melodie("The Beatles", "yesterday", 163)
    playlist.adauga_melodie("pink floyd", "another brick in the wall", 400)

    print(playlist)
    print("Detalii tehnice:")
    print(repr(playlist))

    playlist.sorteaza()

    print("Detalii tehnice:")
    print(repr(playlist))

    playlist.sterge_melodie("yesterday")

    print("Detalii tehnice:")
    print(repr(playlist))





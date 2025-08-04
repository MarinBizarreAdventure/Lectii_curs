# Exerciții Simple NumPy și Pandas - 10 minute fiecare

## 🚀 Exercițiul 1: NumPy de Bază - Primul meu array (10 min)

### Obiectiv: Să creezi și să lucrezi cu primul tău array NumPy

```python
import numpy as np

# PASUL 1: Creează primul array (2 min)
# Fă un array cu numerele de la 1 la 5
primul_meu_array = np.array([1, 2, 3, 4, 5])
print("Array-ul meu:", primul_meu_array)

# PASUL 2: Operații simple (3 min)
# Înmulțește toate numerele cu 2
array_inmultit = primul_meu_array * 2
print("Înmulțit cu 2:", array_inmultit)

# Adună 10 la toate numerele
array_adunat = primul_meu_array + 10
print("Plus 10:", array_adunat)

# PASUL 3: Informații despre array (2 min)
print("Lungimea array-ului:", len(primul_meu_array))
print("Suma tuturor numerelor:", np.sum(primul_meu_array))
print("Cea mai mare valoare:", np.max(primul_meu_array))

# PASUL 4: Exercițiu personal (3 min)
# Creează un array cu vârstele tale și ale familiei
# Calculează vârsta medie
varste = np.array([25, 50, 48, 22])  # Exemplu - pune vârstele reale!
varsta_medie = np.mean(varste)
print(f"Vârsta medie în familie: {varsta_medie:.1f} ani")
```

**🎯 Ce să înveți:** Crearea array-urilor, operații de bază, funcții simple

---

## 🚀 Exercițiul 2: NumPy - Tablouri 2D simple (10 min)

### Obiectiv: Să lucrezi cu "tabele" de numere

```python
import numpy as np

# PASUL 1: Creează o "tabelă" 3x3 (3 min)
# Gândește-te la ea ca la o grilă de numere
tabel = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
print("Tabelul meu 3x3:")
print(tabel)

# PASUL 2: Explorează tabelul (3 min)
print("Forma tabelului:", tabel.shape)  # Câte rânduri și coloane
print("Primul rând:", tabel[0])         # Rândul de sus
print("Ultima coloană:", tabel[:, 2])   # Coloana din dreapta

# PASUL 3: Calculează cu tabelul (2 min)
print("Suma pe fiecare rând:", np.sum(tabel, axis=1))
print("Suma pe fiecare coloană:", np.sum(tabel, axis=0))

# PASUL 4: Exercițiu practic - Notele tale (2 min)
# Creează un tabel cu notele tale la 3 materii în 3 luni
note = np.array([[8, 9, 7],    # Matematică: Ian, Feb, Mar
                 [7, 8, 9],    # Română: Ian, Feb, Mar  
                 [9, 8, 8]])   # Engleză: Ian, Feb, Mar

media_pe_materie = np.mean(note, axis=1)
print("Media pe materii:", media_pe_materie)
```

**🎯 Ce să înveți:** Array-uri 2D, indexarea, calcularea pe axe

---

## 🚀 Exercițiul 3: Pandas - Prima mea listă de cumpărături (10 min)

### Obiectiv: Să creezi și să gestionezi o listă de cumpărături cu Pandas

```python
import pandas as pd

# PASUL 1: Creează o listă de cumpărături (3 min)
cumparaturi = pd.Series(['pâine', 'lapte', 'ouă', 'brânză', 'mere'])
preturi = pd.Series([2.5, 4.0, 6.0, 15.0, 8.0])

print("Lista de cumpărături:")
print(cumparaturi)
print("\nPrețurile:")
print(preturi)

# PASUL 2: Combină informațiile (3 min)
# Creează un "tabel" cu produse și prețuri
lista_completa = pd.DataFrame({
    'Produs': cumparaturi,
    'Pret': preturi
})
print("\nLista completă:")
print(lista_completa)

# PASUL 3: Calculează total (2 min)
total = lista_completa['Pret'].sum()
print(f"\nTotal de plată: {total} lei")

# Găsește cel mai scump produs
cel_mai_scump = lista_completa[lista_completa['Pret'] == lista_completa['Pret'].max()]
print("\nCel mai scump produs:")
print(cel_mai_scump)

# PASUL 4: Adaugă cantități (2 min)
lista_completa['Cantitate'] = [1, 2, 10, 1, 2]  # bucăți/kg/litri
lista_completa['Total_per_produs'] = lista_completa['Pret'] * lista_completa['Cantitate']

print("\nLista finală cu cantități:")
print(lista_completa)
print(f"Total final: {lista_completa['Total_per_produs'].sum()} lei")
```

**🎯 Ce să înveți:** Series, DataFrame, operații de bază, calcularea totale

---

## 🚀 Exercițiul 4: Pandas - Notele mele la școală (10 min)

### Obiectiv: Să analizezi notele tale cu Pandas

```python
import pandas as pd

# PASUL 1: Creează tabelul cu notele (3 min)
note_scolare = pd.DataFrame({
    'Materia': ['Matematică', 'Română', 'Engleză', 'Istorie', 'Fizică'],
    'Nota_1': [8, 9, 7, 6, 8],
    'Nota_2': [9, 8, 8, 7, 7],
    'Nota_3': [7, 9, 9, 8, 9]
})

print("Notele mele:")
print(note_scolare)

# PASUL 2: Calculează mediile (3 min)
# Media pentru fiecare materie
note_scolare['Media'] = (note_scolare['Nota_1'] + 
                        note_scolare['Nota_2'] + 
                        note_scolare['Nota_3']) / 3

print("\nCu mediile calculate:")
print(note_scolare)

# PASUL 3: Analizează performanța (2 min)
media_generala = note_scolare['Media'].mean()
print(f"\nMedia mea generală: {media_generala:.2f}")

# Materia la care merg cel mai bine
materia_cea_mai_buna = note_scolare[note_scolare['Media'] == note_scolare['Media'].max()]
print("\nMateria mea preferată (cea mai bună medie):")
print(materia_cea_mai_buna['Materia'].values[0])

# PASUL 4: Găsește materiile unde trebuie să te îmbunătățești (2 min)
materiile_de_imbunatatit = note_scolare[note_scolare['Media'] < 8]
print("\nMateriile unde trebuie să mă îmbunătățesc:")
print(materiile_de_imbunatatit[['Materia', 'Media']])
```

**🎯 Ce să înveți:** DataFrame-uri, calcularea mediilor, filtrarea datelor

---

## 🚀 Exercițiul 5: Pandas - Analizez filmele mele preferate (10 min)

### Obiectiv: Să gestionezi o colecție de filme cu Pandas

```python
import pandas as pd

# PASUL 1: Creează colecția de filme (3 min)
filme = pd.DataFrame({
    'Titlu': ['Avatar', 'Titanic', 'Avengers', 'Harry Potter', 'Frozen'],
    'An': [2009, 1997, 2019, 2001, 2013],
    'Rating': [7.8, 7.9, 8.4, 7.6, 7.4],
    'Vizionat': ['Da', 'Da', 'Nu', 'Da', 'Nu']
})

print("Colecția mea de filme:")
print(filme)

# PASUL 2: Analizează colecția (3 min)
print(f"\nAm în total {len(filme)} filme în listă")

# Filme vizionate
filme_vizionate = filme[filme['Vizionat'] == 'Da']
print(f"Am vizionat {len(filme_vizionate)} filme")

# Cel mai bun rating
cel_mai_bun_film = filme[filme['Rating'] == filme['Rating'].max()]
print(f"\nFilmul cu cel mai bun rating: {cel_mai_bun_film['Titlu'].values[0]}")

# PASUL 3: Filme de vizionat (2 min)
filme_de_vizionat = filme[filme['Vizionat'] == 'Nu']
print("\nFilme pe care trebuie să le văd:")
print(filme_de_vizionat[['Titlu', 'Rating']])

# PASUL 4: Statistici rapide (2 min)
rating_mediu = filme['Rating'].mean()
print(f"\nRating-ul mediu al filmelor: {rating_mediu:.1f}")

# Filme mai noi de 2010
filme_noi = filme[filme['An'] > 2010]
print(f"Filme din ultimii 15 ani: {len(filme_noi)}")
```

**🎯 Ce să înveți:** Filtrarea datelor, statistici de bază, lucru cu text

---

## 🚀 Exercițiul 6: NumPy + Pandas - Bugetul meu lunar (10 min)

### Obiectiv: Să analizezi bugetul personal cu ambele biblioteci

```python
import numpy as np
import pandas as pd

# PASUL 1: Creează datele de buget (3 min)
categorii = ['Mâncare', 'Transport', 'Distracție', 'Haine', 'Economii']
buget_planificat = np.array([800, 200, 300, 400, 500])
buget_cheltuit = np.array([850, 180, 350, 200, 500])

# PASUL 2: Calculează diferențele cu NumPy (2 min)
diferente = buget_cheltuit - buget_planificat
print("Diferențele (cheltuit - planificat):")
print(diferente)

peste_buget = diferente > 0
print("Categorii unde am cheltuit peste buget:", np.sum(peste_buget))

# PASUL 3: Creează tabel cu Pandas (3 min)
buget_df = pd.DataFrame({
    'Categorie': categorii,
    'Planificat': buget_planificat,
    'Cheltuit': buget_cheltuit,
    'Diferenta': diferente
})

print("\nRaportul bugetului:")
print(buget_df)

# PASUL 4: Analize finale (2 min)
total_planificat = buget_df['Planificat'].sum()
total_cheltuit = buget_df['Cheltuit'].sum()

print(f"\nTotal planificat: {total_planificat} lei")
print(f"Total cheltuit: {total_cheltuit} lei")
print(f"Diferența: {total_cheltuit - total_planificat} lei")

if total_cheltuit > total_planificat:
    print("🚨 Am cheltuit peste buget!")
else:
    print("✅ Am respectat bugetul!")
```

**🎯 Ce să înveți:** Combinarea NumPy cu Pandas, analize bugetare

---

## 🚀 Exercițiul 7: Pandas - Vremea săptămânii (10 min)

### Obiectiv: Să analizezi datele despre vreme

```python
import pandas as pd
import numpy as np

# PASUL 1: Creează datele meteo (3 min)
vremea = pd.DataFrame({
    'Ziua': ['Luni', 'Marți', 'Miercuri', 'Joi', 'Vineri', 'Sâmbătă', 'Duminică'],
    'Temperatura': [22, 25, 23, 20, 18, 24, 26],
    'Precipitatii': [0, 0, 5, 12, 8, 0, 0],
    'Vant': [10, 15, 20, 25, 30, 12, 8]
})

print("Prognoza vremii pentru săptămână:")
print(vremea)

# PASUL 2: Zilele frumoase (3 min)
# O zi frumoasă = temperatura > 20°C și fără precipitații
zile_frumoase = vremea[(vremea['Temperatura'] > 20) & (vremea['Precipitatii'] == 0)]
print(f"\nZile frumoase în săptămână: {len(zile_frumoase)}")
print(zile_frumoase['Ziua'].values)

# PASUL 3: Statistici (2 min)
print(f"\nTemperatura medie: {vremea['Temperatura'].mean():.1f}°C")
print(f"Cea mai caldă zi: {vremea['Temperatura'].max()}°C")
print(f"Cea mai rece zi: {vremea['Temperatura'].min()}°C")

# PASUL 4: Zilele de ploaie (2 min)
zile_ploioase = vremea[vremea['Precipitatii'] > 0]
print(f"\nZile cu ploaie: {len(zile_ploioase)}")
print("Total precipitații:", vremea['Precipitatii'].sum(), "mm")
```

**🎯 Ce să înveți:** Filtrarea cu multiple condiții, statistici meteorologice

---

## 🚀 Exercițiul 8: NumPy - Joc simplu cu zaruri (10 min)

### Obiectiv: Să simulezi aruncări de zaruri cu NumPy

```python
import numpy as np

# PASUL 1: Simulează aruncări de zaruri (3 min)
# Aruncă un zar de 100 de ori
aruncari = np.random.randint(1, 7, 100)  # Numere de la 1 la 6
print("Primele 20 de aruncări:", aruncari[:20])

# PASUL 2: Analizează rezultatele (3 min)
print(f"\nNumărul total de aruncări: {len(aruncari)}")
print(f"Suma tuturor aruncărilor: {np.sum(aruncari)}")
print(f"Media aruncărilor: {np.mean(aruncari):.2f}")

# Câte ori a ieșit fiecare număr
for numar in range(1, 7):
    aparitii = np.sum(aruncari == numar)
    print(f"Numărul {numar} a ieșit {aparitii} ori")

# PASUL 3: Noroc sau ghinion? (2 min)
# Câte aruncări "bune" (5 sau 6)
aruncari_bune = np.sum((aruncari == 5) | (aruncari == 6))
print(f"\nAruncări norocoase (5 sau 6): {aruncari_bune}")

# PASUL 4: Joc cu 2 zaruri (2 min)
zar1 = np.random.randint(1, 7, 50)
zar2 = np.random.randint(1, 7, 50)
suma_zaruri = zar1 + zar2

print(f"\nJoc cu 2 zaruri - 50 de aruncări:")
print(f"Cea mai mare sumă: {np.max(suma_zaruri)}")
print(f"Câte ori am făcut 7: {np.sum(suma_zaruri == 7)}")  # 7 e cel mai probabil
```

**🎯 Ce să înveți:** Numere aleatorii, simulări, operații logice

---

## 🚀 Exercițiul 9: Pandas - Playlist-ul meu muzical (10 min)

### Obiectiv: Să gestionezi o listă de melodii

```python
import pandas as pd

# PASUL 1: Creează playlist-ul (3 min)
playlist = pd.DataFrame({
    'Melodie': ['Bohemian Rhapsody', 'Imagine', 'Hotel California', 'Billie Jean', 'Sweet Child O Mine'],
    'Artist': ['Queen', 'John Lennon', 'Eagles', 'Michael Jackson', 'Guns N Roses'],
    'Durata_minute': [6.0, 3.1, 6.5, 4.9, 5.6],
    'Gen': ['Rock', 'Pop', 'Rock', 'Pop', 'Rock'],
    'An': [1975, 1971, 1976, 1983, 1987]
})

print("Playlist-ul meu:")
print(playlist)

# PASUL 2: Analizează playlist-ul (3 min)
durata_totala = playlist['Durata_minute'].sum()
print(f"\nDurata totală: {durata_totala:.1f} minute ({durata_totala/60:.1f} ore)")

# Melodia cea mai lungă
melodia_lunga = playlist[playlist['Durata_minute'] == playlist['Durata_minute'].max()]
print(f"Cea mai lungă melodie: {melodia_lunga['Melodie'].values[0]}")

# PASUL 3: Filtrare pe gen (2 min)
melodii_rock = playlist[playlist['Gen'] == 'Rock']
print(f"\nMelodii Rock: {len(melodii_rock)}")
print(melodii_rock[['Melodie', 'Artist']])

# PASUL 4: Melodii vintage (2 min)
melodii_vechi = playlist[playlist['An'] < 1980]
print(f"\nMelodii din anii '70: {len(melodii_vechi)}")
durata_medie = playlist['Durata_minute'].mean()
print(f"Durata medie pe melodie: {durata_medie:.1f} minute")
```

**🎯 Ce să înveți:** Lucru cu string-uri, filtrarea pe categorii, calcule temporale

---

## 🚀 Exercițiul 10: NumPy + Pandas - Analiză sportivă simplă (10 min)

### Obiectiv: Să analizezi scoruri la fotbal

```python
import numpy as np
import pandas as pd

# PASUL 1: Creează meciurile (3 min)
echipe = ['Barcelona', 'Real Madrid', 'Liverpool', 'Manchester City', 'PSG']
goluri_marcate = np.random.randint(0, 5, 5)  # 0-4 goluri pentru fiecare echipă
goluri_primite = np.random.randint(0, 4, 5)  # 0-3 goluri primite

# PASUL 2: Creează tabelul cu Pandas (3 min)
clasament = pd.DataFrame({
    'Echipa': echipe,
    'Goluri_marcate': goluri_marcate,
    'Goluri_primite': goluri_primite
})

# Calculează diferența de goluri
clasament['Diferenta'] = clasament['Goluri_marcate'] - clasament['Goluri_primite']

print("Rezultatele echipelor:")
print(clasament)

# PASUL 3: Analizează performanțele (2 min)
# Echipa cu cel mai bun atac
cel_mai_bun_atac = clasament[clasament['Goluri_marcate'] == clasament['Goluri_marcate'].max()]
print(f"\nCel mai bun atac: {cel_mai_bun_atac['Echipa'].values[0]}")

# Echipa cu cea mai bună apărare
cea_mai_buna_aparare = clasament[clasament['Goluri_primite'] == clasament['Goluri_primite'].min()]
print(f"Cea mai bună apărare: {cea_mai_buna_aparare['Echipa'].values[0]}")

# PASUL 4: Clasament final (2 min)
# Sortează după diferența de goluri
clasament_final = clasament.sort_values('Diferenta', ascending=False)
print("\nClasamentul final (după diferența de goluri):")
print(clasament_final)

print(f"\nCâmpioana: {clasament_final.iloc[0]['Echipa']}! 🏆")
```

**🎯 Ce să înveți:** Combinarea bibliotecilor, sortarea, analize sportive

---

## 📝 Sfaturi pentru Exerciții

### ✅ **Înainte să începi:**
1. **Instalează bibliotecile:** `pip install numpy pandas`
2. **Deschide un Jupyter Notebook** sau un fișier Python nou
3. **Rulează pas cu pas** - nu te grăbi!

### 🎯 **În timpul exercițiilor:**
- **Schimbă datele** cu informații personale (vârstele, notele, etc.)
- **Experimentează** - încearcă să modifici valorile
- **Printează des** - vezi ce se întâmplă la fiecare pas

### 🚀 **După ce termini:**
- **Combină exercițiile** - de exemplu, fă un buget cu playlist muzical
- **Creează variante** - în loc de filme, folosește cărți sau jocuri
- **Pune întrebări noi** datelor - "Care e cea mai..." sau "Câte sunt..."

### 💡 **Dacă te blochezi:**
1. **Citește eroarea** cu atenție
2. **Printează variabilele** să vezi ce conțin
3. **Încearcă cu date mai simple** mai întâi
4. **Google it** - "pandas how to..." sau "numpy tutorial..."

**Timp total:** ~100 minute pentru toate exercițiile
**Dificultate:** Foarte ușor - perfect pentru începători! 

🎉 **Mult succes și să te distrezi învățând!**
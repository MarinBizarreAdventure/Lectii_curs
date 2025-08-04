# Start Task - Virtual Environment și Matplotlib

## 🎯 Obiectiv
Creează un mediu virtual, instalează matplotlib și realizează 4 grafice diferite într-un subplot.

## ⏱️ Timp estimat: 15 minute

---

## 📋 Instrucțiuni Pas cu Pas

### 1. Crearea Mediului Virtual (3 minute)
- Deschide terminalul/command prompt
- Navighează într-un director unde vrei să lucrezi
- Creează un mediu virtual numit `venv`
- Activează mediul virtual
- Verifică că ești în mediul virtual (trebuie să vezi `(venv)` în prompt)

### 2. Instalarea Matplotlib (2 minute)
- Cu mediul virtual activ, instalează matplotlib
- Verifică instalarea importând matplotlib în Python

### 3. Crearea Script-ului Python (10 minute)
Creează un fișier numit `grafice.py` cu următoarele caracteristici:

#### Structura necesară:
- Importă matplotlib.pyplot
- Creează o figură cu 4 subplot-uri (2x2)
- Realizează 4 tipuri diferite de grafice:

#### Graficul 1 - Line Plot (sus stânga):
- **Date sugerate**: 
  - x: numerele de la 1 la 10
  - y: pătratele numerelor (1, 4, 9, 16, ...)
- **Titlu**: "Funcția x²"
- **Culoare**: albastru

#### Graficul 2 - Pie Chart (sus dreapta):
- **Date sugerate**: 
  - Limbaje de programare și popularitatea lor
  - Exemple: Python (35%), JavaScript (25%), Java (20%), C++ (20%)
- **Titlu**: "Popularitatea Limbajelor"
- **Afișează procentele**

#### Graficul 3 - Histogram (jos stânga):
- **Date sugerate**: 
  - Liste cu note ale unui student: [7, 8, 9, 7, 6, 8, 9, 10, 7, 8, 9, 6, 7, 8, 9, 10]
- **Titlu**: "Distribuția Notelor"
- **Culoare**: verde
- **Numărul de bins**: 5

#### Graficul 4 - Bar Chart (jos dreapta):
- **Date sugerate**: 
  - Lunile: Ian, Feb, Mar, Apr, Mai
  - Temperaturi: 2, 5, 12, 18, 25
- **Titlu**: "Temperatura Medie pe Luni"
- **Culoare**: portocaliu

### 4. Finalizarea (2 minute)
- Ajustează layout-ul folosind `plt.tight_layout()`
- Afișează graficele cu `plt.show()`
- Rulează script-ul și verifică rezultatele

---

## 🎯 Rezultatul Final Așteptat
Ar trebui să ai:
- ✅ Un mediu virtual activ numit `venv`
- ✅ Matplotlib instalat în mediul virtual
- ✅ Un script `grafice.py` care afișează 4 grafice diferite
- ✅ Fiecare grafic să aibă date, titlu și să fie vizibil

---

## 💡 Hints
- Pentru mediul virtual: `python -m venv venv`
- Pentru activare pe Windows: `venv\Scripts\activate`
- Pentru activare pe Mac/Linux: `source venv/bin/activate`
- Pentru matplotlib: `pip install matplotlib`
- Pentru subplot: `plt.subplot(2, 2, poziția)`
- Pozițiile subplot-urilor: 1 (sus stânga), 2 (sus dreapta), 3 (jos stânga), 4 (jos dreapta)

---

## ❓ Întrebări de Verificare
1. Ce comandă folosești pentru a verifica că ești în mediul virtual?
2. De ce este important să folosești medii virtuale?
3. Care este diferența între `plot()` și `bar()`?
4. Cum poți salva graficul într-un fișier în loc să-l afișezi?

---

**Mult succes! 🚀**
# Python Fundamentals - Lecția 25: NumPy și Pandas pentru Prelucrarea Datelor

## 🎯 Obiectivele Lecției
- Înțelegerea conceptelor fundamentale ale bibliotecii NumPy
- Lucrul cu array-uri multidimensionale (ndarray)
- Introducere în biblioteca Pandas
- Utilizarea Series și DataFrame pentru analiza datelor
- Operații de indexare, filtrare și manipulare a datelor

---

## 📅 Recapitulare și Context

### ✅ Unde ne aflăm în curs:
- **Modul 7 - Librării Externe Python** (Lecția 2/7)
- Am învățat despre PIP și librării externe
- Urmează: vizualizarea datelor cu Matplotlib și Seaborn
- Context: pregătire pentru Data Science și Machine Learning

---

## 📊 NumPy - Numerical Python

### 📖 Introducere în NumPy

**NumPy** reprezintă biblioteca fundamentală necesară pentru calculul performant și analiza datelor în Python. Este proiectat pentru eficiență pe seturi mari de date.

#### **De ce NumPy?**

**NumPy oferă:**
- **ndarray** pentru crearea de tablouri multidimensionale
  - Stochează intern datele într-un bloc contiguu de memorie
  - Utilizează mult mai puțină memorie decât secvențele Python încorporate
- **Funcții matematice standard** pentru operațiuni rapide pe întreg tablouri de date
  - Permite exprimarea operațiunilor batch pe date fără a scrie bucle for
  - Acest lucru se numește **vectorizare**

### 🚀 Avantajele NumPy vs Liste Python

#### **1. Performanță superioară**
```python
import time
import numpy as np

# Test de performanță
start_time_numpy = time.time()
my_array = np.arange(1000000)
end_time_numpy = time.time()
print("Timp NumPy:", end_time_numpy - start_time_numpy)

start_time_list = time.time()
my_list = list(range(1000000))
end_time_list = time.time()
print("Timp List:", end_time_list - start_time_list)

# Rezultat: NumPy este de 10-100x mai rapid!
```

#### **2. Memorie eficiență**
- **NumPy:** Tip fix (Fixed Type) - toate elementele au același tip
- **Liste Python:** Fiecare element este un obiect Python complet cu overhead

#### **3. Operații vectorizate**
```python
# Liste Python - EROARE
a = [1, 3, 5]
b = [1, 2, 3]
# a * b = ERROR

# NumPy - Funcționează perfect
a = np.array([1, 3, 5])
b = np.array([1, 2, 3])
# a * b = np.array([1, 6, 15])
```

### 🔢 Tipuri de Array-uri NumPy

#### **Array-uri 1D, 2D și 3D**
```python
import numpy as np

# 1D array - shape: (4,)
arr_1d = np.array([7, 2, 9, 10])

# 2D array - shape: (2, 3)
arr_2d = np.array([[5.2, 3.0, 4.5],
                   [9.1, 0.1, 0.3]])

# 3D array - shape: (4, 3, 2)
arr_3d = np.random.randint(0, 10, (4, 3, 2))
```

### 🛠️ Crearea Array-urilor NumPy

#### **1. Din liste existente**
```python
import numpy as np

# Array 1D
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
print(arr1.dtype)  # float64
print(arr1.shape)  # (5,)
print(arr1.ndim)   # 1

# Array 2D
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
print(arr2.ndim)   # 2
print(arr2.shape)  # (2, 4)
```

#### **2. Array-uri cu valori speciale**
```python
# Array de zerouri
zero_array = np.zeros((2, 3))
print(zero_array)
# [[0. 0. 0.]
#  [0. 0. 0.]]

# Array de unu-uri
ones_array = np.ones((2, 3))
print(ones_array)
# [[1. 1. 1.]
#  [1. 1. 1.]]

# Matrice identitate
eye_array = np.eye(3)
print(eye_array)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]
```

#### **3. Array-uri cu valori aleatorii**
```python
# Numere întregi aleatorii
random_int_array = np.random.randint(0, 10, (3, 3))
print(random_int_array)

# Numere float aleatorii între 0 și 10
array_interval = np.random.uniform(0, 10, (3, 3))
print(array_interval)
```

### ➕ Operații Aritmetice cu Array-uri

#### **Operații element cu element**
```python
arr = np.array([[1., 2., 3.],
                [4., 5., 6.]])

# Operații cu sine
print(arr * arr)    # Înmulțire element cu element
print(arr - arr)    # Scădere element cu element
print(arr ** 2)     # Ridicare la putere

# Operații cu scalari
print(arr + 10)     # Adună 10 la fiecare element
print(arr * 2)      # Înmulțește fiecare element cu 2
```

#### **Comparații între array-uri**
```python
arr1 = np.array([[1., 2., 3.], [4., 5., 6.]])
arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])

result = arr2 > arr1
print(result)
# [[False  True False]
#  [ True False  True]]
```

### 🔍 Indexarea și Slicing

#### **Indexarea de bază**
```python
arr = np.arange(10)  # [0 1 2 3 4 5 6 7 8 9]

# Modificare prin slice - ATENȚIE: modifică array-ul original!
arr_slice = arr[5:8]
arr_slice[1] = 0
print(arr)  # [0 1 2 3 4 5 0 7 8 9]
```

**⚠️ Important:** Array-urile NumPy returnează vizualizări, nu copii!

---

## 🐼 Pandas - Python Data Analysis Library

### 📖 Introducere în Pandas

**Pandas** este una dintre cele mai populare biblioteci utilizate de oamenii de știință din domeniul datelor, oferind:

- **Axe etichetate** pentru a evita alinierea greșită a datelor
- **Gestionarea valorilor lipsă** sau speciale
- **Structuri de date bogate** și funcții pentru lucrul rapid cu datele

### 🏗️ Prezentare Generală

**Pandas** a fost creată de **Wes McKinney** în 2008 (autorul cărții "Python for Data Analysis"):
- Biblioteca Python puternică și productivă pentru analiza și gestionarea datelor
- Numele provine din "**Panel Data**" - un termen din econometrie
- Este construită pe baza NumPy
- Oferă caracteristici similare cu R, MATLAB, SAS

**Componente cheie:**
- **Series** - structuri de date 1D
- **DataFrame** - structuri de date 2D (tabele)

---

## 📈 Pandas Series

### 📖 Ce este un Series?

**Series** este un obiect asemănător unui array unidimensional care conține:
- Un array de date (de orice tip NumPy)
- Indexuri asociate (pot fi string-uri, numere, etc.)
- Implicit, indexarea este de la 0 la N-1

### 🔧 Crearea unui Series

```python
from pandas import Series
import pandas as pd

# Series simplu
obj = Series([4, 7, -5, 3])
print(obj)
print(obj.index)    # RangeIndex(start=0, stop=4, step=1)
print(obj.values)   # [ 4  7 -5  3]
```

### 🏷️ Series cu Index Personalizat

```python
# Series cu index personalizat
obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2)
print(obj2['a'])    # -5

# Accesare multiplă
print(obj2[['d', 'c', 'a']])

# Slicing
print(obj2[:2])     # Primele 2 elemente
print(obj2.a)       # Accesare ca atribut
```

### 🔄 Series din Dicționar

```python
# Crearea direct din dicționar
obj3 = Series({'d': 4, 'b': 7, 'a': -5, 'c': 3})
print(obj3)

# Operații matematice
print(obj3 ** 2)    # Ridicare la putere
print('b' in obj3)  # Verificare existență
```

### 🔍 Gestionarea Valorilor Lipsă

```python
# Auto-alinierea în Pandas
sdata = {'Texas': 10, 'Ohio': 20, 'Oregon': 15, 'Utah': 18}
states = ['Texas', 'Ohio', 'Oregon', 'Iowa']
obj4 = Series(sdata, index=states)

print(obj4)
# Texas     10.0
# Ohio      20.0
# Oregon    15.0
# Iowa       NaN

# Verificarea valorilor lipsă
print(pd.isnull(obj4))   # Boolean array cu True pentru NaN
print(pd.notnull(obj4))  # Invers
print(obj4[obj4.notnull()])  # Doar valorile non-NaN
```

### 🏷️ Numele Series și Index

```python
obj4.name = 'population'
obj4.index.name = 'state'
print(obj4)
# state
# Texas     10.0
# Ohio      20.0
# Oregon    15.0
# Iowa       NaN
# Name: population, dtype: float64

# Schimbarea indexului (obiectul index este imutabil)
obj4.index = ['Florida', 'New York', 'Kentucky', 'Georgia']
# obj4.index[2] = 'California'  # EROARE! Index-ul este imutabil
```

### 🎯 Indexarea și Filtrarea Series

```python
S = Series(range(4), index=['zero', 'one', 'two', 'three'])

# Indexare cu etichete
print(S['two'])              # 2
print(S[['zero', 'two']])    # Multiple etichete

# Indexare cu poziții
print(S[[0, 2]])             # Poziții numerice

# Slicing
print(S[:2])                 # Primele 2
print(S['zero':'two'])       # Slice cu etichete
print(S[S > 1])             # Filtrare condiționată
print(S[-2:])               # Ultimele 2
```

---

## 📋 Pandas DataFrame

### 📖 Ce este un DataFrame?

**DataFrame** este o structură de date tabulară compusă din rânduri și coloane, asemănătoare cu:
- Un tabel de spreadsheet sau de bază de date
- O colecție ordonată de coloane
- Fiecare coloană poate fi de un tip de date diferit
- Are atât indici de rânduri, cât și de coloane

### 🔧 Crearea unui DataFrame

#### **1. Din dicționar**
```python
from pandas import DataFrame
import pandas as pd

data = {
    'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
    'year': [2000, 2001, 2002, 2001, 2002],
    'pop': [1.5, 1.7, 3.6, 2.4, 2.9]
}

frame = DataFrame(data)
print(frame)
#     state  year  pop
# 0    Ohio  2000  1.5
# 1    Ohio  2001  1.7
# 2    Ohio  2002  3.6
# 3  Nevada  2001  2.4
# 4  Nevada  2002  2.9
```

#### **2. Cu ordine și index personalizat**
```python
frame2 = DataFrame(data, 
                   columns=['year', 'state', 'pop', 'debt'], 
                   index=['A', 'B', 'C', 'D', 'E'])
print(frame2)
#    year   state  pop debt
# A  2000    Ohio  1.5  NaN
# B  2001    Ohio  1.7  NaN
# C  2002    Ohio  3.6  NaN
# D  2001  Nevada  2.4  NaN
# E  2002  Nevada  2.9  NaN
```

#### **3. Din dicționare imbricate**
```python
pop = {
    'Nevada': {2001: 2.9, 2002: 2.9},
    'Ohio': {2002: 3.6, 2001: 1.7, 2000: 1.5}
}
frame3 = DataFrame(pop)
print(frame3)
#       Nevada  Ohio
# 2001     2.9   1.7
# 2002     2.9   3.6
# 2000     NaN   1.5

# Transpunerea
print(frame3.T)  # Schimbă rândurile cu coloanele
```

### 🔍 Proprietățile DataFrame

```python
# Accesarea proprietăților
frame3.index.name = 'year'
frame3.columns.name = 'state'

print(frame3.index)    # Index-ul rândurilor
print(frame3.columns)  # Index-ul coloanelor
print(frame3.values)   # Valorile ca array NumPy
print(type(frame3.values))  # <class 'numpy.ndarray'>
```

### 📊 Extragerea Datelor din DataFrame

#### **1. Extragerea coloanelor**
```python
# O coloană ca Series
print(frame['state'])
print(frame.state)     # Accesare ca atribut

# Multiple coloane
print(frame[['state', 'pop']])
```

#### **2. Indexarea cu loc și iloc**
```python
# loc - indexare cu etichete
print(frame2.loc[['A', 'B']])              # Rânduri specifice
print(frame2.loc['A'])                     # Un rând
print(frame2.loc['A':'E', ['state', 'pop']]) # Slice cu coloane

# iloc - indexare cu poziții
print(frame2.iloc[1:3])      # Rânduri 1-2
print(frame2.iloc[:, 1:3])   # Toate rândurile, coloanele 1-2
```

#### **3. Indexarea complexă**
```python
import numpy as np

data = np.arange(9).reshape(3, 3)
frame = DataFrame(data, 
                 index=['r1', 'r2', 'r3'], 
                 columns=['c1', 'c2', 'c3'])

# Diverse metode de indexare
print(frame['c1'])                    # O coloană
print(frame[['c1', 'c3']])           # Multiple coloane
print(frame.loc['r1'])               # Un rând
print(frame['c1']['r1'])             # Element specific
print(frame.loc[['r1', 'r3']])       # Multiple rânduri
print(frame.iloc[:2])                # Primele 2 rânduri
print(frame[:2])                     # Același lucru
```

#### **4. Indexarea cu condiții**
```python
# Filtrarea cu condiții
print(frame < 3)                     # Boolean DataFrame
print(frame[frame['c1'] > 0])        # Rânduri care satisfac condiția

# Modificarea cu condiții
frame[frame < 3] = 3                 # Înlocuire condițională
```

### ✏️ Modificarea DataFrame-urilor

#### **1. Modificarea coloanelor**
```python
# Setarea unei coloane cu valoare constantă
frame2['debt'] = 0

# Setarea cu array
frame2['debt'] = range(5)

# Setarea cu Series (auto-aliniere)
val = Series([10, 10, 10], index=['A', 'C', 'D'])
frame2['debt'] = val
# Doar index-urile care se potrivesc sunt setate
```

#### **2. Ștergerea coloanelor și rândurilor**
```python
# Ștergerea unei coloane
del frame2['debt']

# Ștergerea cu drop() - nu modifică original
print(frame.drop(['r1']))              # Șterge rândul r1
print(frame.drop(['r1', 'r3']))        # Șterge multiple rânduri
print(frame.drop(['c1'], axis=1))      # Șterge coloana c1
```

### 🔄 Reindexarea

```python
# Schimbarea ordinii rândurilor/coloanelor
frame2 = frame.reindex(['r1', 'r3', 'r2', 'r4'])    # Rânduri noi
frame2 = frame.reindex(columns=['c2', 'c1', 'c3'])  # Coloane noi
```

### 🎭 Aplicarea Funcțiilor

#### **1. Funcții pe elemente**
```python
# applymap - pe fiecare element
def square(x):
    return x ** 2

print(frame.applymap(square))
```

#### **2. Funcții pe rânduri/coloane**
```python
# apply - pe rânduri sau coloane
def max_minus_min(x):
    return max(x) - min(x)

print(frame.apply(max_minus_min, axis=1))  # Pe rânduri

# Funcție care returnează Series
def max_min(x):
    return Series([max(x), min(x)], index=['max', 'min'])

print(frame.apply(max_min))  # Pe coloane (implicit)
```

### 📈 Funcții Statistice

```python
# Funcții statistice incorporate
print(frame.mean())         # Media pe coloane
print(frame.sum())          # Suma pe coloane
print(frame.cumsum())       # Suma cumulativă
print(frame.describe())     # Statistici descriptive

# Pentru date numerice: mean, std, max, min, 25%, 50%, 75%
# Pentru date non-numerice: count, unique, most-frequent item
```

### 🔄 Sortarea

```python
# Sortarea după index
print(frame.sort_index())           # Sortare rânduri
print(frame.sort_index(axis=1))     # Sortare coloane

# Sortarea după valori
frame_random = DataFrame(np.random.randint(0, 10, 9).reshape(3, -1), 
                        index=['r1', 'r2', 'r3'], 
                        columns=['c1', 'c2', 'c3'])
                        
print(frame_random.sort_values(by='c1'))              # După o coloană
print(frame_random.sort_values(axis=1, by=['r3', 'r1'])) # După rânduri
```

### 🚫 Gestionarea Valorilor Lipsă

#### **1. Detectarea valorilor lipsă**
```python
from numpy import nan as NaN

data = Series([1, NaN, 2.5, NaN, 6])
print(data.notnull())    # Boolean Series
print(data[data.notnull()])  # Doar valorile valide
print(data.dropna())     # Elimină NaN-urile
```

#### **2. Gestionarea în DataFrame**
```python
data = DataFrame([[1, 2, 3], [1, NaN, NaN], [NaN, NaN, NaN], [NaN, 4, 5]])

print(data.dropna())              # Elimină rândurile cu orice NaN
print(data.dropna(how='all'))     # Elimină doar rândurile cu toate NaN
print(data.dropna(axis=1, how='all'))  # Elimină coloanele cu toate NaN
```

#### **3. Completarea valorilor lipsă**
```python
# Completare cu valoare constantă
print(data.fillna(0))

# Completare cu media coloanei
print(data.fillna(data.mean(skipna=True)))

# Modificarea în loc
data.fillna(0, inplace=True)  # Modifică DataFrame-ul original
```

---

## 🎯 Exerciții Practice

### 📊 Exercițiul 1: Analiza Datelor cu NumPy

```python
import numpy as np

# 1. Creați un array 2D cu forme geometrice
geometry_data = np.random.randint(1, 100, (5, 3))  # 5 forme, 3 dimensiuni
print("Date geometrice:", geometry_data)

# 2. Calculați aria pentru fiecare formă (presupunem dreptunghiuri)
areas = geometry_data[:, 0] * geometry_data[:, 1]  # lungime * lățime
print("Arii:", areas)

# 3. Găsiți forma cu aria maximă
max_area_index = np.argmax(areas)
print(f"Forma cu aria maximă: {max_area_index}, Aria: {areas[max_area_index]}")

# 4. Calculați statistici
print(f"Aria medie: {np.mean(areas):.2f}")
print(f"Aria mediană: {np.median(areas):.2f}")
print(f"Deviația standard: {np.std(areas):.2f}")
```

### 📋 Exercițiul 2: Analiza Vânzărilor cu Pandas

```python
import pandas as pd
import numpy as np

# 1. Creați un DataFrame cu date de vânzări
np.random.seed(42)  # Pentru rezultate reproductibile

sales_data = {
    'Produs': ['Laptop', 'Mouse', 'Tastatură', 'Monitor', 'Webcam'] * 4,
    'Luna': ['Ian', 'Ian', 'Ian', 'Ian', 'Ian',
             'Feb', 'Feb', 'Feb', 'Feb', 'Feb',
             'Mar', 'Mar', 'Mar', 'Mar', 'Mar',
             'Apr', 'Apr', 'Apr', 'Apr', 'Apr'],
    'Vanzari': np.random.randint(10, 100, 20),
    'Pret_unitar': [2500, 50, 150, 800, 200] * 4
}

df_sales = pd.DataFrame(sales_data)
df_sales['Venit_total'] = df_sales['Vanzari'] * df_sales['Pret_unitar']

print("DataFrame Vânzări:")
print(df_sales.head(10))

# 2. Analiză statistică
print("\n=== ANALIZĂ STATISTICĂ ===")
print("Statistici descriptive pentru vânzări:")
print(df_sales['Vanzari'].describe())

print("\nVenitul total pe produs:")
venit_pe_produs = df_sales.groupby('Produs')['Venit_total'].sum()
print(venit_pe_produs.sort_values(ascending=False))

print("\nVânzările medii pe lună:")
vanzari_pe_luna = df_sales.groupby('Luna')['Vanzari'].mean()
print(vanzari_pe_luna)

# 3. Filtrarea datelor
print("\n=== FILTRARE ===")
vanzari_mari = df_sales[df_sales['Vanzari'] > 50]
print(f"Produse cu vânzări > 50 unități: {len(vanzari_mari)} înregistrări")

# Produsele cu venitul cel mai mare
top_venit = df_sales.nlargest(5, 'Venit_total')
print("\nTop 5 vânzări după venit:")
print(top_venit[['Produs', 'Luna', 'Venit_total']])
```

### 🔍 Exercițiul 3: Curățarea și Prelucrarea Datelor

```python
import pandas as pd
import numpy as np

# 1. Creați date cu valori lipsă
data_dirty = {
    'Nume': ['Ana', 'Bob', 'Carol', None, 'Eve'],
    'Vârsta': [25, None, 30, 35, 28],
    'Salariu': [50000, 60000, None, 70000, 55000],
    'Departament': ['IT', 'HR', 'IT', 'Finance', None]
}

df_dirty = pd.DataFrame(data_dirty)
print("Date originale (cu probleme):")
print(df_dirty)
print("\nInformații despre valorile lipsă:")
print(df_dirty.isnull().sum())

# 2. Curățarea datelor
df_clean = df_dirty.copy()

# Completarea valorilor lipsă
df_clean['Nume'].fillna('Necunoscut', inplace=True)
df_clean['Vârsta'].fillna(df_clean['Vârsta'].mean(), inplace=True)
df_clean['Salariu'].fillna(df_clean['Salariu'].median(), inplace=True)
df_clean['Departament'].fillna('General', inplace=True)

print("\n=== DATE CURĂȚATE ===")
print(df_clean)

# 3. Analiză după curățare
print("\n=== ANALIZĂ FINALĂ ===")
print("Salariul mediu pe departament:")
print(df_clean.groupby('Departament')['Salariu'].mean())

print("\nVârsta medie pe departament:")
print(df_clean.groupby('Departament')['Vârsta'].mean())

# 4. Operații avansate
df_clean['Salariu_categorie'] = pd.cut(df_clean['Salariu'], 
                                      bins=[0, 55000, 65000, float('inf')], 
                                      labels=['Mic', 'Mediu', 'Mare'])
print("\nDistribuția categoriilor de salariu:")
print(df_clean['Salariu_categorie'].value_counts())
```

---

## 💡 Sfaturi și Bune Practici

### 🎯 NumPy - Bune Practici

1. **Folosiți vectorizarea** în loc de bucle:
```python
# ❌ GREȘIT
result = []
for x in array:
    result.append(x ** 2)

# ✅ CORECT
result = array ** 2
```

2. **Specificați tipul de date** când este posibil:
```python
# Eficient pentru memorie
arr = np.array([1, 2, 3], dtype=np.int32)
```

3. **Folosiți funcții NumPy** pentru operații matematice:
```python
# ✅ CORECT - rapid și eficient
mean_value = np.mean(array)
max_value = np.max(array)
```

### 🐼 Pandas - Bune Practici

1. **Verificați mereu datele** după încărcare:
```python
print(df.head())          # Primele rânduri
print(df.info())          # Informații generale
print(df.describe())      # Statistici descriptive
print(df.isnull().sum())  # Valorile lipsă
```

2. **Folosiți indexarea eficientă**:
```python
# ✅ CORECT pentru condiții multiple
mask = (df['age'] > 25) & (df['salary'] > 50000)
result = df[mask]

# ✅ CORECT pentru selecție de coloane
columns_needed = ['name', 'age', 'salary']
df_subset = df[columns_needed]
```

3. **Gestionați valorile lipsă** corespunzător:
```python
# Pentru date numerice
df['numeric_col'].fillna(df['numeric_col'].mean())

# Pentru date categorice
df['category_col'].fillna(df['category_col'].mode()[0])
```

### ⚡ Optimizarea Performanței

1. **Utilizați metode vectorizate** Pandas:
```python
# ❌ GREȘIT - lent
df['new_col'] = df.apply(lambda x: x['col1'] + x['col2'], axis=1)

# ✅ CORECT - rapid
df['new_col'] = df['col1'] + df['col2']
```

2. **Folosiți tipuri de date optimizate**:
```python
# Optimizarea tipurilor de date
df['category_col'] = df['category_col'].astype('category')
df['int_col'] = df['int_col'].astype('int32')  # dacă valorile sunt mici
```

---

## 🎓 Recapitulare

### ✅ Ce am învățat:

**NumPy:**
- Crearea și manipularea array-urilor multidimensionale
- Operații vectorizate și avantajele performanței
- Indexarea, slicing-ul și operațiile matematice
- Diferențele fundamentale față de listele Python

**Pandas:**
- Structurile de date Series și DataFrame
- Încărcarea, manipularea și curățarea datelor
- Indexarea avansată cu loc și iloc
- Operații de grupare și agregare
- Gestionarea valorilor lipsă

### 🚀 Următorii Pași:
- **Lecția următoare:** Vizualizarea datelor cu Matplotlib și Seaborn
- **Aplicații practice:** Analiza seturilor de date reale
- **Pregătire pentru:** Machine Learning cu Scikit-learn

---

## 📚 Resurse Suplimentare

### 📖 Documentația Oficială
- [NumPy Documentation](https://numpy.org/doc/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)

### 🎯 Exerciții pentru Acasă

#### **Exercițiul 1: NumPy Array Operations**
```python
import numpy as np

# 1. Creați o matrice 4x4 cu numere aleatorii între 1-20
matrix = np.random.randint(1, 21, (4, 4))

# 2. Calculați suma pentru fiecare rând și coloană
# 3. Găsiți valoarea maximă și minimă
# 4. Înlocuiți toate valorile > 15 cu 0
# 5. Calculați media pentru întreaga matrice
```

#### **Exercițiul 2: Pandas Data Analysis**
```python
import pandas as pd
import numpy as np

# 1. Creați un DataFrame cu informații despre studenți:
#    - Nume, Vârstă, Nota_Matematică, Nota_Română, Nota_Engleză, Clasa
# 2. Calculați media generală pentru fiecare student
# 3. Găsiți studentul cu cea mai mare medie
# 4. Calculați media pe materii
# 5. Filtrați studenții cu media > 8.5
# 6. Grupați după clasă și calculați statistici
```

#### **Exercițiul 3: Real-world Data Cleaning**
```python
# Simulați un dataset "murdar" și curățați-l:
dirty_data = {
    'Produs': ['laptop', 'LAPTOP', 'Laptop', None, 'mouse'],
    'Preț': ['2500', '2600', None, '2550', 'invalid'],
    'Stoc': [10, -5, 15, None, 8],
    'Categorie': ['Electronics', 'electronics', 'ELECTRONICS', 'Tech', None]
}

# Sarcinile:
# 1. Standardizați numele produselor
# 2. Convertiți prețurile la numeric
# 3. Corectați valorile negative din stoc
# 4. Uniformizați categoriile
# 5. Completați valorile lipsă logic
```

### 🔧 Exerciții Practice Avansate

#### **Exercițiul 4: Simularea unui Magazin Online**
```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Simulați date pentru un magazin online
np.random.seed(42)

# Generați date pentru 1000 de comenzi
n_orders = 1000
start_date = datetime(2024, 1, 1)

# Datele de generat:
# - ID comandă, Data, Client, Produs, Cantitate, Preț unitar, Status

# Sarcinile de analiză:
# 1. Calculați venitul total pe lună
# 2. Găsiți top 10 clienți după valoarea comenzilor
# 3. Identificați produsele cu cele mai mari vânzări
# 4. Analizați tendințele sezoniere
# 5. Calculați rata de returnare (comenzi anulate)
```

#### **Exercițiul 5: Analiza Performanței Angajaților**
```python
# Creați un sistem de tracking pentru performanța angajaților
# Include: Nume, Departament, Proiecte finalizate, Ore lucrate, Rating, Salariu

# Analize de efectuat:
# 1. Productivitatea pe departament
# 2. Corelația între ore lucrate și rating
# 3. Analiza salariilor vs performanță
# 4. Identificarea angajaților cu performanță excepțională
# 5. Recomandări pentru măriri salariale
```

### 📊 Proiect Final de Modul

#### **Proiect: Analiza Datelor de Vânzări E-commerce**

**Obiectiv:** Analizați un dataset complex de vânzări online și extrageți insights actionabile.

**Date de simulat:**
- 10,000 de tranzacții
- 50 de produse în 5 categorii
- 1,000 de clienți unici
- Perioada: 12 luni
- Include: retur-uri, discount-uri, regiunea clientului

**Deliverabile:**
1. **Raport de curățare a datelor** - documentați problemele găsite și soluțiile
2. **Analiza descriptivă** - statistici generale, tendințe, patterns
3. **Analiza segmentării** - gruparea clienților, produselor, regiunilor
4. **Insights de business** - recomandări concrete pentru îmbunătățiri
5. **Cod Python documentat** - cu toate analizele efectuate

**Structura raportului:**
```markdown
# Analiza Datelor E-commerce - Raport Final

## 1. Rezumat Executiv
- Principalele descoperiri
- Recomandări cheie

## 2. Curățarea Datelor
- Probleme identificate
- Metodele de curățare aplicate
- Impactul asupra analizei

## 3. Analiza Explorativă
- Statistici descriptive
- Distribuții și tendințe
- Identificarea outlier-ilor

## 4. Segmentarea și Gruparea
- Analiza pe categorii de produse
- Segmentarea clienților
- Analiza geografică

## 5. Insights și Recomandări
- Descoperiri surprinzătoare
- Oportunități identificate
- Acțiuni recomandate
```

### 🎯 Criterii de Evaluare

**Proiectul va fi evaluat după:**
- **Curățarea datelor** (25%) - Identificarea și rezolvarea problemelor
- **Acuratețea analizei** (25%) - Corectitudinea calculelor și interpretărilor
- **Calitatea insights-urilor** (25%) - Relevanța și utilitatea descoperirilor
- **Prezentarea rezultatelor** (25%) - Claritatea raportului și organizarea codului

### 💻 Setup pentru Lucrul Acasă

#### **Instalarea bibliotecilor necesare:**
```bash
# Instalare prin pip
pip install numpy pandas matplotlib seaborn jupyter

# Sau prin conda
conda install numpy pandas matplotlib seaborn jupyter
```

#### **Template pentru începerea proiectelor:**
```python
# Template pentru proiecte NumPy/Pandas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Configurări pentru afișare
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 50)

# Setări pentru grafice (pentru lecțiile viitoare)
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

print("🐍 Mediul de lucru pentru NumPy și Pandas este gata!")
print("📊 Versiuni instalate:")
print(f"NumPy: {np.__version__}")
print(f"Pandas: {pd.__version__}")
```

### 🔗 Legături cu Lecțiile Viitoare

#### **Lecția 26 - Matplotlib și Seaborn:**
- Vizualizarea datelor create cu Pandas
- Grafice pentru explorarea datelor NumPy
- Storytelling cu date

#### **Lecția 27 - Streamlit:**
- Crearea aplicațiilor web interactive
- Dashboard-uri pentru analizele Pandas
- Prezentarea rezultatelor în timp real

#### **Lecția 28 - Machine Learning:**
- Pregătirea datelor cu Pandas pentru ML
- Feature engineering cu NumPy
- Pipeline-uri de procesare a datelor

---

## 🎯 Verificarea Cunoștințelor

### ❓ Întrebări de Autoevaluare

1. **Care sunt principalele avantaje ale NumPy față de listele Python?**
2. **Când folosim Series vs DataFrame în Pandas?**
3. **Ce înseamnă "vectorizarea" și de ce este importantă?**
4. **Cum gestionăm valorile lipsă într-un DataFrame?**
5. **Care este diferența între loc și iloc?**
6. **De ce array-urile NumPy returnează "view-uri" și nu copii?**
7. **Cum optimizăm performanța când lucrăm cu datasets mari?**

### 🧪 Test Rapid de Cunoștințe

```python
# Completați codul pentru a rezolva problemele:

import numpy as np
import pandas as pd

# 1. Creați un array NumPy 3x3 cu valori de la 1 la 9
arr = # COMPLETAȚI

# 2. Calculați suma pe fiecare coloană
col_sums = # COMPLETAȚI

# 3. Creați un DataFrame cu datele de mai sus
df = # COMPLETAȚI

# 4. Adăugați o coloană nouă care este suma rândurilor
df['row_sum'] = # COMPLETAȚI

# 5. Filtrați rândurile unde suma > 15
filtered_df = # COMPLETAȚI

# 6. Calculați media pentru întregul DataFrame
overall_mean = # COMPLETAȚI
```

**Răspunsuri:**
```python
# 1.
arr = np.arange(1, 10).reshape(3, 3)

# 2.
col_sums = np.sum(arr, axis=0)

# 3.
df = pd.DataFrame(arr, columns=['A', 'B', 'C'])

# 4.
df['row_sum'] = df.sum(axis=1)

# 5.
filtered_df = df[df['row_sum'] > 15]

# 6.
overall_mean = df.select_dtypes(include=[np.number]).mean().mean()
```

---

## 🎉 Încheierea Lecției

Felicitări! Ați completat cu succes introducerea în NumPy și Pandas - două dintre cele mai importante biblioteci pentru Data Science în Python. 

**Ce urmează:**
- Practicați exercițiile propuse
- Începeți lucrul la proiectul final
- Pregătiți-vă pentru lecția despre vizualizarea datelor

**Resurse pentru continuarea învățării:**
- Kaggle Learn - Pandas Course
- DataCamp - NumPy și Pandas tracks
- Real Python - Pandas și NumPy tutorials

**💡 Sfat final:** Cea mai bună modalitate de a învăța NumPy și Pandas este să lucrați cu date reale. Căutați dataset-uri interessante pe Kaggle, UCI ML Repository sau datele deschise ale guvernului și începeți să explorați!

---

*Lecția 25 completă - NumPy și Pandas pentru Prelucrarea Datelor*
*Python Fundamentals - Modul 7: Librării Externe Python*
*© 2024 Tekwill Academy*
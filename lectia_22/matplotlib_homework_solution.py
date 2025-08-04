# Ghid pentru Profesori - Matplotlib și Git

"""
🎯 GHID PENTRU EVALUARE:
Acest fișier conține explicații detaliate pentru profesori despre ce trebuie să facă studenții.

📋 CRITERII DE EVALUARE:
1. Setup corect (25 puncte)
2. Implementare funcții (50 puncte)
3. Git workflow (25 puncte)
"""

# ===============================
# 1. SETUP CORECT (25 puncte)
# ===============================

"""
VERIFICĂ CĂ STUDENTUL A FĂCUT:

✅ Repo GitHub creat cu numele "my-matplotlib-project"
✅ Repo clonat local
✅ Virtual environment creat (.venv folder există)
✅ Matplotlib instalat (verifică cu pip list)
✅ requirements.txt generat și conține matplotlib

PUNCTAJ:
- 5p: Repo GitHub creat
- 5p: Repo clonat local  
- 5p: Virtual environment creat
- 5p: Matplotlib instalat
- 5p: requirements.txt generat
"""

# ===============================
# 2. IMPLEMENTARE FUNCȚII (50 puncte)
# ===============================

"""
FUNCȚIA create_line_plot() (12.5 puncte):
✅ plt.figure(figsize=(8, 6)) - creează figura
✅ plt.plot() cu parametrii corecți (x, y, color, marker, linewidth, markersize)
✅ plt.title(), plt.xlabel(), plt.ylabel() cu text și formatare
✅ plt.grid(True) activat
✅ plt.savefig() și plt.show() funcționează
✅ Fișierul line_plot.png este generat

FUNCȚIA create_bar_plot() (12.5 puncte):
✅ plt.figure(figsize=(8, 6)) - creează figura
✅ plt.bar() cu categories, values, culori multiple, alpha
✅ plt.title(), plt.xlabel(), plt.ylabel() corecte
✅ plt.grid(True, axis='y') pentru grid vertical
✅ plt.savefig() și plt.show() funcționează
✅ Fișierul bar_plot.png este generat

FUNCȚIA create_scatter_plot() (12.5 puncte):
✅ plt.figure(figsize=(8, 6)) - creează figura
✅ plt.scatter() cu x, y, culoare, alpha, dimensiune puncte
✅ plt.title(), plt.xlabel(), plt.ylabel() corecte
✅ plt.grid(True) activat
✅ plt.savefig() și plt.show() funcționează
✅ Fișierul scatter_plot.png este generat

FUNCȚIA create_subplot() (12.5 puncte):
✅ plt.subplots(2, 2, figsize=(12, 10)) - creează subplot
✅ axes[0, 0].plot() pentru grafic cu linii
✅ axes[0, 1].bar() pentru grafic cu bare
✅ axes[1, 0].scatter() pentru grafic cu puncte
✅ axes[1, 1].pie() pentru pie chart
✅ Toate subplot-urile au titluri și grid
✅ plt.tight_layout() pentru spațiere
✅ plt.savefig() și plt.show() funcționează
✅ Fișierul subplot.png este generat
"""

# ===============================
# 3. GIT WORKFLOW (25 puncte)
# ===============================

"""
VERIFICĂ CĂ STUDENTUL A FĂCUT:

✅ git add . - adaugă fișierele
✅ git commit -m "mesaj relevant" - commit cu mesaj
✅ git push origin main - push pe GitHub
✅ Toate fișierele sunt vizibile pe GitHub:
   - matplotlib_homework.py (codul completat)
   - requirements.txt
   - line_plot.png
   - bar_plot.png
   - scatter_plot.png
   - subplot.png

PUNCTAJ:
- 5p: Fișierele .py și requirements.txt pe GitHub
- 5p: Imaginile PNG pe GitHub
- 5p: Commit cu mesaj relevant
- 10p: Repo organizat și funcțional pe GitHub
"""

# ===============================
# 4. CRITERII BONUS (10 puncte)
# ===============================

"""
PUNCTE BONUS PENTRU:
✅ Formatare frumoasă a graficelor (culori, fonturi)
✅ Cod organizat și comentat
✅ Gestionarea erorilor
✅ Funcții suplimentare (histogram, alte tipuri de grafice)
✅ README.md în repo cu descrierea proiectului
✅ .gitignore pentru .venv și __pycache__
"""

# ===============================
# 5. ERORI COMUNE DE VERIFICAT
# ===============================

"""
PROBLEME FRECVENTE:

❌ Virtual environment nu este activat
   - Verifică că (venv) apare în terminal
   - pip list să arate matplotlib instalat local

❌ Matplotlib nu este instalat
   - ImportError: No module named 'matplotlib'
   - Soluție: pip install matplotlib

❌ Graficele nu se salvează
   - Verifică că plt.savefig() este apelat
   - Verifică că fișierele PNG există în folder

❌ Subplots nu funcționează
   - Verifică sintaxa: fig, axes = plt.subplots(2, 2)
   - Verifică indexarea: axes[0, 0], axes[0, 1], etc.

❌ Git push nu funcționează
   - Verifică că repo-ul este clonat corect
   - Verifică că studentul este logat în Git
   - Verifică că branch-ul este main (nu master)

❌ Requirements.txt este gol
   - Verifică că virtual environment este activat
   - pip freeze > requirements.txt în directorul corect
"""

# ===============================
# 6. RESURSE PENTRU STUDENȚI
# ===============================

"""
DACĂ STUDENȚII AU PROBLEME, ÎNDREAPTĂ-I CĂTRE:

📖 Matplotlib Tutorial:
https://www.w3schools.com/python/matplotlib_intro.asp

📖 Plot Types:
https://www.w3schools.com/python/matplotlib_plotting.asp

📖 Customization:
https://www.w3schools.com/python/matplotlib_labels.asp

📖 Subplots:
https://www.w3schools.com/python/matplotlib_subplot.asp

📖 Git Basics:
https://www.w3schools.com/git/

📖 Virtual Environments:
https://docs.python.org/3/tutorial/venv.html
"""

# ===============================
# 7. FEEDBACK CONSTRUCTIV
# ===============================

"""
EXEMPLE DE FEEDBACK POZITIV:

✅ "Excelent! Toate graficele sunt create corect și au formatare frumoasă."
✅ "Bună treabă cu git workflow-ul. Repo-ul este organizat perfect."
✅ "Îmi place cum ai personalizat culorile și markerele."

EXEMPLE DE FEEDBACK PENTRU ÎMBUNĂTĂȚIRE:

📝 "Graficele funcționează, dar încearcă să adaugi mai multe detalii la formatare."
📝 "Virtual environment nu pare să fie folosit corect. Verifică instalarea."
📝 "Lipsesc câteva fișiere PNG din repo. Verifică că plt.savefig() funcționează."
"""

print("📊 Ghid pentru evaluarea temei de matplotlib completat!")
print("📋 Acest fișier ajută profesorii să evalueze corect tema studenților.")
print("🎯 Criteriile acoperă setup, implementare, și git workflow.")
print("✅ Studenții vor învăța matplotlib, git, și virtual environments!")
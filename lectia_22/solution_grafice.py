"""
Soluție Start Task - Virtual Environment și Matplotlib
Creează 4 grafice diferite într-un subplot 2x2
"""

import matplotlib.pyplot as plt
import numpy as np

# Crearea figurii cu 4 subplot-uri
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Graficul 1 - Line Plot (sus stânga)
x = list(range(1, 11))  # 1 la 10
y = [i**2 for i in x]   # pătratele numerelor
axes[0, 0].plot(x, y, color='blue', marker='o')
axes[0, 0].set_title('Funcția x²')
axes[0, 0].set_xlabel('x')
axes[0, 0].set_ylabel('x²')
axes[0, 0].grid(True, alpha=0.3)

# Graficul 2 - Pie Chart (sus dreapta)
limbaje = ['Python', 'JavaScript', 'Java', 'C++']
popularitate = [35, 25, 20, 20]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

axes[0, 1].pie(popularitate, labels=limbaje, autopct='%1.1f%%', 
               colors=colors, startangle=90)
axes[0, 1].set_title('Popularitatea Limbajelor')

# Graficul 3 - Histogram (jos stânga)
note = [7, 8, 9, 7, 6, 8, 9, 10, 7, 8, 9, 6, 7, 8, 9, 10]
axes[1, 0].hist(note, bins=5, color='green', alpha=0.7, edgecolor='black')
axes[1, 0].set_title('Distribuția Notelor')
axes[1, 0].set_xlabel('Note')
axes[1, 0].set_ylabel('Frecvența')

# Graficul 4 - Bar Chart (jos dreapta)
luni = ['Ian', 'Feb', 'Mar', 'Apr', 'Mai']
temperaturi = [2, 5, 12, 18, 25]
axes[1, 1].bar(luni, temperaturi, color='orange', alpha=0.8)
axes[1, 1].set_title('Temperatura Medie pe Luni')
axes[1, 1].set_xlabel('Luni')
axes[1, 1].set_ylabel('Temperatura (°C)')

# Ajustarea layout-ului pentru a evita suprapunerea
plt.tight_layout()

# Afișarea graficelor
plt.show()

print("📊 Graficele au fost create cu succes!")
print("🎯 Task completat!")

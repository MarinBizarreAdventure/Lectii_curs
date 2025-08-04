# REZOLVAREA SARCINII - NumPy și Pandas (10 minute)
# Analiza temperaturilor săptămânii

import numpy as np
import pandas as pd

print("🌡️ ANALIZA TEMPERATURILOR SĂPTĂMÂNII")
print("=" * 40)

# 1. CREEAZĂ ARRAY-UL CU TEMPERATURI
temperature = np.array([22, 25, 18, 20, 23, 27, 24])
print("📊 Temperaturile săptămânii:", temperature)

# 2. CALCULEAZĂ CU NumPy
temp_medie = np.mean(temperature)
temp_maxima = np.max(temperature)
temp_minima = np.min(temperature)
zile_calde = np.sum(temperature > 23)  # Câte zile peste 23°C

print(f"\n📈 STATISTICI NumPy:")
print(f"   🌡️  Temperatura medie: {temp_medie:.1f}°C")
print(f"   🔥 Temperatura maximă: {temp_maxima}°C")
print(f"   🧊 Temperatura minimă: {temp_minima}°C")
print(f"   ☀️  Zile calde (>23°C): {zile_calde}")

# 3. CREEAZĂ DATAFRAME-UL PANDAS
zilele_saptamanii = ['Luni', 'Marți', 'Miercuri', 'Joi', 'Vineri', 'Sâmbătă', 'Duminică']

# Creează DataFrame-ul
df_vremea = pd.DataFrame({
    'Ziua': zilele_saptamanii,
    'Temperatura': temperature
})

# Adaugă coloana cu categoria (Cald/Răcoros)
df_vremea['Categorie'] = df_vremea['Temperatura'].apply(
    lambda x: 'Cald' if x > 23 else 'Răcoros'
)

# 4. AFIȘEAZĂ REZULTATELE
print(f"\n📋 DATAFRAME COMPLET:")
print(df_vremea)

print(f"\n🔥 DOAR ZILELE CALDE:")
zile_calde_df = df_vremea[df_vremea['Categorie'] == 'Cald']
print(zile_calde_df)

print(f"\n📊 TEMPERATURA MEDIE (cu Pandas): {df_vremea['Temperatura'].mean():.1f}°C")

# BONUS - Statistici suplimentare
print(f"\n🎯 STATISTICI BONUS:")
print(f"   📅 Cea mai caldă zi: {df_vremea.loc[df_vremea['Temperatura'].idxmax(), 'Ziua']}")
print(f"   📅 Cea mai rece zi: {df_vremea.loc[df_vremea['Temperatura'].idxmin(), 'Ziua']}")
print(f"   🌡️  Variația temperaturii: {temp_maxima - temp_minima}°C")

print(f"\n✅ Sarcina completată cu succes! 🎉")

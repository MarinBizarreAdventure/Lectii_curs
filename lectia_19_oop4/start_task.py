
# ### 🧪 **Exercițiu de evaluare: Relația dintre Mașină, Motor și Șofer**

# #### Cerință:

# Creează următoarele clase:

# 1. **Clasa `Motor`**

#    * Atribut **privat**: `putere` (în cai putere)
#    * Metodă **publică**: `descrie_motor()` → returnează un string cu puterea motorului

class Motor:
   def __init__(self, putere):
        self.__putere = putere

   def descrie_motor(self):
       return f" motorul are puterea de {self.__putere} CP"

# 2. **Clasa `Sofer`**

#    * Atribut **public**: `nume`
#    * Metodă **privată**: `__verifica_permis()` → returnează `True`
#    * Metodă **publică**: `poate_conduce()` → folosește metoda `__verifica_permis()`

class Sofer:
   def __init__(self, nume):
        self.nume = nume

   def __verifica_permis(self):
       return True
   
   def poate_conduce(self):
      return self.__verifica_permis()
      

# 3. **Clasa `Masina`**

#    * **Agregare**: primește un obiect de tip `Sofer` ca parametru în constructor
#    * **Compoziție**: creează în constructor un obiect de tip `Motor`
#    * Atribut **privat**: `__marca`
#    * Metodă **publică**: `porneste()` → verifică dacă șoferul poate conduce și afișează un mesaj cu marca și puterea motorului


class Masina:
   def __init__(self, marca, sofer):
        self.sofer = sofer
        self.__marca = marca 
        self.motor = Motor(100)

   def porneste(self):
       if self.sofer.poate_conduce():
           print(f"masina de marca {self.__marca} cu soferul {self.sofer.nume} si cu motorul {self.motor.descrie_motor()}")
       else:
           print("soferul nu poate conduce")
# #### Exemplu de utilizare:

# ```python
sofer = Sofer("Maria")
masina = Masina("Dacia", sofer)
masina.porneste()
# ```

# ### ✅ Ce trebuie să conțină testul:

# * Folosirea **atributelor private** (`__marca`, `__verifica_permis`)
# * Utilizarea **metodelor publice/private**
# * Demonstrarea **compoziției** (`Masina` creează `Motor`)
# * Demonstrarea **agregării** (`Masina` primește un `Sofer`)
# * Verificare logică simplă în metoda `porneste()`


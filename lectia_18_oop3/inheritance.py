"""
Cerință:
Creați un sistem de gestionare a animalelor de companie folosind programarea orientată pe obiecte.

1. Clasa de bază Animal:
Trebuie să aibă un constructor (init) care primește:
- name (string): numele animalului
- age (int): vârsta animalului în ani

Trebuie să aibă metodele:
- get_name(): returnează numele animalului
- speak(): metodă care returneaza "Sunet generic de animal"


2. Clasele derivate trebuie să includă:
a) Clasa Dog:
    Moștenește din Animal constructor cu parametrii:
    - name (string)
    - age (int)
    * breed (string): rasa câinelui
    * is_guard_dog (boolean): dacă este câine de pază

    
b) Clasa Cat:
    Moștenește din Animal constructor cu parametrii:
    - name (string)
    - age (int)
    * color (string): culoarea blănii
    * indoor (boolean): dacă este pisică de interior
    

c) Clasa Parrot:
    Moștenește din Animal constructor cu parametrii:
    - name (string)
    - age (int)
    * can_speak_words (boolean): dacă poate vorbi cuvinte
    * favorite_phrase (string): fraza favorită (dacă poate vorbi)

- Toate clasele derivate trebuie să folosească super().init() pentru a initializa atributele din clasa părinte
- Trebuie să fie posibilă crearea unei liste cu diferite tipuri de animale și apelarea metodei speak() 
  pentru fiecare
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return f" My name is {self.name}"
    @abstractmethod
    def speak(self):
        pass
    

class Dog(Animal):
    def __init__(self, name, age,breed, is_guard_dog):
        super().__init__(name, age)        
        self.breed = breed
        self.is_guard_dog = is_guard_dog
    
    def speak(self):
        return f"Im a good boy named {self.name} and my breed is {self.breed} and {"a guard dog" if self.is_guard_dog else "simple dog"}"
    

class Cat(Animal):
    def __init__(self, name, age, color, indoor):
        super().__init__(name, age)
        self.color =color
        self.indoor = indoor
    
    def speak(self):
        return f"im a cat and my name is {self.name} and my color is {self.color}"
    


class Parrot(Animal):
    def __init__(self, name, age, can_speak_words, favorite_phrase):
        super().__init__(name, age)
        self.can_speak_words = can_speak_words
        self.favorite_phrase = favorite_phrase
    
    def speak(self):
        return f"im a prrot and my favorite phrase is {self.favorite_phrase}"


animal = Animal("animal", 8)

print(animal.speak())
dog = Dog("Rex", "LONDRA","Labrador", False)
cat = Cat("Garfild", 4,"orange",True)
parrot = Parrot("RICO", 1,True, "Hello world")

animals = [dog, cat, parrot]

for animal in animals:

    print(animal.speak())
    print(animal.get_name())


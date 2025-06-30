
def decorator_continuu(func):
    def wrapper():
        while True:
            func()
            exit = input("vrei sa coninui? Y/n")
            if exit == "n":
                break
                
    return wrapper

def decorator_input(func):
    def wrapper():
        a = input("introduceti primul numar:")
        b = input("introduceti al doilea numar:")
        rezutlat = func(a,b)
        print(f"rezultatul primit de la functia noastra este {rezutlat}")

    return wrapper

def decorator_validare(funct):
    def wrapper(a, b):
        suma = 0
        try:
            a, b = int(a), int(b)
            suma = funct(a,b)
        except ValueError:
            print("inputul trebuie sa fie numar valid!!!!!")

        return suma  
    return wrapper

@decorator_continuu
@decorator_input
@decorator_validare
def suma(a, b):
    print(f"suma numerelor este {a+b}")
    return a+b 


suma()

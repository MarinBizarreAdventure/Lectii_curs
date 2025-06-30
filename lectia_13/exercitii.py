def calculator_avansat(operatie):
    def adunare(a,b):
        return a+b
    
    def scadere(a,b):
        return a-b
    
    def inmultire(a,b):
        return a*b
    
    operatii = {
        '+' : adunare,
        "-" : scadere,
        "*" : inmultire,
    }

    if operatie in operatii:
        return operatii[operatie]
    else:
        return lambda a,b : a,b
    


lista = []
def press_button(x):
    lista.append(x)
    return lista


print(press_button(10))
print(press_button(19))

def creare_butoane():
    lista = []
    def press_button(x):
        lista.append(x)
        return lista
    
    return press_button


button1 = creare_butoane()
button2 = creare_butoane()


button1(5)
button1(6)
button1(7)
print(button1(11))
print(button2(1))

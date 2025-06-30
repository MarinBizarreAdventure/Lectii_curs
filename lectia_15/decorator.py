
def decorator_extern(func):
    def wrapper(*args, **kwargs):
        print("decorator extern start")
        rezultat = func(*args,**kwargs)
        print("decorator extern stop")
        return rezultat
    return wrapper


def decorator_intern(func):
    def wrapper(*args, **kwargs):
        print(f"decorator intern start")
        rezultat = func(*args, **kwargs)
        print(f"decorator intern stop")
        return rezultat

    return wrapper

@decorator_extern
@decorator_intern
def functie():
    print("functia originala")
    return 'Gata'


functie()






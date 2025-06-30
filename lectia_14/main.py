def hello_solar_system(old_function):
    def wrapper(planet=None):
        print("hello solar system")
        old_function(planet)
        print("goodbye solar system")
    return wrapper

def hello_galaxy(old_function):
    def wrapper(planet=None):
        print("hello milky way galaxy!")
        old_function(planet)
    return wrapper

@hello_galaxy
@hello_solar_system
def hello(planet = None):
    if planet == None:
        print("hello world")
        return
    print(f"hello {planet}")


hello_wrapped = hello

hello_wrapped = hello_solar_system(hello)


hello_wrapped = hello_galaxy(hello_solar_system(hello))
hello_wrapped = hello_galaxy(hello_wrapped)
hello_wrapped("jupiter")



# hello = hello_solar_system(hello)
# hello_wrapped()
# hello("jupiter")
# decorator_simplu = hello_solar_system(hello)
# decorator_simplu("mars")



class Masina:
    def __init__(self, marca, putere):
        self.marca = marca
        self.motor = Motor(putere)

    
    def porneste(self):
        return f"masina porneste motorul cu puterea {self.motor.putere} hp"
    

class Motor:
    def __init__(self, putere):
        self.putere = putere

class Toyota(Masina):
    def __init__(self, marca, motor):
        super().__init__(marca, motor)

motor = 500
car = Masina("Ford", motor)
print(car.porneste())
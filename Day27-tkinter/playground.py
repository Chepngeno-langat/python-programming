def add(*args):
    for n in args:
        print(n)

add(4, 8, 16)

def calculate(n, **kwargs):
    #for key, value in kwargs.items():
        #print(key)
        #print(value)

    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
        self.color = kw.get("color")

my_car = Car(make="Nissan", model="GT-R", color="Gray")
print(my_car.make, my_car.model, my_car.color)
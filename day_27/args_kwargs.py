from numpy import multiply


def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

add(3, 5, 6)

def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    #     print(f"{key} => {value}")
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    
calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
    
new_car = Car(make="VW")
print(new_car.make)
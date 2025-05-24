from functions import (greet, add, subtract, multiply)
from classes import (Person, Animal, Car)


print(greet("Meshack"))
print("Add:", add(9, 8))
print("Subtract:", subtract(10, 6))
print("Multiply:", multiply(2, 3))


person = Person("Meshack")
animal = Animal("cat")
car = Car("Buggati")

print(person.say_hello())
print(animal.speak())
print(car.drive())
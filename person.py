class Person:
    def __init__(self, name, age): #Dunder method, Important Method
        self.name = str(name)
        self.age = int(age)

    def talk(self):
        return "Hi there! My name is " +  \
        self.name + " and I am " + \
        str(self.age) + " years old"

new_person = Person("Charlotte", 45)
#
# print(new_person.name)
# print(new_person.age)
# print(new_person.talk())

class Car:
    def __init__(self, make, model, top_speed):
        self.make = str(make)
        self.model = str(model)
        self.top_speed = int(top_speed)

    def start(self):
        return "Vrrrrm, put, put"

    def drive(self, person):
        return "I am being driven by " + person.name

ford = Car("Ford, "Escort", 85)

# print(ford.make)
# print(ford.model)
# print(ford.top_speed)
print(ford.start())

print(ford.drive(ford))

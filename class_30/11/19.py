# OBJECT ORIENTED PROGRAM(OOP)
# OOP, CLASSES, OBJECT, ENCAPSULATION, INHERITANCE, POLYMORPHISM, METHOD, ATTRIBUTE, PROCEDURE

# __ (2 underscores are called constructors)
# a constructor is a special kind o0f method that python calls when it instantiates an object using the definition found in ur class


# (x, y, z) = tuple
# [x, y, z] = list
# {x, y, z} = set
# {x:"value", y:"value"} dictionaries
# JSON = javascript object notation

'''
class Human(object):            # classes that defines human beings
    def __init__(self, name, age, race, gender, religion):  # __init__ initialize constructor

        self.name = name
        self.age = age
        self.race = race
        self.gender = gender
        self.religion = religion

    def person(self):
        profile = """
        Name of person is {}, \n
        and {} is {} years old.\n
        {} is a {} and  a {}
        """.format(self.name, self.name, self.age, self.name, self.name, self.gender, self.religion)
        print(profile)

    def grow(self, value):
        new_age = int(self.age) + int(value)
        self.age = new_age
        print("Age is now: ", self.age)

    def test(self):
        print(self.personal())

class Swimmer(Human):
    def swim(self):
        print(self.name, "is swimming now")


sola = Human("Sola", "49", "African", "male", "muslim")
career = Swimmer("sola", "49", "African", "male", "muslim")
career.swim()
sola.person()
sola.grow(49)
'''


class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = point()
point1.draw()


# LIBRARY INSTALLATIONS AND WEB SCRAPPING

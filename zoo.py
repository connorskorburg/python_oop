'''Imagine a game where you can create a zoo and start raising different types of animals. Say that for each zoo you create can have several different animals. Start by creating an Animal class, and then at least 3 specific animal classes that inherit from Animal. (Maybe lions and tigers and bears, oh my!) Each animal should at least have a name, an age, a health level, and happiness level. The Animal class should have a display_info method that shows the animal's name, health, and happiness. It should also have a feed method that increases health and happiness by 10.

In at least one of the Animal child classes you've created, add at least one unique attribute. Give each animal different default levels of health and happiness. The animals should also respond to the feed method with varying levels of changes to health and happiness.'''
class Animal:
    def __init__(self, name, age, health, happiness):
        self.animal_name = name
        self.age = age
        self.health = health
        self.happiness = happiness
    def display_info(self):
        print(f"Animal Name: {self.animal_name}, Age: {self.age}, Health: {self.health}, Happines: {self.happiness}")
        return self
    def feed(self):
        self.happiness += 10
        self.health += 10
        return self

class Lion(Animal):
    def __init__(self, name, age = 8, health = 50, happiness = 25):
        super().__init__(name, age, health, happiness)
        self.has_mane = True
    def feed(self):
        self.health += 15
        self.happiness += 15
        return self

class Tiger(Animal):
    def __init__(self, name, age = 10, health = 30, happiness = 40):
        super().__init__(name, age, health, happiness)
        self.has_stripes = True
    def feed(self):
        self.health += 20
        self.happiness += 5
        return self

class Bear(Animal):
    def __init__(self, name, age = 15, health = 25, happiness = 15):
        super().__init__(name, age, health, happiness)
        self.color = "Black"
    def feed(self):
        self.health += 20
        self.happiness += 10
        return self

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self, Lion):
        self.animals.append( Lion )
        return self
    def add_tiger(self, Tiger):
        self.animals.append( Tiger )
        return self
    def add_bear(self, Bear):
        self.animals.append( Bear )
        return self
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
# initialize
bear = Bear("Big Bear")
tiger = Tiger("Tigger")
lion = Lion("Simba")
lion2 = Lion("Scar", age = 11)
zoo2 = Zoo("Bob's Zoo")
# methods
bear.feed().feed()
tiger.feed().feed().feed().feed().feed().feed().feed()
lion.feed().feed()
lion2.feed().feed().feed()
zoo2.add_bear(bear).add_tiger(tiger).add_lion(lion).add_lion(lion2)
zoo2.print_all_info()


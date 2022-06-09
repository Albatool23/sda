
class Animal:
    def __init__(self,name,age ,hp,happiness):
        self.name = name
        self.hp = hp
        self.happiness= happiness
        self.age= age
    def displayInfo(self):
        print(f'Name: {self.name} | Type: {self.type} | Hp: {self.hp} | age: {self.age} | happiness: {self.happiness}')

    def feed(self):
        pass

class  Bird(Animal):
    def __init__(self,name,age,fly):
        super().__init__(name,age ,hp = 10, happiness=20)
        self.type = "Baird"
        self.fly = fly

    def feed(self):
        self.happiness += 4
        self.hp  += 8

class Monkey(Animal):
    def __init__(self,name,age,tail):
        super().__init__(name,age,hp = 50,happiness=66 )
        self.type = "Monkey"
        self.tail = tail
    def feed(self):
        self.happiness += 1
        self.hp  += 18

class Bear (Animal):
    def __init__(self, name, age ,claws):
        super().__init__(name,age, hp=10 , happiness= 43)
        self.type = "Bear"
        self.claws = claws
    def feed(self):
        self.happiness += 11
        self.hp  += 9
class Zoo:
    def __init__(self,name):
        self.animals = []
        self.name = name
    def addBird(self, name,age,fly):
        self.animals.append(Bird(name,age,fly))
    def addBear(self, name,age,claws):
        self.animals.append(Bear(name,age,claws))
    def addMonkey(self, name,age,tail):
        self.animals.append(Monkey(name,age,tail))
    def printAll(self):
        for animal in self.animals:
            animal.displayInfo()
    def feedAll(self):
        for animal in self.animals:
            animal.feed()



zoo = Zoo("New Zoo")
zoo.addBird("Mano",9,True)
zoo.addMonkey("Marseel",13,True)
zoo.addBear("Anything",55,True)
zoo.printAll()
zoo.feedAll()
print("=="*30)
print("After feeding the animals:")
zoo.printAll()



class Animal:
    def __init__(self, name, age, species):
        self.name = name 
        self.age = age
        self.species = species
        
        if self.name == "dog":
            self.sound = "Woof! Woof!"
            
        
    def speak(self):
        print(self.sound)


a1 = Animal("dog", 10, "labrador")

a1.speak()
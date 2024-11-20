#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Animal:
    def __init__(self, name, backbone, classification, diet, sound):
        self.name = name
        self.backbone = backbone  #vertebrates or invertebrates
        self.classification = classification  #mammal, reptile, bird, etc.
        self.diet = diet  #carnivore, herbivore, omnivore
        self.sound = sound  #Animal sound
    
    def eat(self):
        if self.diet.lower() == "omnivore":
            print(f"{self.name} says: Yummy chicken salad!")
        elif self.diet.lower() == "herbivore":
            print(f"{self.name} says: Yummy grass!")
        elif self.diet.lower() == "carnivore":
            print(f"{self.name} says: Yummy beef!")
        else:
            print(f"{self.name} says: Oops, I don't know what to eat!")
    
    def make_sound(self):
        print(f"{self.name} says: {self.sound}")

    def show_details(self):
        print(f"""
        Name: {self.name}
        Backbone: {"Yes" if self.backbone else "No"}
        Classification: {self.classification}
        Diet: {self.diet}
        Sound: {self.sound}
        """)

class Dog(Animal):
    def __init__(self, name, age, breed, color, size, toy):
        super().__init__(name=name, backbone='vertebrate', classification='mammal', diet='omnivore', sound='bark')
        self.breed = breed
        self.color = color
        self.size = size
        self.toy = toy
    def bark(self):
        print('Woof!')
    def fetch(self, toy):
        print(f"{self.name} fetches the {toy}!")
    def wag(self):
        print(f"{self.name} wags their tail.")

#Animal instance
my_animal = Animal(name="Tiger",backbone=True,classification="Mammal",diet="Carnivore",sound="Roar")

my_animal.show_details()
my_animal.eat()
my_animal.make_sound()

buddy = Dog("Buddy", 3, "Golden Retriever", "golden", "large", "tennis ball")
print(buddy.wag())
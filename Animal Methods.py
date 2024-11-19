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

#Animal instance
my_animal = Animal(name="Tiger",backbone=True,classification="Mammal",diet="Carnivore",sound="Roar")

my_animal.show_details()
my_animal.eat()
my_animal.make_sound()


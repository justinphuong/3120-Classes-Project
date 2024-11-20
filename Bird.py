#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Animal:
    def __init__(self, name, backbone,blood,classifications,habitat,diet,reproduction):
        self.name = name
        self.backbone = backbone
        self.blood = blood
        self.classifications = classifications
        self.habitat = habitat
        self.diet = diet
        self.Reproduction = reproduction

class Bird(Animal):
    def __init__(self, name, backbone, color, diet, sound, can_fly):
        self.name = name
        self.backbone = backbone
        self.classification = "Bird"  
        self.diet = diet
        self.sound = sound
        self.color = color  
        self.can_fly = can_fly  # True or False

    def make_sound(self):
        print(f"{self.name} says: {self.sound}")

    def eat(self):
        if self.diet.lower() == "omnivore":
            print(f"{self.name} says: Yummy seeds and fruits!")
        elif self.diet.lower() == "herbivore":
            print(f"{self.name} says: Yummy leaves and grains!")
        elif self.diet.lower() == "carnivore":
            print(f"{self.name} says: Yummy insects!")
        else:
            print(f"{self.name} says: Hmm, I don't know what to eat!")

    def fly(self):
        if self.can_fly:
            print(f"{self.name} spreads its {self.color} wings and flies into the sky!")
        else:
            print(f"{self.name} can't fly, but it hops around cheerfully.")

    def show_details(self):
        print(f"""
        Name: {self.name}
        Backbone: {"Yes" if self.backbone else "No"}
        Classification: {self.classification}
        Diet: {self.diet}
        Sound: {self.sound}
        Color: {self.color}
        Can Fly: {'Yes' if self.can_fly else 'No'}
        """)

# Parrot instance
parrot = Bird(
    name="Parrot",
    backbone=True, 
    color="green",
    diet="Herbivore",
    sound="Squawk",
    can_fly=True
)

parrot.show_details()
parrot.fly()
parrot.make_sound()
parrot.eat()


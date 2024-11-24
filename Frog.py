class Animal:
    def __init__(self, name, backbone, blood, classifications, habitat, diet, reproduction):
        self.name = name
        self.backbone = backbone
        self.blood = blood
        self.classifications = classifications
        self.habitat = habitat
        self.diet = diet
        self.reproduction = reproduction

class Frog(Animal):
    def __init__(self, name, backbone, color, diet, sound, can_swim):
        self.name = name
        self.backbone = backbone
        self.classification = "Amphibian"
        self.diet = diet
        self.sound = sound
        self.color = color
        self.can_swim = can_swim

    def make_sound(self):
        print(f"{self.name} says: {self.sound}")

    def eat(self):
        if self.diet.lower() == "omnivore":
            print(f"{self.name} says: insects & plants")
        elif self.diet.lower() == "herbivore":
            print(f"{self.name} says: algae and plants")
        elif self.diet.lower() == "carnivore":
            print(f"{self.name} says: insects!")
        else:
            print(f"{self.name} says: Hmm, I don't know what to eat!")

    def swim(self):
        if self.can_swim:
            print(f"{self.name} leaps into the water and swims !")
        else:
            print(f"{self.name} Satys on land and hops around.")

    def show_details(self):
        print(f"""
        Name: {self.name}
        Backbone: {"Yes" if self.backbone else "No"}
        Classification: {self.classification}
        Diet: {self.diet}
        Sound: {self.sound}
        Color: {self.color}
        Can Swim: {'Yes' if self.can_swim else 'No'}
        """)

# Frog instance
frog = Frog(
    name="Tree Frog",
    backbone=True,
    color="green",
    diet="Carnivore",
    sound="Ribbit",
    can_swim=True
)

frog.show_details()
frog.swim()
frog.make_sound()
frog.eat()

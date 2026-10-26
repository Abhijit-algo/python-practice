# 1. Define the blueprint (Class)
class Dog:
    # Class attribute (shared by all dogs)
    species = "Canine"

    def __init__(self, name, breed):
        self.name = name   
        self.breed = breed  

    def bark(self):
        return f"{self.name} says Woof!"

    def get_details(self):
        return f"{self.name} is a {self.breed} ({self.species})."


dog1 = Dog(name="Buddy", breed="Golden Retriever")
dog2 = Dog(name="Max", breed="German Shepherd")

print("--- Dog 1 ---")
print(f"Name: {dog1.name}")
print(f"Breed: {dog1.breed}")
print(dog1.bark())
print(dog1.get_details())

print("\n--- Dog 2 ---")
print(f"Name: {dog2.name}")
print(f"Breed: {dog2.breed}")
print(dog2.bark())
print(dog2.get_details())

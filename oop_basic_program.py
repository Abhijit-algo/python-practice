# 1. Define a class
class Dog:
    # Set up initial data when an object is created
    def __init__(self, name):
        self.name = name

    # Define an action the object can do
    def bark(self):
        print(f"{self.name} says Woof!")


# 2. Create an object (instance)
my_dog = Dog("Buddy")

# 3. Call the object's method
my_dog.bark()

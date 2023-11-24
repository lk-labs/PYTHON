
class Person:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def display_info(self):
        print("Name\t\tAge\tWeight\tHeight")
        print("-----------------------------------")
        print(f"{self.name}\t{self.age}\t{self.weight}\t{self.height}")


# User input
name = input("Enter the name: ")
age = int(input("Enter the age: "))
weight = float(input("Enter the weight: "))
height = float(input("Enter the height: "))

# Create Person object with user input
person1 = Person(name, age, weight, height)

# Display the person's information
person1.display_info()

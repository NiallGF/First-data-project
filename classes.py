class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking")



Dog1 = Dog("James", 2)

Dog2 = Dog("Allen", 3)

print(Dog2.name)
Dog1.bark()
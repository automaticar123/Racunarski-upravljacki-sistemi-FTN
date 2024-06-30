# empty dictionary
empty_dict = {}

# dictionary with key-value pairs
person = {'name': 'John', 'age': 30, 'gender': 'Male'}

# using the dict() constructor
person = dict(name='John', age=30, gender='Male')

# accessing values using keys
print(person['name'])  # 'John'
print(person['age'])   # 30

# using the get() method to access values
print(person.get('name'))  # 'John'
print(person.get('height', 180))  # 180 (default value)

# adding a new key-value pair
person['height'] = 180

# updating an existing value
person['age'] = 35

# deleting a key-value pair using del statement
del person['age']

# deleting a key-value pair using pop() method
person.pop('gender')

# deleting all elements in a dictionary using clear() method
person.clear()

# using the 'in' keyword
if 'name' in person:
    print('Name is present in the dictionary')

# using the keys() method
if 'age' in person.keys():
    print('Age is present in the dictionary')


# looping through keys
for key in person:
    print(key)

# looping through values
for value in person.values():
    print(value)

# looping through key-value pairs
for key, value in person.items():
    print(key, value)

# Here's how to sort a dictionary by keys:
d = {'a': 3, 'c': 1, 'b': 2}
sorted_d = dict(sorted(d.items()))
print(sorted_d)  # Output: {'a': 3, 'b': 2, 'c': 1}

# Here's how to sort a dictionary by values:
d = {'a': 3, 'c': 1, 'b': 2}
sorted_d = dict(sorted(d.items(), key=lambda item: item[1]))
print(sorted_d)  # Output: {'c': 1, 'b': 2, 'a': 3}

# sort the dictionary in descending order:
d = {'a': 3, 'c': 1, 'b': 2}
sorted_d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
print(sorted_d)  # Output: {'a': 3, 'b': 2, 'c': 1}



# KLASE
# Instance creation: Instances of a class are created using the class name followed 
# by parentheses, which can contain arguments that are passed to the class constructor.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

p = Person("John", 30)
p.greet()  # Output: Hello, my name is John and I'm 30 years old.

# Inheritance: Classes can inherit attributes and methods from a parent class 
# using the super() function.
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        print("Bark bark!")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def make_sound(self):
        print("Meow meow!")

my_dog = Dog("Rufus", "Labrador Retriever")
my_cat = Cat("Whiskers", "Orange")

print(my_dog.name)
print(my_dog.breed)
my_dog.make_sound()

print(my_cat.name)
print(my_cat.color)
my_cat.make_sound()


# Polymorphism  is the ability of an object to take on many forms. 
# In Python, polymorphism is achieved through the use of method overriding and method overloading.
class Animal:   # parent class
    def sound(self):
        print("")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

animals = [Dog(), Cat()]
for animal in animals:
    animal.sound()

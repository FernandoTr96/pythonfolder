"""
OOP in Python - Example and Explanation
Author: Fernando's study notes
"""

# ----------------------------
# 1. CLASS & OBJECT
# ----------------------------
# A class is a blueprint for creating objects.
# An object is an instance of a class.

class Person:
    # __init__ is the constructor - it runs when you create a new object.
    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age    # instance attribute

    # Method = function inside a class
    def greet(self):
        print(f"Hi, my name is {self.name} and I’m {self.age} years old.")

# Create an object from the Person class
p1 = Person("Fernando", 26)
p1.greet()  # Calls the greet method


# ----------------------------
# 2. CLASS ATTRIBUTES vs INSTANCE ATTRIBUTES
# ----------------------------
class Dog:
    species = "Canis familiaris"  # Class attribute (shared by all instances)

    def __init__(self, name):
        self.name = name  # Instance attribute (unique per object)

dog1 = Dog("Max")
dog2 = Dog("Buddy")
print(dog1.species)  # same for all dogs
print(dog1.name)     # unique for this object


# ----------------------------
# 3. ENCAPSULATION (PUBLIC, PROTECTED, PRIVATE)
# ----------------------------
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner        # Public attribute
        self._balance = balance   # Protected attribute (by convention)
        self.__pin = "1234"       # Private attribute (name mangling)

    def get_balance(self):
        return self._balance

account = BankAccount("Fer", 5000)
print(account.owner)      # OK
print(account._balance)   # Possible but not recommended
# print(account.__pin)    # ERROR: AttributeError (private)


# ----------------------------
# 4. INHERITANCE
# ----------------------------
# Inheritance allows a class to reuse attributes/methods from another class.

class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

Dog().speak()  # Woof!
Cat().speak()  # Meow!


# ----------------------------
# 5. POLYMORPHISM
# ----------------------------
# Same method name, different behavior depending on the object type.

animals = [Dog(), Cat()]
for animal in animals:
    animal.speak()  # Each object calls its own speak()


# ----------------------------
# 6. ABSTRACTION
# ----------------------------
# Abstraction hides unnecessary implementation details.
# We use abstract base classes to force subclasses to implement methods.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Must be implemented by subclasses

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

c = Circle(5)
print(c.area())  # 78.5


# ----------------------------
# 7. MAGIC METHODS
# ----------------------------
# Special methods start and end with __
# __str__ controls how the object is printed.

class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book: {self.title}"

b = Book("Python 101")
print(b)  # Calls __str__


# ----------------------------
# 8. COMPOSITION (HAS-A RELATIONSHIP)
# ----------------------------
# Instead of "is-a" (inheritance), a class can use another class.

class Engine:
    def start(self):
        print("Engine starting...")

class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS an Engine

    def drive(self):
        self.engine.start()
        print("Car is moving!")

car = Car()
car.drive()



"""
OOP Decorators in Python - Study Notes
Author: Fernando's practice file
"""

# ----------------------------------------------------
# 1. @classmethod
# ----------------------------------------------------
# A class method receives the class itself (cls) as the first argument
# It can be called from the class or from an instance
# Common uses:
# - Factory methods (alternative constructors)
# - Class-level configuration or counters

class ExampleClass:
    count = 0  # Class attribute shared by all instances

    def __init__(self, name):
        self.name = name

    @classmethod
    def increment_count(cls):
        """Increase the shared class counter."""
        cls.count += 1

    @classmethod
    def from_uppercase(cls, name):
        """Factory method that creates an object with uppercase name."""
        return cls(name.upper())

# Calling a class method directly on the class
ExampleClass.increment_count()
print("Class count after increment:", ExampleClass.count)

# Using a class method as a factory
obj1 = ExampleClass.from_uppercase("fer")
print("Object name from factory:", obj1.name)


# ----------------------------------------------------
# 2. @staticmethod
# ----------------------------------------------------
# A static method does not receive self or cls
# It behaves like a normal function but is logically grouped inside the class
# Common uses:
# - Utility/helper functions related to the class's domain

class MathUtils:
    @staticmethod
    def add(a, b):
        """Return the sum of two numbers."""
        return a + b

    @staticmethod
    def is_even(number):
        """Check if a number is even."""
        return number % 2 == 0

print("Sum 2 + 3 =", MathUtils.add(2, 3))
print("Is 4 even?", MathUtils.is_even(4))


# ----------------------------------------------------
# 3. @property
# ----------------------------------------------------
# @property allows you to access a method like an attribute (read-only by default)
# Useful for computed attributes or for controlling access to internal data

class Circle:
    def __init__(self, radius):
        self._radius = radius  # Protected attribute

    @property
    def area(self):
        """Return the area of the circle."""
        return 3.14 * self._radius ** 2

    @property
    def radius(self):
        """Get the radius."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set the radius with validation."""
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

c = Circle(5)
print("Circle area:", c.area)  # No parentheses needed

c.radius = 10  # Calls the setter
print("New circle area:", c.area)



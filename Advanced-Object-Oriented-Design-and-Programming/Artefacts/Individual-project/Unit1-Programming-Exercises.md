# Programming Exercise (Unit 1) – Classes, Inheritance, Polymorphism, Abstraction and Encapsulation

## Activity overview

- **Exercise topic:** Programming exercises on Classes, Objects, Access Control, Inheritance, Polymorphism, Abstraction, and Encapsulation.
- **Duration:** Unit 1.

## Tasks

1. **Basic Class Hierarchy (Inheritance):**
      Define a base class Vehicle with brand and fuel_type as instance attributes (use __init__).
      Create a subclass Car that inherits from Vehicle and adds num_doors as an additional attribute.
      Ensure the Car class calls the parent class's __init__ method (using super() in Python).
2. **Polymorphism with Methods:**
      Define an abstract Shape class with an abstract method area() (use ABC and abstractmethod in Python).
      Create Circle and Rectangle subclasses that inherit from Shape.
      Implement area() in each subclass (for Circle, use πr²; for Rectangle, use length * width).
3. **Encapsulation with Access Control:**
      Define BankAccount with a private attribute __balance (use double underscore in Python).
      Provide public methods:
      deposit(amount) to add to __balance.
      withdraw(amount) to deduct from __balance (check for sufficient funds).
      Use getter methods if balance access is needed (e.g., get_balance()).
4. **Abstraction with Base Class:**
      Create an abstract Animal class with an abstract method make_sound().
      Implement subclasses Dog and Cat, each overriding make_sound() to return "Woof!" and "Meow!" respectively.
      Use ABC and abstractmethod decorators in Python.
5. **Constructor and Destructor:**
      Define a Person class with __init__(self, name) to set the name attribute.
      Add a destructor __del__(self) that prints a farewell message (e.g., "Goodbye, {name}!").
      Test by creating and deleting an instance (use del explicitly or let it go out of scope).

## My Code

### Task 1: Basic Class Hierarchy (Inheritance)

```python
class Vehicle:
    def __init__(self, brand, fuel_type):
        self.brand = brand
        self.fuel_type = fuel_type

class Car(Vehicle):  # subclass Car inherits from Vehicle
    def __init__(self, brand, fuel_type, num_doors):
        super().__init__(brand, fuel_type)  # call the parent __init__ first
        self.num_doors = num_doors

vehicle = Vehicle("Toyota", "Gasoline")  # object
car = Car("Toyota", "Gasoline", 4)       # object

print(vehicle.brand)
print(vehicle.fuel_type)
print(car.num_doors)
```

### Task 2: Polymorphism with Methods

```python
import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod                 # hides details
    def area(self):
        pass                        # the block is intentionally empty

class Circle(Shape):                # subclass
    def __init__(self, radius):     # Single Responsibility Principle, one method by class
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


circle = Circle(2).area()
rectangle = Rectangle(2, 4).area()
print(f"The area of circle is {circle:.2f} and the area of rectangle is {rectangle}")
```

### Task 3: Encapsulation with Access Control

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance    # private attribute (name mangling)

    @property                       # read access to balance
    def balance(self):
        return self.__balance

    def deposit(self, deposit_amount):
        self.__balance += deposit_amount

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.__balance:   # check for sufficient funds
            print("Insufficient funds")
            return
        self.__balance -= withdraw_amount


b = BankAccount(20)
b.deposit(100)
print(b.balance)
b.withdraw(50)
print(b.balance)
```

### Task 4: Abstraction with Base Class

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):                  # subclass
    def make_sound(self):           # polymorphism: same name "make_sound" behaves differently
        return "Woof!"


class Cat(Animal):                  # subclass
    def make_sound(self):
        return "Meow!"

for animal in [Dog(), Cat()]:
    print(animal.make_sound())
```

### Task 5: Constructor and Destructor

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):          # destructor
        print(f"Goodbye {self.name}!")


person = Person("li")
del person
```
#Task 1: Basic Class Hierarchy (Inheritance)

class Vehicle:
    def __init__(self, brand, fuel_type):
        self.brand = brand
        self.fuel_type = fuel_type

class Car(Vehicle): # subclass car inherits from Vehicle
    def __init__(self, brand, fuel_type, num_doors):
        super().__init__(brand, fuel_type) # do the subclass after the class
        self.num_doors = num_doors

vehicle = Vehicle("Toyota", "Gasoline")  #object
car = Car("Toyota", "Gasoline", 4) #object

print(vehicle.brand)
print(vehicle.fuel_type)
print(car.num_doors)


#Task 2: Polymorphism with Methods

import math
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod                 #hides details
    def area(self):
        pass                        # The block is intentionally empty

class Circle(Shape):                #subclass
    def __init__(self, radius):     #Single Responsibility Principle, one method by class
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


circle = Circle(2).area()
rectangle = Rectangle(2,4).area()
print(f"The area of circle is {circle:.2f} and the area of rectangle is {rectangle}")

#Task 3: Encapsulation with Access Control


class BankAccount:
    def __init__(self, __balance):
        self. __balance = __balance


    @property                       # gave access to balance, deposit and withdraw
    def balance(self):
        return self.__balance

    def deposit(self,deposit_amount):
        self.__balance += deposit_amount

    def withdraw(self,withdraw_amount):
        self.__balance -= withdraw_amount


b = BankAccount(20)
b.deposit(100)
print(b.balance)
b.withdraw(50)
print(b.balance)

#Task 4: Abstraction with Base Class

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):                  #subclass
    def make_sound(self):           #polymorphism . same name "make_sound" behave differently
        return "Woof!"


class Cat(Animal):                  #subclass
    def make_sound(self):
        return "Meow!"

for animal in [Dog(), Cat()]:
    print(animal.make_sound())



#Task 5: Constructor and Destructor


class Person:
    def __init__(self,name):
        self.name =name

    def __del__(self):          #delete user
        print(f"Goodbye {self.name}!")


person = Person("li"); del person


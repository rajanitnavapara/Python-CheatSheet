'''
12.Constructors 
1. Write a class with a default constructor, one argument constructor and two argument 
constructors. Instantiate the class to call all the constructors of that class from a main 
class 
2. Call the constructors(both default and argument constructors) of super class from a child 
class 
3. Apply private, public, protected and default access modifiers to the constructor 
4. Write a program which illustrates the concept of attributes of a constructor.
'''

# 1. Write a class with a default constructor, one argument constructor and two argument 
# constructors. Instantiate the class to call all the constructors of that class from a main
# class
class Constructors:
    def __init__(self):
        print("Default Constructor")

    def __init__(self, arg1):
        print("One Argument Constructor: ", arg1)

    def __init__(self, arg1, arg2):
        print("Two Argument Constructor: ", arg1, arg2)


# 2. Call the constructors(both default and argument constructors) of super class from a child 
# class
class ChildClass(Constructors):
    def __init__(self):
        print("Child Class Default Constructor")
        super().__init__()

    def __init__(self, arg1):
        print("Child Class One Argument Constructor: ", arg1)
        super().__init__(arg1)

    def __init__(self, arg1, arg2):
        print("Child Class Two Argument Constructor: ", arg1, arg2)
        super().__init__(arg1, arg2)


obj1 = Constructors() # Output: Default Constructor
obj2 = Constructors("Hello") # Output: One Argument Constructor: Hello
obj3 = Constructors("Hello", "World") # Output: Two Argument Constructor: Hello World
obj4 = ChildClass() # Output: Child Class Default Constructor
#         Default Constructor
obj5 = ChildClass("Hello") # Output: Child Class One Argument Constructor: Hello
#         One Argument Constructor: Hello
obj6 = ChildClass("Hello", "World") # Output: Child Class Two Argument Constructor: Hello World
                                         #    Two Argument Constructor: Hello World


# 3. Apply private, public, protected and default access modifiers to the constructor
class AccessModifiers:
    def __init__(self):
        self.__private = "Private"
        self.public = "Public"
        self._protected = "Protected"
        self.default = "Default"

    def display(self):
        print(self.__private)
        print(self.public)
        print(self._protected)
        print(self.default)

    def __private_method(self):
        self.__private_method()
        print("Private Method")


obj7 = AccessModifiers()
print(obj7.public)  # Output: Public attribute
print(obj7._protected)  # Output: Protected attribute
obj7.access_private()  # Output: Private method, Private attribute


# 4. Write a program which illustrates the concept of attributes of a constructor.
class Attributes:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    def update(self, name, age):
        self.name = name
        self.age = age


obj8 = Attributes("John", 25)
obj8.display()  # Output: Name: John, Age: 25
obj8.update("Jane", 30) # Output: Name: Jane, Age: 30

# End of 12_Constructors.py
# Date: 04/07/2024

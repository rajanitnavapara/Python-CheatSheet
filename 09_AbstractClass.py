'''
9.Abstract Class 
1. Create an abstract class with abstract and non-abstract methods. 
2. Create a sub class for an abstract class. Create an object in the child class for the  
abstract class and access the non-abstract methods 
3. Create an instance for the child class in child class and call abstract methods 
4. Create an instance for the child class in child class and call non-abstract methods
'''

from abc import ABC, abstractmethod

# 1. Create an abstract class with abstract and non-abstract methods.
class Abstract(ABC):
        
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def abstract_method(self):
        pass
    
    def non_abstract_method(self):
        print("Non-abstract method")

# 2. Create a sub class for an abstract class. Create an object in the child class for the  
# abstract class and access the non-abstract methods
class SubAbstract(Abstract):

    def __init__(self, value):
        super().__init__(value)

    # Implement the abstract method
    def abstract_method(self):
        print(f"Abstract method implementation: {self.value}")

    def access_non_abstract_method(self):
        # Create an object of the abstract class in the subclass
        abstract_obj = Abstract(self.value)
        abstract_obj.non_abstract_method()


# 3. Create an instance of the subclass and call the abstract method
concrete_obj = SubAbstract("Hello")
concrete_obj.abstract_method()  # Output: Abstract method implementation: Hello


# 4. Create an instance of the subclass and call the non-abstract method
concrete_obj.access_non_abstract_method()  # Output: Non-abstract method: Hello
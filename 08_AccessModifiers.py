'''
8.Access Modifiers 
1. Create a class with PRIVATE fields, private method and a main method. Print the fields 
in main method. Call the private method in main method. 
Create a sub class and try to access the private fields and methods from sub class. 
2. Create a class with PROTECTED fields and methods. Access these fields and methods 
from any other class in the same package.  
Also, Access the PROTECTED fields and methods from child class located in a different 
package 
Access the PROTECTED fields and methods from any class in different package 
3. Create a class with PUBLIC fields and methods.  
Access the public methods and fields from any class in the same package or different 
package. 
'''

# 1. Create a class with PRIVATE fields, private method and a main method. Print the fields 
# in main method. Call the private method in main method.
# Create a sub class and try to access the private fields and methods from sub class.

class Private:
    
    
    def __init__(self):
        self.__privateField = 10
        print("Private class constructor")
    
    def __privateMethod(self):
        print("Private method")
    
    def main(self):
        print("Private field:", self.__privateField)
        self.__privateMethod()


class SubPrivate(Private):
        
    def __init__(self):
        print("SubPrivate class constructor")
    
    def main(self):
        print("Private field:", self.__privateField)
        self.__privateMethod()


p = Private() # Private class constructor
p.main() # Private field: 10
         # Private method
s = SubPrivate() # SubPrivate class constructor
s.main() # AttributeError: 'SubPrivate' object has no attribute '_SubPrivate__privateField'
         # AttributeError: 'SubPrivate' object has no attribute '_SubPrivate__privateMethod'


# 2. Create a class with PROTECTED fields and methods. Access these fields and methods 

class Protected:
    
    def __init__(self):
        self._protectedField = 20
        print("Protected class constructor")

    def _protectedMethod(self):
        print("Protected method")

    def main(self):
        print("Protected field:", self._protectedField)
        self._protectedMethod()


# Access the PROTECTED fields and methods from any other class in the same package.  
class TestProtected:
    
    def __init__(self):
        self.protected = Protected()
        print("TestProtected class constructor")

    def main(self): 
        print("Protected field:", self.protected._protectedField)
        self.protected._protectedMethod()


t = TestProtected() # Protected class constructor
t.main() # Protected field: 20
         # Protected method


# 2. Create a class with PROTECTED fields and methods. Access these fields and methods 
# from child class located in a different package.
# Access the PROTECTED fields and methods from any class in different package


# 3. Create a class with PUBLIC fields and methods.
# Access the public methods and fields from any class in the same package or different
# package.

class Public:
        
        def __init__(self):
            self.publicField = 30
            print("Public class constructor")
        
        def publicMethod(self):
            print("Public method")
        
        def main(self):
            print("Public field:", self.publicField)
            self.publicMethod()


# Access the public methods and fields from any class in the same package or different
# package.
class TestPublic:
    
    def __init__(self):
        self.public = Public()
        print("TestPublic class constructor")
    
    def main(self):
        print("Public field:", self.public.publicField)
        self.public.publicMethod()


t = TestPublic() # Public class constructor
t.main() # Public field: 30
         # Public method

# End of 08_AccessModifiers.py
# Date: 04/07/2024
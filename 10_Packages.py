'''
10.Packages 
1. Create a program to create two class. 
1.1. Create a constructor and a method for each class 
1.2. Create a __init__.py for adding all packages 
1.3. Import the respective packages 
1.4. Call each class by creating an object to it  
1.5. Create a program by all the above 
'''

from Packages import Class1, Class2

def main():
    obj1 = Class1("Hello")
    obj1.method1()  # Output: Method1 of Class1: Hello

    obj2 = Class2("World")
    obj2.method2()  # Output: Method2 of Class2: World

if __name__ == "__main__":
    main()
'''
7. Inheritance 
A, B and C are classes 
A is a super class. B is a sub class of A. C is a sub class of B.  
Create three methods in each class, 2 methods are specific to each class and third 
method (override method) should be in all three Classes A, B and C 
Create a class with main method. Create an object for each class A, B and C in main 
method and call every method of each class using its own object/instance. 
Call an overridden method with super class reference to B and C class’s objects 
Runtime Polymorphism with Data Members/Instance variables, Repeat the above 
process only for data members
'''

class A:
    
    def __init__(self):
        print("A class constructor")
    
    def method1(self):
        print("Method1 of A")
    
    def method2(self):
        print("Method2 of A")
    
    def method3(self):
        print("Method3 of A")


class B(A):
    
    def __init__(self):
        print("B class constructor")

    def method1(self):
        print("Method1 of B")

    def method2(self):
        print("Method2 of B")

    def method3(self):
        print("Method3 of B")


class C(B):

    def __init__(self):
        print("C class constructor")
    
    def method1(self):
        print("Method1 of C")

    def method2(self):
        print("Method2 of C")

    def method3(self):
        print("Method3 of C")


class Main:

    def main():
        a = A()
        a.method1() # Method1 of A
        a.method2() # Method2 of A
        a.method3() # Method3 of A
        print() 
        
        b = B()
        b.method1() # Method1 of B
        b.method2() # Method2 of B
        b.method3() # Method3 of B
        print()
        
        c = C()
        c.method1() # Method1 of C
        c.method2() # Method2 of C
        c.method3() # Method3 of C
        print()
        
        a.method3() # Method3 of A
        b.method3() # Method3 of B
        c.method3() # Method3 of C
        print()


if __name__ == "__main__":
    Main.main()


# End of 07_Inheritance.py
# Date: 04/07/2024
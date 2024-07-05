'''
1. Python Basics 
1. Write a program to print your name. 
2. Write a program for a Single line comment and multi-line comments 
3. Define variables for different Data Types int, Boolean, char, float, double and print on the 
Console. 
4. Define the local and Global variables with the same name and print both variables and 
understand the scope of the variables
'''

# 1. Write a program to print your name.
print("My name is Rajanit Navapara.")


# 2. Write a program for a Single line comment and multi-line comments
# Single line comment
'''
Multi line comment 
Multi line comment
Multi line comment
'''


# 3. Define variables for different Data Types int, Boolean, char, float, double and print on the Console.
a = 10 # int
b = True # Boolean
c = 'A' # char
d = 10.5 # float
e = 10.5 # double
print(a, b, c, d, e) # 10 True A 10.5 10.5


# 4. Define the local and Global variables with the same name and print both variables and understand the scope of the variables
# Global variable
f = 10
def test():
    # Local variable
    f = 20
    print(f) # 20

test()
print(f) # 10


# End of 01_PythonBasics.py
# Date: 04/07/2024
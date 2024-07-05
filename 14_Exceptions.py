'''
14.Exceptions 
1. Write a program to generate Arithmetic Exception without exception handling 
2. Handle the Arithmetic exception using try-catch block 
3. Write a method which throws exception, Call that method in main class without try block 
4. Write a program with multiple catch blocks 
5. Write a program to throw exception with your own message 
6. Write a program to create your own exception 
7. Write a program with finally block 
8. Write a program to generate Arithmetic Exception 
9. Write a program to generate FileNotFoundException 
10. Write a program to generate ClassNotFoundException 
11. Write a program to generate IOException 
12. Write a program to generate NoSuchFieldException 
'''

# 1. Write a program to generate Arithmetic Exception without exception handling
a = 10/0 # Output: ZeroDivisionError: division by zero


# 2. Handle the Arithmetic exception using try-catch block
try:
    a = 10/0
except ZeroDivisionError:
    print("Arithmetic Exception: Division by Zero")


# 3. Write a method which throws exception, Call that method in main class without try block
def method():
    raise Exception("Exception Raised")

method() # Output: Exception: Exception Raised


# 4. Write a program with multiple catch blocks
try:
    a = 10/0
except ZeroDivisionError:
    print("Arithmetic Exception: Division by Zero")
except Exception as e:
    print("Exception: ", e)


# 5. Write a program to throw exception with your own message
try:
    a = 10/0
except ZeroDivisionError:
    raise Exception("Arithmetic Exception: Division by Zero")


# 6. Write a program to create your own exception
class MyException:
    def __init__(self, message):
        self.message = message

try:
    raise MyException("My Exception")   
except MyException as e:
    print("My Exception: ", e.message)


# 7. Write a program with finally block
try:
    a = 10/0
except ZeroDivisionError:
    print("Arithmetic Exception: Division by Zero")
finally:
    print("Finally Block")


# 8. Write a program to generate Arithmetic Exception
a = 10/0 # Output: ZeroDivisionError: division by zero


# 9. Write a program to generate FileNotFoundException
try:
    file = open("file.txt", "r")
except FileNotFoundError:
    print("File Not Found Exception")


# 10. Write a program to generate ClassNotFoundException
try:
    import abc
except ModuleNotFoundError:
    print("Class Not Found Exception")


# 11. Write a program to generate IOException
try:
    file = open("file.txt", "r")
except IOError:
    print("IO Exception")


# 12. Write a program to generate NoSuchFieldException
class NoSuchFieldException(Exception):
    def __init__(self, message):
        self.message = message

try:
    raise NoSuchFieldException("No Such Field Exception")
except NoSuchFieldException as e:
    print("No Such Field Exception: ", e.message)


# End of 14_Exceptions.py
# Date : 04/07/2024
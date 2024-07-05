'''
13.Method Overloading 
1. Write two methods with the same name but different number of parameters of same type 
and call the methods  
2. Write two methods with the same name but different number of parameters of different 
data type and call the methods  
3. Write two methods with the same name and same number of parameters of same type 
'''

# 1. Write two methods with the same name but different number of parameters of same type 
# and call the methods
class MethodOverloading:
    def method(self, arg1):
        print("One Argument Method: ", arg1)

    def method(self, arg1, arg2):
        print("Two Argument Method: ", arg1, arg2)

obj = MethodOverloading()
# obj.method("Hello") # Output: TypeError: method() missing 1 required positional argument: 'arg2'
obj.method("Hello", "World") # Output: Two Argument Method: Hello World

# 2. Write two methods with the same name but different number of parameters of different 
# data type and call the methods
class MethodOverloading:
    def method(self, arg1):
        print("One Argument Method: ", arg1)

    def method(self, arg1:str, arg2:int):
        print("Two Argument Method: ", arg1, arg2)

obj = MethodOverloading()
# obj.method("Hello") # Output: TypeError: method() missing 1 required positional argument: 'arg2'
obj.method("Hello", 15) # Output: Two Argument Method: Hello 15


# 3. Write two methods with the same name and same number of parameters of same type
class MethodOverloading:
    def method(self, arg1):
        print("One Argument Method: 1 ", arg1)

    def method(self, arg1):
        print("One Argument Method: 2 ", arg1)

obj = MethodOverloading()
obj.method("Hello") # Output: One Argument Method: 2 Hello

# Note: In Python, method overloading is not supported. If we write two methods with the same name, 
# the latest method will override the previous method. So, the latest method will be executed.
# To achieve method overloading, we can use default arguments.
class MethodOverloading:
    def method(self, arg1, arg2=None):
        if arg2:
            print("Two Argument Method: ", arg1, arg2)
        else:
            print("One Argument Method: ", arg1)

obj = MethodOverloading()
obj.method("Hello") # Output: One Argument Method: Hello
obj.method("Hello", "World") # Output: Two Argument Method: Hello World

# Note: In the above example, we have used default arguments to achieve method overloading. 
# If we pass two arguments, then the two argument method will be executed. If we pass only one 
# argument, then the one argument method will be executed.

# End of 13_MethodOverloading.py
# Date :

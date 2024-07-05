'''
2.Operators 
1. Write a function for arithmetic operators(+,-,*,/) 
2. Write a method for increment and decrement operators(++, --) 
3. Write a program to find the two numbers equal or not. 
4. Program for relational operators (<,<==, >, >==) 
5. Print the smaller and larger number
'''

# 1. Write a function for arithmetic operators(+,-,*,/)
def arithmetic_operators(a, b):
    print(a + b) # 30
    print(a - b) # 10
    print(a * b) # 200
    print(a / b) # 2.0

arithmetic_operators(20, 10) # 30, 10, 200, 2.0


# 2. Write a method for increment and decrement operators(++, --)
def increment_decrement_operators(a):
    a += 1
    print(a) # 11
    a -= 1
    print(a) # 10

increment_decrement_operators(10) # 11, 10


# 3. Write a program to find the two numbers equal or not.
def equal_numbers(a, b):
    if a == b:
        print("Both numbers are equal.")
    else:
        print("Both numbers are not equal.")

equal_numbers(10, 20) # Both numbers are not equal.


# 4. Program for relational operators (<,<==, >, >==)
def relational_operators(a, b):
    if a < b:
        print("a is less than b.")
    elif a <= b:
        print("a is less than or equal to b.")
    elif a > b:
        print("a is greater than b.")
    elif a >= b:
        print("a is greater than or equal to b.")

relational_operators(10, 20) # a is less than b.


# 5. Print the smaller and larger number
def smaller_larger_number(a, b):
    if a < b:
        print("Smaller number is", a)
        print("Larger number is", b)
    else:
        print("Smaller number is", b)
        print("Larger number is", a)

smaller_larger_number(10, 20) # Smaller number is 10, Larger number is 20


# End of 02_Operators.py
# Date: 04/07/2024
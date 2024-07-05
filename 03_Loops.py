'''
3.Loops 
1. Write a program to print  “Bright IT Career”  ten times using for loop 
2. Write a  program to print 1 to 20 numbers using the while loop. 
3. Program to equal operator and not equal operators 
4. Write a program to print the odd and even numbers. 
5. Write a program to print largest number among three numbers. 
6. Write a  program to print even number between 10 and 20 using while 
7. Write a program to print 1 to 10 using the do-while loop statement. 
8. Write a program to find Armstrong number or not 
9. Write a program to find the prime or not. 
10. Write a program to palindrome or not. 
11. Program to check whether a number is EVEN or ODD using switch 
12. Print gender (Male/Female) program according to given M/F using switch 
'''

# 1. Write a program to print  “Bright IT Career”  ten times using for loop
for i in range(10):
    print("Bright IT Career")


# 2. Write a program to print 1 to 20 numbers using the while loop.
i = 1
while i <= 20:
    print(i)
    i += 1


# 3. Program to equal operator and not equal operators
def equal_not_equal_operators(a, b):
    if a == b:
        print("Both numbers are equal.")
    elif a!= b:
        print("Both numbers are not equal.")

equal_not_equal_operators(10, 20) # Both numbers are not equal.


# 4. Write a program to print the odd and even numbers.
def odd_even_numbers():
    for i in range(1, 5):
        if i % 2 == 0:
            print(i, "is even.")
        else:
            print(i, "is odd.")

odd_even_numbers() # 1 is odd. 2 is even. 3 is odd. 4 is even.


# 5. Write a program to print largest number among three numbers.
def largest_number(a, b, c):
    if a > b and a > c:
        print(a, "is the largest number.")
    elif b > a and b > c:
        print(b, "is the largest number.")
    else:
        print(c, "is the largest number.")

largest_number(10, 20, 30) # 30 is the largest number.


# 6. Write a  program to print even number between 10 and 20 using while
i = 10
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1
# 10, 12, 14, 16, 18, 20


# 7. Write a program to print 1 to 10 using the do-while loop statement.
i = 1
while True:
    print(i)
    i += 1
    if i > 10:
        break


# 8. Write a program to find Armstrong number or not
def armstrong_number(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if n == sum:
        print(n, "is an Armstrong number.")
    else:
        print(n, "is not an Armstrong number.")

armstrong_number(153) # 153 is an Armstrong number.


# 9. Write a program to find the prime or not.
def prime_number(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                print(n, "is not a prime number.")
                break
        else:
            print(n, "is a prime number.")
    else:
        print(n, "is not a prime number.")

prime_number(7) # 7 is a prime number.


# 10. Write a program to palindrome or not.
def palindrome_number(n):
    temp = n
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    if temp == rev:
        print(temp, "is a palindrome number.")
    else:
        print(temp, "is not a palindrome number.")

palindrome_number(121) # 121 is a palindrome number.


# 11. Program to check whether a number is EVEN or ODD using switch
def even_odd_number(n):
    match n%2:
        case 0:
            print(n, "is an even number.")
        case 1:
            print(n, "is an odd number.")

even_odd_number(10) # 10 is an even number.


# 12. Print gender (Male/Female) program according to given M/F using switch
def print_gender(gender):
    match gender:
        case "M":
            print("Male")
        case "F":
            print("Female")

print_gender("M") # Male

# End of 03_Loops.py
# Date: 04/07/2024
'''
6.Strings 
1. Different ways creating a string 
2. Concatenating two strings using + operator 
3. Finding the length of the string 
4. Extract a string using Substring 
5. Searching in strings using index() 
6. Matching a String Against a Regular Expression With matches() 
7. Comparing strings  
8. startsWith(), endsWith() and compareTo() 
9. Trimming strings with strip() 
10. Replacing characters in strings with replace() 
11. Splitting strings with split() 
12. Converting integer objects to Strings 
13. Converting to uppercase and lowercase
'''

# 1. Different ways creating a string
string1 = "Hello World"
string2 = 'Hello World'
string3 = """Hello World"""
string4 = '''Hello World'''


# 2. Concatenating two strings using + operator
string1 = "Hello"
string2 = "World"
print(string1 + " " + string2) # Hello World


# 3. Finding the length of the string
string = "Hello World"
print(len(string)) # 11


# 4. Extract a string using Substring
string = "Hello World"
print(string[0:5]) # Hello


# 5. Searching in strings using index()
string = "Hello World"
print(string.index("World")) # 6


# 6. Matching a String Against a Regular Expression With matches()
import re
string = "Hello World"
pattern = re.compile("Hello")
print(pattern.match(string)) # <re.Match object; span=(0, 5), match='Hello'>
pattern = re.compile("World")
print(pattern.match(string)) # None


# 7. Comparing strings
string1 = "Hello World"
string2 = "Hello World"
string3 = "Hello"
print(string1 == string2) # True
print(string1 == string3) # False


# 8. startsWith(), endsWith() and compareTo()
string = "Hello World"
print(string.startswith("Hello")) # True
print(string.endswith("World")) # True
string1 = "Hello"
string2 = "World"
print(string1 < string2) # True


# 9. Trimming strings with strip()
string = " Hello World "
print(string.strip()) # Hello World


# 10. Replacing characters in strings with replace()
string = "Hello World"
print(string.replace("World", "Universe")) # Hello Universe


# 11. Splitting strings with split()
string = "Hello World"
print(string.split(" ")) # ['Hello', 'World']


# 12. Converting integer objects to Strings
integer = 10
print(str(integer)) # 10


# 13. Converting to uppercase and lowercase
string = "Hello World"
print(string.upper()) # HELLO WORLD
print(string.lower()) # hello world


# End of 06_Strings.py
# Date: 04/07/2024
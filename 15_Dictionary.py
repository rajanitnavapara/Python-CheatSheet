'''
15.Dictionary 
1. Create a Dictionary with at least 5 key value pairs of the Student ID and Name 
1.1. Adding the values in dictionary 
1.2. Updating the values in dictionary 
1.3. Accessing the value in dictionary 
1.4. Create a nested loop dictionary 
1.5. Access the values of nested loop dictionary 
1.6. Print the keys present in a particular dictionary 
1.7. Delete a value from a dictionary
'''

# 1. Create a Dictionary with at least 5 key value pairs of the Student ID and Name
student = {1: 'John', 2: 'Doe', 3: 'Jane', 4: 'Doe', 5: 'Smith'}

# 1.1. Adding the values in dictionary
student[6] = 'Doe'

# 1.2. Updating the values in dictionary
student[6] = 'Smith'

# 1.3. Accessing the value in dictionary
print(student[6]) # Smith

# 1.4. Create a nested loop dictionary
student = { 1: {'Name': 'John', 'Age': 20}, 
            2: {'Name': 'Doe', 'Age': 21},
            3: {'Name': 'Jane', 'Age': 22}, 
            4: {'Name': 'Doe', 'Age': 23}, 
            5: {'Name': 'Smith', 'Age': 24}
          }

# 1.5. Access the values of nested loop dictionary
print(student[1]['Name']) # John

# 1.6. Print the keys present in a particular dictionary
print(student.keys())

# 1.7. Delete a value from a dictionary
del student[1]
print(student) # {2: {'Name': 'Doe', 'Age': 21}, 3: {'Name': 'Jane', 'Age': 22}, 4: {'Name': 'Doe', 'Age': 23}, 5: {'Name': 'Smith', 'Age': 24}}

# End of 15_Dictionary.py
# Date: 04/07/2024
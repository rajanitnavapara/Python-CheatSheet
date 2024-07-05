'''
4.Arrays 
1. Write a function to add integer values of an array 
2. Write a function to calculate the average value of an array of integers 
3. Write a program to find the index of an array element 
4. Write a function to test if array contains a specific value 
5. Write a function to remove a specific element from an array 
6. Write a function to copy an array to another array 
7. Write a function to insert an element at a specific position in the array 
8. Write a function to find the minimum and maximum value of an array 
9. Write a function to reverse an array of integer values 
10. Write a function to find the duplicate values of an array 
11. Write a program to find the common values between two arrays 
12. Write a method to remove duplicate elements from an array 
13. Write a method to find the second largest number in an array 
14. Write a method to find the second largest number in an array 
15. Write a method to find number of even number and odd numbers in an array 
16. Write a function to get the difference of largest and smallest value 
17. Write a method to verify if the array contains two specified elements(12,23) 
18. Write a program to remove the duplicate elements and return the new array 
''' 

# 1. Write a function to add integer values of an array 
def add_integer_values_of_array(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

arr = [1,2,3,4,5]
print(add_integer_values_of_array(arr)) # 15


# 2. Write a function to calculate the average value of an array of integers
def average_value_of_array(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum/len(arr)

arr = [1,2,3,4,5]
print(average_value_of_array(arr)) # 3.0


# 3. Write a program to find the index of an array element
def find_index_of_element(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return -1

arr = [1,2,3,4,5]
element = 3
print(find_index_of_element(arr, element)) # 2


# 4. Write a function to test if array contains a specific value
def test_if_array_contains_specific_value(arr, element):
    for i in arr:
        if i == element:
            return True
    return False

arr = [1,2,3,4,5]
element = 3
print(test_if_array_contains_specific_value(arr, element)) # True


# 5. Write a function to remove a specific element from an array
def remove_specific_element_from_array(arr, element):
    new_arr = []
    for i in arr:
        if i != element:
            new_arr.append(i)
    return new_arr

arr = [1,2,3,4,5]
element = 3
print(remove_specific_element_from_array(arr, element)) # [1, 2, 4, 5]


# 6. Write a function to copy an array to another array
def copy_array_to_another_array(arr):
    new_arr = []
    for i in arr:
        new_arr.append(i)
    return new_arr

arr = [1,2,3,4,5]
print(copy_array_to_another_array(arr)) # [1, 2, 3, 4, 5]


# 7. Write a function to insert an element at a specific position in the array
def insert_element_at_specific_position_in_array(arr, element, position):
    new_arr = []
    for i in range(len(arr)):
        if i == position:
            new_arr.append(element)
        new_arr.append(arr[i])
    return new_arr

arr = [1,2,3,4,5]
element = 10
position = 2
print(insert_element_at_specific_position_in_array(arr, element, position)) # [1, 2, 10, 3, 4, 5]


# 8. Write a function to find the minimum and maximum value of an array
def find_min_max_value_of_array(arr):
    min = arr[0]
    max = arr[0]
    for i in arr:
        if i < min:
            min = i
        if i > max:
            max = i
    return min, max

arr = [1,2,3,4,5]
print(find_min_max_value_of_array(arr)) # (1, 5)


# 9. Write a function to reverse an array of integer values
def reverse_array_of_integer_values(arr):
    return arr[::-1]

arr = [1,2,3,4,5]
print(reverse_array_of_integer_values(arr)) # [5, 4, 3, 2, 1]


# 10. Write a function to find the duplicate values of an array
def find_duplicate_values_of_array(arr):
    duplicate_values = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                duplicate_values.append(arr[i])
    return list(set(duplicate_values))

arr = [1,2,3,4,5,1,2,3,4,5]
print(find_duplicate_values_of_array(arr)) # [1, 2, 3, 4, 5]


# 11. Write a program to find the common values between two arrays
def find_common_values_between_two_arrays(arr1, arr2):
    common_values = []
    for i in arr1:
        if i in arr2:
            common_values.append(i)
    return list(set(common_values))

arr1 = [1,2,3,4,5]
arr2 = [4,5,6,7,8]
print(find_common_values_between_two_arrays(arr1, arr2)) # [4, 5]


# 12. Write a method to remove duplicate elements from an array
def remove_duplicate_elements_from_array(arr):
    return list(set(arr))

arr = [1,2,3,4,5,1,2,3,4,5]
print(remove_duplicate_elements_from_array(arr)) # [1, 2, 3, 4, 5]


# 13. Write a method to find the second largest number in an array
def find_second_largest_number_in_array(arr):
    arr = list(set(arr))
    arr.sort()
    return arr[-2]

arr = [1,2,3,4,5]
print(find_second_largest_number_in_array(arr)) # 4


# 14. Write a method to find the second largest number in an array
# Same as above 13


# 15. Write a method to find number of even number and odd numbers in an array
def find_number_of_even_number_and_odd_numbers_in_array(arr):
    even = 0
    odd = 0
    for i in arr:
        if i%2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

arr = [1,2,3,4,5]
print(find_number_of_even_number_and_odd_numbers_in_array(arr)) # (2, 3)


# 16. Write a function to get the difference of largest and smallest value
def get_difference_of_largest_and_smallest_value(arr):
    arr.sort()
    return arr[-1] - arr[0]

arr = [1,2,3,4,5]
print(get_difference_of_largest_and_smallest_value(arr)) # 4


# 17. Write a method to verify if the array contains two specified elements(12,23)
def verify_if_array_contains_two_specified_elements(arr, element1, element2):
    if element1 in arr and element2 in arr:
        return True
    return False

arr = [1,2,3,4,5]
element1 = 3
element2 = 5
print(verify_if_array_contains_two_specified_elements(arr, element1, element2)) # True


# 18. Write a program to remove the duplicate elements and return the new array
# Same as above 12

# End of 04_Arrays.py
# Date: 04/07/2024
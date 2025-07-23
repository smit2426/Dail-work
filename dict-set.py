
'''
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)
my_set.add(6)
print(" Adding 6:", my_set)
my_set.remove(3)
print("Removing 3:", my_set)
my_set.add(2)  
print(" Trying to Add Duplicate (2):", my_set)
'''
'''
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print("Original Dictionary:", my_dict)
my_dict['email'] = 'alice@example.com'
print("After Adding Email:", my_dict)
my_dict['age'] = 26
print("After Updating Age:", my_dict)
del my_dict['city']
print("After Removing City:", my_dict)
'''
'''
num_list = [1, 2, 2, 3, 4, 4, 5]
print("Original List:", num_list)
unique_numbers = set(num_list)
print("Unique Numbers:", unique_numbers)
'''
'''
my_list = [1, 2, 3, 3]
my_tuple = (4, 5, 6)
my_set = {7, 8, 9}
list_to_set = set(my_list)
print("List to Set:", list_to_set) 
list_to_tuple = tuple(my_list)
print("List to Tuple:", list_to_tuple) 
tuple_to_list = list(my_tuple)
print("Tuple to List:", tuple_to_list) 
set_to_list = list(my_set)
print("Set to List:", set_to_list)     
set_to_tuple = tuple(my_set)
print("Set to Tuple:", set_to_tuple) 
'''
'''
input_string = "10,20,30,40,50"
list_data = input_string.split(',')
print("List:", list_data)
set_data = set(list_data)
print("Set:", set_data)
tuple_data = tuple(list_data)
print("Tuple:", tuple_data)
'''

unique_integers = {1, 2, 3, 4, 5}
squared_dict = {i: i**2 for i in unique_integers}

print("Squared Dictionary:", squared_dict)

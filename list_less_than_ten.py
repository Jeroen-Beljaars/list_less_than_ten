"""
Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

Instead of printing the elements one by one, 
make a new list that has all the elements less than 5 from this list in it and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that 
contains only elements from the original list a that are smaller than that number given by the user.
"""

"""
Created by Jeroen on 28-11-2017
"""

"""
Remove all the items above under_what_number

Return a list with only numbers below under_what_number
"""
def less_than_five(a_list, under_what_number):
    less_than_five_list = []
    for item in a_list:
        if item < under_what_number:
            less_than_five_list.append(item)
    return less_than_five_list

under_what_number = input("Pick a number (Default is 5) ")
if under_what_number == "":
    under_what_number = 5

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(less_than_five(a, under_what_number))
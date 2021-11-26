# Write a Python program to calculate the sum of a list of numbers


def list_function(elements):
    sum = 0
    for x in elements:
        sum += x
    return sum    

list1 = [1,2,3,4,5] 
print("Sum of the list of numbers : ", list_function(list1))
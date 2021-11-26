# To calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0). 

def series(num):
    if (num < 0):
        return 0
    else:
        num = num + series(num - 2) 
        return num 

number = int(input("Enter a number :"))      
print("Sum = ",series(number))
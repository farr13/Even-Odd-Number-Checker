"""
A function that recieves two numbers as parameters and returns the lesser of the two numbers 
if both numbers are even. if one or both number are odd, the functions returns the greater if the two numbers.
"""
def check_num(num1, num2):
    if (num1 % 2 == 0) and (num2 % 2 == 0):
        if num1 <= num2:
            print(num1)
            return num1
        else:
            print(num2)
            return num1
    else:
        if num1 >= num2:
            print(num1)
            return num1
        else:
            print(num2)
            return num2

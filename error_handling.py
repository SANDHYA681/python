#error handling in python

try:
    result = 5/0
    print(result)
    
except ZeroDivisionError as e: #handle the specific error
 print(e) #print the error message
 
 
try:
    result = 15/0
    print(result)
    
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed") #print the error message
    
try:
    num = int(input("Enter a number: "))
    print(num)
    
except (ValueError, TypeError) as e:
    print("e") #print the error message
    
    
try:
    num1 = int(input("Enter an odd number: "))
    if num1%2 == 0:
        raise ValueError("Number is even")#raise a custom error
    else:
        print(num1)
except ValueError as e:
    print(e) #print the error message
    
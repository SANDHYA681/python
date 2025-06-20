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
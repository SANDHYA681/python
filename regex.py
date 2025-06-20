# regex in python

import re


# #Pattern for regex
# pattern = "test"
# string = "test string"

# # matching the pattern in the string
# if re.match(pattern, string):
#     print("Pattern found in the string")
    
    
#     #search
# if re.search(pattern, string):
#     print("Pattern found in the string")


pattern = r'[a-z]'
string = input("Enter string:")

if re.match(pattern, string):
    print("Pattern matched")
else:
    print("Pattern not found in the string")

# # pattern for regex
# pattern = r'[a-z]'
# # string to search
# string = "Test"

# # matching the pattern 
# match = re.search(pattern, string)
# # print the match
# print(match)




# #matching the pattern in string
# searching_string = re.search(pattern, string)
# # print the match
# print(searching_string)


# match_string = re.match(pattern, string)
# # print the match
# print(match_string)
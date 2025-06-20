# regex in python

import re

# pattern for regex
pattern = r'[a-z]'
# string to search
string = "Test"

# matching the pattern 
match = re.search(pattern, string)
# print the match
print(match)




#matching the pattern in string
searching_string = re.search(pattern, string)
# print the match
print(searching_string)


match_string = re.match(pattern, string)
# print the match
print(match_string)
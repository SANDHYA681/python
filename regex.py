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

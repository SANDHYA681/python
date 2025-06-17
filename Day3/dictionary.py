#dictionary in python
#dictionaly is mutable
#dictionary is unorderd collection of key-value pairs
#key is immutable and value can be mutable or immutable
#key is unique and value can be duplicate
#key is hashable and value can be mutable or immutable


dict1= {
    "name": "John",
    "age": 25,
    "city": "New York",
    "marks": [90, 85, 95],
}

# print(dict1) # Output: {'name': 'John', 'age': 25, 'city': '
# print(dict1.keys()) # printing the keys of the dictionary
# print(dict1.values()) #printing the values of the dictionary
# print(dict1.items()) #printing the items of the dictionary
# print(dict1["email"]) #accessing the value of the key "email"

# for item in dict1.items():
#     print(item) #printing the key-value pairs of the dictionary
    
    
for keys, values in dict1.items():
        print(keys, values) #printing the key-value pairs of the dictionary
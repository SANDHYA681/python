# #dictionary in python
# #dictionaly is mutable
# #dictionary is unorderd collection of key-value pairs
# #key is immutable and value can be mutable or immutable
# #key is unique and value can be duplicate
# #key is hashable and value can be mutable or immutable


dict1= {
    "name": "John",
    "age": 25,
    "city": "New York",
    "marks": [90, 85, 95],
}

# # print(dict1) # Output: {'name': 'John', 'age': 25, 'city': '
# # print(dict1.keys()) # printing the keys of the dictionary
# # print(dict1.values()) #printing the values of the dictionary
# # print(dict1.items()) #printing the items of the dictionary
# # print(dict1["email"]) #accessing the value of the key "email"

#updating the values in dictionary
dict1["age"]=30
#updating the values with update function
dict1.update({"city":"Los Angeles","marks": 25})
print("Dictionary after updating, dict1")


#get function in dictionary
print(dict1.get("name")) #printing the value of the key "name"

#set default function in dictionary
print(dict1.get("email","default")) #printing the value of the key "email" if

# # for item in dict1.items():
# #     print(item) #printing the key-value pairs of the dictionary
    
    
# for keys, values in dict1.items():
#         print(keys, values) #printing the key-value pairs of the dictionary
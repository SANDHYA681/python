#list in python
#list are mutable, i.e they can be modified after creation
list1 = ['Hello', 'World',  'Python', 'Programming', 1, 2.4, True, None, "Hello", 2.4]
#print(list1)# printing whole list
#print(list1[1])# printing through index 

#print(list1[2:5])#printing through index range
#list1.append('Appended String')
#print(list1)

print (len(list1))

#Printing using len function
#for i in range (len(list1)):
    #print(list1[i ], end= "")
    
#printing every items in list using for loop
for item in list1:
    print(item, end="")

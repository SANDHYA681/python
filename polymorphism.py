#polymorphism in python

class A:
    def displayName():
        print("This is class A")
        
        def displayHello():
            print("Hello ")

class B(A):
    #overriding the method of class A
    def displayName():
        print("This is class B")
        

class C(B):
       #overriding the method of class B
    def displayName():
        print("This is class C")
        
obj = A
obj.displayName()  # Output: This is class A

obj1 = B
obj1.displayName()  # Output: This is class B

obj3 = C
obj3.displayName() 
obj3.displayHello()

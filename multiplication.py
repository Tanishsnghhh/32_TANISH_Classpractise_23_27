class Parent:
    def multiplication(self, x, y):
        return x * y

class Child(Parent):
    def takevalue(self):
        x= int(input("Enter  x: "))  
        y = int(input("Enter y: "))
        return self.multiplication(x, y) 
     

hi = Child()  
result = hi.takevalue()  
print(result)



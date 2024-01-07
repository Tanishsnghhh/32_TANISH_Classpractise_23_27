'''class Parent:
    def areaofsquare(self,l):
        return l**2

class Child(Parent):
    def takevalue(self):
        l=int(input("enter length value"))
        return self.areaofsquare (l)

hi = Child()  
result = hi.takevalue()  
print(result)'''




class Parent:
    def add(self, x):
        return x ** 2

class Child(Parent):
    def takevalue(self):
        x= int(input(" The Length "))  
       
        return self.add(x) 
     

hi = Child()  
result = hi.takevalue()  
print(result)




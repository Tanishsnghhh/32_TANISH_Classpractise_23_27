class Parent:
    def add(self, x, y):
        return x + y

class Child(Parent):
    def takevalue(self):
        x= int(input("Enter  x: "))  
        y = int(input("Enter y: "))
        return self.add(x, y) 
     

hi = Child()  
result = hi.takevalue()  
print(result)



class parent():
    def add (self,a,b):
        return a+b
class child(parent):
    def takevalue(self):
        a= int(input("Enter  a: "))  
        b= int(input("Enter  b: ")) 
        return self.add(a,b)

hi= child()
result= hi.takevalue()
print(result)
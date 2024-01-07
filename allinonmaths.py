class Parent:
    def add(self, x):
        return x
    def raidus(self,y):
        return y
    def rectangle(self,l,b):
        return (l,b)

class Child(Parent):

    def takevalue(self):
        x= int(input("Enter The Length "))  
        print("area of square",x ** 2)
        return self.add(x) 
    def takenvalue(self):
        y=int(input("Enter The raidus "))
        print(" raidus of circle",3.14 * y * y )
        return self.raidus(y)
    def valueofrec(self):
        l= int(input("Enter The Length "))
        b=int(input("enter bredth"))
        print(" area of rectangle",l * b )
        return self.rectangle(l,b)
    
hi = Child()  
result = hi.takevalue() 

hi=Child()
result = hi.takenvalue()

hi=Child()
result = hi.valueofrec()



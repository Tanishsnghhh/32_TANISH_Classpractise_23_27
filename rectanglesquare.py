class Shape:
    def area(self,x=None,y=None):
        if(y == None):
            print(self.x*self.x)
        else:
            print(self.x*self.y)


class Square(Shape):

    def takeval(self):
        print(self)
        self.x=int(input("Enter Side"))

class Rectangle(Shape):
    def takeval(self):
        self.x=int(input("Enter Length : "))
        self.y = int(input("Enter Breadth : "))
        

    
a = Square()
b = Rectangle()
a.takeval()
b.takeval()
a.area(a.x)
b.area(b.x,b.y)
class Grandfather():
    def __init__(self):
        self.name="tanish"
        self.landarea=2
        self.money=2

class Father(Grandfather):
    def __init__(self):
        super().__init__()
        self.namee=" ramapati "+ self.name
        self.money=10+self.money
        self.landarea= 6  + self.landarea

class Child(Father):
    def __init__(self,name):
        super().__init__()
        self.name = name + self.namee
        self.money = self.money
        self.landarea = self.landarea
        print("Hello",self.name)
        print("Inherited property: ",self.landarea,"acre")
        print("Purchased property: Rs",self.money,"crore")
        print("Total property: Rs",self.money+self.landarea,"crore")

obj=Child("randeep")


'''class grandfather():
    def __init__(self):
        self.name="tanish"
        self.cash=20,000
        self.flats=5
    
class father():
    def __init__(self):
        super().__init__()
        self.name="singh"
        self.money=self.cash+self.money
        self.flats=self.flats +7
class child():
    def __init__(self,name):
        super().__init__()
        self.name= name+self.name
        self.money=self.money

        print(self.name)'''


'''class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def update_grade(self, new_grade):
        self.grade = new_grade

    def update_name(qt,new_name):
        qt.name = new_name
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

# Usage example:
student1 = Student("Alice", 15, "A")
student1.display_info()    # Output: Name: Alice, Age: 15, Grade: A

student1.update_grade("B")
student1.display_info()    # Output: Name: Alice, Age: 15, Grade: B

student1.update_name("tanish")
student1.display_info() '''




'''class grandfather():
    def __init__(self):
        self.name="tanish"
        self.property="2acre"


class father(grandfather):
    def __init__(self):
        super().__init__(self)
        self.name="singh"+self.name
        self.property=self.property+self.property

class Child(father):
    def __init__(self,name):
        super().__init__()
        self.name = name + self.namee
        self.money = self.money
        self.landarea = self.landarea
        print("Hello",self.name)
        print("Inherited property: ",self.landarea,"acre")
        print("Purchased property: Rs",self.money,"crore")
        print("Total property: Rs",self.money+self.landarea,"crore")
        '''
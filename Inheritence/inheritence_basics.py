class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def show_info(self):
        print(f"My name is {self.name} , i am {self.age} years old")
        
        
        
class Student(Person):
    def __init__(self,name,age,roll_no):
        super().__init__(name,age)
        self.roll_no=roll_no
        
    def show_info(self):
        super().show_info()
        print(f"and my roll no is {self.roll_no}")
s1=Student("wasil",23,44)

s1.show_info()
class Person:
    def __init__(self,name):
        
        self.name=name
        print("Level 1")
    
    def show(self):
        print(f"My name is {self.name}")
class Employee(Person):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary=salary
        print("Level 2")
        
    def show(self):
        super().show()
        print(f"My salary is {self.salary}")
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        print("Level 3")
        self.department=department
    def show(self):
        super().show()
        print(f"Mydepartment is {self.department}")   
        
        
m=Manager("Wasil",100000,"IT")

m.show()


for x in (m):
    print(x)
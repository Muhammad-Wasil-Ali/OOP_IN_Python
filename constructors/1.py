class Person:
    count=0
    def __init__(self,name="wasil",age=23):
        Person.count+=1
        self.name=name
        self.age=age
        self.arr=[1,2,3,4,5]
        
    def displayInfo(self):
        print(f"{self.name} {self.age}")
        print(self.arr)
        print(f"{self.count} objects created")
p1=Person()

p1.displayInfo()


p2=Person("Muhammad Wasil Ali",23)

p2.displayInfo()

p3=Person("Asad butt",22)

p3.displayInfo()
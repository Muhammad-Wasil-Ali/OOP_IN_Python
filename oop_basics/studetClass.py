from typing import List
class Student:
    def __init__(self,name:str="abc",age:int=0,grades:List=None):
        self.name=name,
        self.age=age
        self.grades=grades
    
    def addGrade(self,grade:int):
        if self.grades is None:
            return
        self.grades.append(grade)
    def calculateAverage(self):
        if self.grades is None:
            return "There is not grades of this student"
        sum=0
        for grade in self.grades:
            sum+=grade
        return sum/len(self.grades)
    
    def checkStatus(self):
        
        if self.grades is None:
            
           return
        if self.calculateAverage()>=60:
            print("You are pass")
        else:
            print("You are not qualified")        
        
std1=Student("wasil",23)

std1.addGrade(0)
std1.addGrade(0)


std1.checkStatus()
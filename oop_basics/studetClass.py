class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    
    def averageMarks(self)->float:
        sum=0
        for i in self.marks:
            sum+=i
        return sum/len(self.marks)
    
    

std1=Student("wasil",[98,99,94,92])

print(std1.averageMarks())
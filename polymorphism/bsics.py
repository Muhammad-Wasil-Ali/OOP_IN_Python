class Shape:
    def shape():
        print("the function is presenting shapes")
        
class Circle:
    def shape():
        print("This function is deawing circles")
        
class Reactangle:
    def shape(self):
        print("This function is prsenting reactangle")
        
s1=[Reactangle(),Circle,Shape]

for x in s1:
    
   x.shape()
from typing import List
def reverseArray(arr:List)->int:
    
    for i in range(len(arr),0,-1):
        
        print(i,end=" ")
        
        
arr=[1,2,3,4,5,6,7,8,9]

reverseArray(arr)
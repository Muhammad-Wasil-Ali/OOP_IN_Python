from typing import List
print("Hello world")
def findLargest(arr:List)->int:
    lar=arr[0]
    
    for i in arr:
        if (lar<i):
            lar=i
            
    return lar



def findSmallest(arr:List)->int:
    smallest=arr[0]
    
    for i in arr:
        if (i<smallest):
            smallest=i
            
    
    
    
    return smallest


arr=[1,4,7,2,3,9,-19]
print(f"The largets element in given array is {findLargest(arr)}")

print(f"The largets element in given array is {findSmallest(arr)}")

        
        
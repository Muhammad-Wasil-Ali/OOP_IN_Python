from typing import List
def reverseArray(arr:List)->int:
    
    for i in range(len(arr),0,-1):
        
        print(i,end=" ")
        
        
arr=[1,2,3,4,5]


def optimizeReverseArray(arr:List)->List:
    if len(arr)==0:
        return "Array is empty"
    
    start=0
    end=len(arr)-1
    
    while(start<=end):
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        
        start+=1
        end-=1
        
    return arr


print(optimizeReverseArray(arr))
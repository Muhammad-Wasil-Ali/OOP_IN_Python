from typing import List
def reverse(arr:List,start:int,end:int)->List:
   
    while start<end:
        
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp

        start+=1
        end-=1
        
    return arr
def rotateRight(arr:List,k:int)->List:
    n=len(arr)
    k=k%n
    
    reverse(arr,0,n-1)
    reverse(arr,0,k-1)
    reverse(arr,k,n-1)
    
    return arr


def rotateLeft(arr:List,k:int)->List:
    n=len(arr)
    k=k%n
    
    reverse(arr,0,k-1)
    reverse(arr,k,n-1)
    reverse(arr,0,n-1)
    
    return arr
arr=[1,2,3,4,5]
print(rotateRight(arr,2))

print(rotateLeft([1,2,3,4,5],2))

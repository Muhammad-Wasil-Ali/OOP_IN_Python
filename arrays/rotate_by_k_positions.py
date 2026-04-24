
from typing import List


# brute Force right rotation
def bruteForceRightRotation(arr:List,k:int)->List:
    n=len(arr)
    
    for _ in range(k):
        last=arr[n-1]
        
        for i  in range(n-1,0,-1):
            arr[i]=arr[i-1]
            
        arr[0]=last
        
    
    
    return arr




# brute Force right rotation
def bruteForceLeftRotation(arr:List,k:int)->List:
    n=len(arr)
    
    for _ in range(k):
        first=arr[0]
        
        for i  in range(0,n-1):
            arr[i]=arr[i+1]
            
        arr[n-1]=first
        
    
    
    return arr


# using Big O9(n)



def rightRotate(arr: List[int], k: int) -> List[int]:
    n = len(arr)
    k = k % n
    
    result = [0]*n 
    
    for i in range(n):
        pos = (i + k) % n
        result[pos] = arr[i]
    
    return result


from typing import List

def leftRotate(arr: List[int], k: int) -> List[int]:
    n = len(arr)
    k = k % n
    
    result = [0] * n
    
    for i in range(n):
        pos = (i - k+n) % n
        result[pos] = arr[i]
    
    return result
print(rightRotate([1,2,3,4,5],2))
print(leftRotate([1,2,3,4,5],2))



print(bruteForceLeftRotation([1,2,3,4,5],2))


print(bruteForceRightRotation([1,2,3,4,5],2))


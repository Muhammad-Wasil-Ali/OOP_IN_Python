arr=[1,2,3,4,5,6,7,8]

def linearSearch(arr,element):
    
    n=len(arr)
    
    if n==0:
        return
    for num in range(len(arr)):
        if arr[num]==element:
            print(f"Element found on index {num}")
            break
    

print(linearSearch(arr,5))

arr=[1,2,3,4,5,6,7,8,9]


def binary_search(arr,element):
    start=0
    end=len(arr)-1
    
    while start<=end:
        
        mid=start+(end-start)//2
    
        if(arr[mid]==element):
            return mid
        
        if arr[mid]>element:
             end=mid-1
        if arr[mid]<element:
            start=mid+1
    


print(binary_search(arr,4))
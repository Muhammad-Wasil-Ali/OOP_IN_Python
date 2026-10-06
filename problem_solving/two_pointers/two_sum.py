def two_sum_using_two_pointer(arr,target):
    start=0
    end=len(arr)-1
    result=[]
    while start<end:
        if arr[start]+arr[end]==target:
            result.append((arr[start],arr[end]))
            start+=1
            end-=1
            while start<end and arr[start]==arr[start-1]:
                start+=1
            while start<end and arr[end]==arr[end+1]:
                end-=1
        elif arr[start]+arr[end]<target:
            start+=1
        else:
            end-=1
    
    return result
        
        
print(two_sum_using_two_pointer([1, 2, 2, 3, 4, 6, 8],4)) 

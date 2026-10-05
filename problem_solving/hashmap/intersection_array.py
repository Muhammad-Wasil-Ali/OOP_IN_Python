def intersection_array(arr1,arr2):
    seen1=set(arr1)
    seen2=set(arr2)
    
    
    result=[]
    for num in seen1:
       if num in seen2:
           result.append(num)
    
    
   
        
        
    return result    


print(intersection_array([1,2,3,4],[2,6,7,4]))
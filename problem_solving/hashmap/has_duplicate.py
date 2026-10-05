def has_duplicate(arr):
    
    seen=set()
    
    
    for num in arr:
        if num in seen:
            return True
        else:
            seen.add(num)
            
    return False

print(has_duplicate([1,2,3,4,5]))
        
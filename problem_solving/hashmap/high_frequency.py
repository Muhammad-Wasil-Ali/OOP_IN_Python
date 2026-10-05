
def finding_high_frequency_element(arr):
    result=0
    max_frequency=0
    hashmap={}
    for num in arr:
        if num in hashmap:
            hashmap[num]+=1
        else:
            hashmap[num]=1
        
    for num in arr:
        if hashmap[num]>max_frequency:
            max_frequency=hashmap[num]
            result=num
    
    
    return result
            
print(finding_high_frequency_element([1, 2, 3, 2, 4, 1, 5, 3]))
def two_sum(arr,target):
    
    hashmap={}
    for i in range(0,len(arr)):
        need=target-arr[i]
        print(hashmap.get(need))
        if hashmap.get(need) is not None:
            return [hashmap.get(need),i]
        hashmap[arr[i]]=i
        
    
    return None

print(two_sum([3,2,4],6))
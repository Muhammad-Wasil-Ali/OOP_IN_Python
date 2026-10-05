def is_anagram(s1:str,s2:str):
    
    if len(s1)!=len(s2):
        return False
    
    hashmap={}
    for char in s1:
        if char in hashmap:
            hashmap[char]+=1
        else:
            hashmap[char]=1
    
    
    for char in s2:
        print(hashmap)
        if char in hashmap and hashmap.get(char) > 0:
            hashmap[char]-=1
        else:
            return False
    return True        
    
    



print(is_anagram("silent","listen"))
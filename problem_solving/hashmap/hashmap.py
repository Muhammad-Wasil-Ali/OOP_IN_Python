arr = [4, 5, 2, 4, 2, 7, 5]
freq={}
for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1

print(freq)
first_unique=[]

# by traversing array
for num in arr:
    if freq.get(num,0) and freq.get(num,0)==1:
        first_unique.append(num)
        break
# by traversing object     
for key,value in freq.items():
    if value==1:
        first_unique.append(key)
        break
    
print(first_unique)
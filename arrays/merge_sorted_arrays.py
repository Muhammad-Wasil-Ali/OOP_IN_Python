arr1=[1,3,5,7,9]
arr2=[2,4,6,8,10]
merge=[]
i=0
j=0
while i<len(arr1) and j<len(arr2):
    if arr1[i]<arr2[j]:
        merge.append(arr1[i])
        i+=1
    else:
        merge.append(arr2[j])
        j+=1

while i<len(arr1):
    merge.append(arr1[i])
    i+=1
while j<len(arr2):
    merge.append(arr2[j])
    j+=1


print(merge)
            
    
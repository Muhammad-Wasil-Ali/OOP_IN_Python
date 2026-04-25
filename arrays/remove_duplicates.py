arr=[1,2,3,3,4,4]

# result=[]
# for i in arr:
#     if i not in result:
#         result.append(i)
        
        
# print(result)

j=0
for i in range(1,len(arr)):
    if arr[i]!=arr[j]:
        j+=1
        arr[j]=arr[i]
print(arr[:j+1])
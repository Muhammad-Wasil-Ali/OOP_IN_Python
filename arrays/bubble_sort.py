arr=[5,4,3,2,1]

for i in range(len(arr)-1):
    isSwap=False
    for j in range(0,len(arr)-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            isSwap=True
            
    if not isSwap:
        break
        

print(arr)
arr=[4,5,3,2,1]


for i in range(len(arr)):
    smallestIndex=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[smallestIndex]:
            smallestIndex=j
            
    arr[i],arr[smallestIndex]=arr[smallestIndex],arr[i]
    


print(arr)
arr=[1,2,3,5]
totalSum=float("-inf")
current_sum=0
for i in range(0,len(arr)):
    current_sum+=arr[i]
    
    
    if current_sum>totalSum:
        totalSum=current_sum
        
    if current_sum<0:
        current_sum=0
print(totalSum)
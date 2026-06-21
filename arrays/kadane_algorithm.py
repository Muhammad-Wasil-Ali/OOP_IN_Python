arr=[1,-2,-3,4,5]

print(f"length {len(arr)}")


maxSum=float("-inf")
currentSum=0
# Brute force
for i in range(0,len(arr)):
    currentSum+=arr[i]
    
    if currentSum > maxSum:
        maxSum=currentSum
    if currentSum <0:
        currentSum=0
           
    
    
    
print(maxSum)
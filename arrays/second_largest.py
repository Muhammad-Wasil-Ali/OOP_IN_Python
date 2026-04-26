arr=[1,3,5,2,13,9]


lar=float("-inf")
sec_lar=float("-inf")


for i in range(0,len(arr)):
    if lar <arr[i]:
        sec_lar=lar
        lar=arr[i]
    elif arr[i]>sec_lar and arr[i] <lar:
        sec_lar=arr[i]    
   
        
print(f"largest element in given array is {lar}")

print(f"second largest element in given array is {sec_lar}")

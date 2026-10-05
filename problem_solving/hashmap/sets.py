
def check_number_reapeating(arr):
    
    seen=set()
    
    for num in arr:
        if num in seen:
            return num
        else:
            seen.add(num)
            
print(check_number_reapeating([11,2,3,4,1,4,5]))
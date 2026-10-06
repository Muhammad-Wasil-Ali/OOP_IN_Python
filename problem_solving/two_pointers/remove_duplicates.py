def remove_duplicates(arr):
    
    write=0
    scan=write+1
    
    while scan<len(arr):
        
        if arr[write]!=arr[scan]:
            write+=1
            arr[write]=arr[scan]
        
        scan+=1
        

    return arr[:write+1]


print(remove_duplicates([1, 1, 2, 2, 3, 4, 4]))
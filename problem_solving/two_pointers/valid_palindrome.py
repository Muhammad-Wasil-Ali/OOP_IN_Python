def check_palindrome(text:str):
    
    start=0
    end=len(text)-1
    text=text.lower()
    
    while start<end:
        if not text[start].isalnum():
            start+=1
            continue
        if not text[end].isalnum():
            end-=1
            continue
        
        
        
        if text[start]==text[end]:
            start+=1
            end-=1
        else:
            return False
        
    return True

print(check_palindrome("A man, a plan, a canal: Panama"))
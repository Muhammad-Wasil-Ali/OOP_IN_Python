class User:
    def userInfo():
        print("Hello i am user")
        
        
class Male(User):
    def userInfo():
        print("His gender is male")
        
        
c=[User,Male]

for f in c:
    f.userInfo()
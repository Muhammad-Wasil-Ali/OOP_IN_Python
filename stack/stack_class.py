class Stack:
    def __init__(self):
        self.stack=[]
    
    def push(self,data):
        self.stack.append(data)
    
    def pop(self):
        self.stack.pop()
        
    def isEmpty(self):
        if len(self.stack)==0:
            return True
        else :
            return False
        
    def peek(self):
        return self.stack[-1]
    
    
    def size(self):
        return len(self.stack)


stack=Stack()

print(stack.isEmpty())
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

print(stack.stack)
stack.pop()
print(stack.stack)
print(stack.peek())
print(stack.size())


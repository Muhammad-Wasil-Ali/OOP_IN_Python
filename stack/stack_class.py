class Stack:
    def __init__(self):
        self.stack=[]
    
    def push(self,data):
        self.stack.append(data)
    
    def pop(self):
        if self.isEmpty():
            return "Stack underflow"
        self.stack.pop()
        
    def isEmpty(self):
       return len(self.stack)==0
        
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
            return
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


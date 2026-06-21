class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
# LinkedList class

class Stack:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def push(self,data):
        newNode=Node(data)
        
        if self.head is None:
            self.head=newNode
            self.tail=newNode
            return
        self.tail.next=newNode
        self.tail=newNode
        
    
    def pop(self):
        if self.head is None:
            print("Stack is empty")
            return
        
        current=self.head
        while current:
            current=current.next
            if current.next==self.tail:
                break
        current.next=None
        self.tail=current
    
    
    def peek(self):
        if self.head is None:
            print("Stack is empty")
            return
        
        return self.tail.data
    
    def size(self):
        if self.head is None:
            return 0
        
        current=self.head
        count=0
        while current:
            current=current.next
            count+=1
            
        return count
            
    def traverseStack(self):
        if self.head is None:
            print("Stack is empty")        
            
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
            
        print("None")
        
        
stack=Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.traverseStack()
stack.pop()
stack.traverseStack()
print(f"Top element {stack.peek()} ")

print(stack.size())

       
     
    
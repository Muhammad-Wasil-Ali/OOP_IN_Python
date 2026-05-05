class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def insertAtHead(self,data):
        newNode=Node(data)
       
        
        if not self.head:
            self.head=newNode
            self.tail=newNode
        else:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode
            
    def appendNode(self,data):
        
        newNode=Node(data)
        
       
        if self.head is None:
            self.head=newNode
            self.tail=newNode
            
            return
        current=self.head
        while current.next:
            current=current.next
        
        current.next=newNode
        newNode.prev=current
        self.tail=newNode
        
    # insert at specific position 
    def insertAtSepcificPosition(self,data,position):
        newNode=Node(data)
        size=self.size()+1
        if position>size:
            print(f"Value error you can insert from 0 to {size}")
            return
        if position==1:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode
            return
        if position== size:
            self.tail.next=newNode
            newNode.prev=self.tail
            self.tail=newNode
            return
          
        
        current =self.head
        count=1
        while count!=position:
            current=current.next
            count+=1
        
       
        newNode.next=current.next
        newNode.prev=current
        current.next=newNode
        current.next.prev=newNode
        
              
        
          
    def traverseForward(self)  :
        current=self.head
        
        while current:
            print(current.data,end="<->")
            current=current.next
        print(None)
         
    def traverseBackward(self)  :
        current=self.tail
        
        while current:
            print(current.data,end="<->")
            current=current.prev
        print(None)
    def headAndTail(self):
        print("Head->", self.head.data)
        print("Tail->", self.tail.data)
    
    # linked list size   
    
    def size(self):
        current= self.head
        count=0
        while current:
            count+=1
            current=current.next
        return count
dd=DoublyLinkedList()

dd.appendNode(10)
dd.appendNode(20)
dd.appendNode(30)
dd.appendNode(40)
dd.appendNode(50)
dd.insertAtHead(100)
dd.insertAtSepcificPosition(200,3)
dd.traverseForward()
dd.traverseBackward()
dd.headAndTail()
print(dd.size())
        
        
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
        self.tail.next=newNode
        newNode.prev=self.tail
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
        while  count!=position-1:
            current=current.next
            count+=1
        
       
        newNode.next=current.next
        newNode.prev=current
        current.next.prev=newNode
        current.next=newNode
        
              
    # delete head
    
    def deleteHead(self):
        
        if self.head is None:
            print("List is empty")
            return
        if self.head==self.tail:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.head.prev=None
    def deleteTail(self):
        if self.tail is None:
            print("List is empty")      
            return
        if self.head==self.tail:
            self.head=None
            self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None
            
    # delete node on specific position
    
    def deleteNodeOnSpecificPosition(self,position):
        size=self.size()
        if position < 1 or position > size:
            print(f"Value should be from 1 to {size}")
            return 
        if position==1:
            self.deleteHead()
            return
        if position==size:
            self.deleteTail()
            return
       
        current=self.head
        count=1
        while current and count <position:
            current=current.next
            count+=1
        
        current.next.prev=current.prev
        current.prev.next=current.next
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

dd.appendNode(1000)

dd.deleteHead()
dd.deleteTail()

dd.deleteNodeOnSpecificPosition(6)
dd.deleteNodeOnSpecificPosition(2)

dd.traverseForward()
dd.traverseBackward()
dd.headAndTail()
print(dd.size())
        
        
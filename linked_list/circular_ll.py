class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
        
class CircularLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def appendNode(self,data):
        
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
            newNode.next=newNode
            return
        
        self.tail.next=newNode
        newNode.next=self.head
        self.tail=newNode
    
    # insert at head
    
    def insertHead(self,data):
        
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
            newNode.next=newNode
            return 
        newNode.next=self.head
        self.tail.next=newNode
        self.head=newNode
        
    def insertTail(self,data):
        newNode=Node(data)
        if self.tail is None:
            self.insertHead(data)
            return
        
        self.tail.next=newNode
        newNode.next=self.head
        self.tail=newNode
        
        
    # insert at specific position    
    
    def insertAtSpecificPosition(self,data,position):
        size=self.size()
        newNode=Node(data)
        if position < 1 or position > size+1:
            print(f"You can insert from 1 to {size+1}")
            return
        if position==1:
            self.insertHead(data)
            
            return
        if position==size+1:
            self.insertTail(data)
            return
        
        # inserting specific position
        count=1
        current=self.head
        
           
        while current and count!=position-1:
            current=current.next
            count+=1
               
        newNode.next=current.next
        current.next=newNode
            
            
        
    def deleteHead(self):
        if self.head is None:
            print("List is epmty")
            return
        if slef.head==self.tail:
            self.head=None
            self.tail=None
            return
        self.head=self.head.next
        self.tail.next=self.head
        
    def deleteTail(self):
        if self.tail is None:
            print("List is empty")
            return
        if slef.head==self.tail:
            self.head=None
            self.tail=None
            return
        current=self.head
        
        while True:
            current=current.next
        
            if current.next==self.tail:
                break
        current.next=self.head
        self.tail=current
        
    def deleteAtSpecificPosition(self,position):
        size=self.size()
        
        if position <1 or position >size:
            print("Position is out of bound")
        if position ==1:
            self.deleteHead()
            print("Deleted Successfully")
            return
        if position ==size:
            self.deleteTail()
            print("Deleted Successfully")
            return
        
        count=1
        current=self.head
        while current and count!=position-1:
            current=current.next
            count+=1
        current.next=current.next.next
    # traverse ll
    def traverseCLL(self) :
        current=self.head
        
        while current:
            print(current.data,end="->")
            current=current.next
            
            if current==self.head:
                break
        print("")
        
    def size(self):
        if self.head is None:
            
            return 0
        count=0
        current=self.head
        while True:
            current=current.next
            count+=1
            if current==self.head:
                break
            
        return count
        
    def headAndTail(self):
        if self.head is None:
            print("List is empty")
        print("Head : ",self.head.data)
        print("Tail : ",self.tail.data)
        
cll=CircularLinkedList() 

cll.appendNode(10)
cll.appendNode(20)
cll.appendNode(30)
cll.appendNode(40)

cll.insertHead(90)
cll.insertTail(100)

cll.insertAtSpecificPosition(120,1)
cll.insertAtSpecificPosition(140,4)
cll.deleteHead()
cll.deleteTail()

cll.deleteAtSpecificPosition(3)
cll.deleteAtSpecificPosition(1)

cll.traverseCLL()
cll.headAndTail()
print(f"CLL size is {cll.size()}")

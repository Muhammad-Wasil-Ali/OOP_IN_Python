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
        
    def traverseCLL(self) :
        current=self.head
        
        while current:
            print(current.data,end="->")
            current=current.next
            
            if current==self.head:
                break
        print("")
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
cll.traverseCLL()
cll.headAndTail()

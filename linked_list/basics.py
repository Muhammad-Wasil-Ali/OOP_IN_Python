class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self,head=None):
        self.head=head
        self.tail=None
        
        
    def appendNode(self,data):
        new_node=Node(data)
        
        if self.head is None:
            self.head=new_node
            return
            
        current=self.head
        
        while current.next:
            current=current.next
        
        
        current.next=new_node
    
    
    # delete node
    
    def deleteNode(self,data):
        current=self.head
        prev=None
        
        # case # 1
        
        if current and current.data==data:
            self.head=current.next
            return
        
        # case # 2 searching node
        
        while current and current.data!=data:
            
           prev=current
           current=current.next
        
        
        if current is None:
            print("Valu not found")
            
        prev.next=current.next
        
        
    # insert node 
    
    def insertNode(self,data,position):
        current=self.head
        prev=None
        count=1
        newNode=Node(data)
        if position==1:
            newNode=self.head
            self.head=newNode
            
            return
        
        while current and count!=position:
            
            prev=current
            current=current.next
            count+=1
            
        if current is None:
            print("Position out of bound")
            
        prev.next=newNode
        newNode.next=current
    
    # finding size of linkedlist
    
    def size(self)->int:
        count=0
        current=self.head
        
        while current:
            current=current.next
            count+=1
        return count
    def traverseLinkedList(self):
        current=self.head
        
        while current:
            print(current.data,end="->")
            
            
            current=current.next
        print(None)

    # reverse a linked list by using three pointers method
    
    
    def reverse(self):
        
        prev=None
        current=self.head
        
        while current:
            nextNode=current.next
            current.next=prev
            prev=current
            current=nextNode
            
        self.head=prev
ll=LinkedList()

ll.appendNode(15)
ll.appendNode(20)
ll.appendNode(25)
ll.appendNode(30)
ll.appendNode(35)

ll.insertNode(40,4)
ll.traverseLinkedList()
print(ll.size())
ll.reverse()

ll.traverseLinkedList()
class Node(object):
    def __init__(self,data,next=None):
        self.data=data;
        self.next=next;
    def setData(self,data):
        self.data=data;
    def getData(self):
        return self.data
    def setNext(self,next):
        self.next=next
    def getNext(self):
        return self.next
class LinkedList(object):
    def __init__ (self):
        self.head=None
    def printLinkedList(self):
        temp=self.head
        while(temp):
            print (temp.data,end='')
            temp=temp.next
    def insertAtStart(self,data):
        if self.head==None:
            newNode=Node(data)
            self.head=newNode
        else:
            newNode=Node(data)
            newNode.next=self.head
            self.head=newNode
    def insertBetween(self,previousNode,data):
        if(previousNode.next is None):
            print("Previous node should have next node")
        else:
            newNode=Node(data)
            newNode.next=previousNode.next
            previousNode.next=newNode
    def insertAtEnd(self,data):
        newNode=Node(data)
        temp=self.head
        while(temp.next is None):
            temp=temp.next
        temp.next=newNode
    def delete(self,data):
        temp=self.head
        if(temp.next is not None):
            if(temp.data==data):
                self.head=temp.next
                temp=None
                return
            else:
                while(temp.next !=None):
                    if(temp.data==data):
                        break
                    prev=temp
                    temp=temp.next
                if temp==None:
                    return
                prev.next=temp.next
                return
        def search(self,node,data):
            if node==None:
                return False
            if node.data==data:
                return True
            return self.search(node.getNext(),data)
if __name__ == '__main__':
    List = LinkedList()
    List.head = Node(1)
    List.printLinkedList()
    node2 = Node(2)
    List.head.setNext(node2)
    List.printLinkedList()
    List.insertAtStart(4)
    List.insertBetween(node2, 5)
    List.insertAtEnd(6)
    List.printLinkedList()
    List.delete(3)  # This value does not exist; nothing will happen
    List.printLinkedList()
    print(List.search(List.head, 1))
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
                        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
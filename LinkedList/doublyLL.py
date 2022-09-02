class Node:
    def __init__(self, data = None, next = None, prv = None) -> None:
        self.data = data
        self.next = None
        self.prv = None

class DoublyLL:
    def __init__(self) -> None:
        self.head = None
    
    def insert_beg(self, data):
        if self.head is None:
            node = Node(data)
            self.head = node
        else:
            node = Node(data)
            node.next = self.head
            self.head.prv = node
            self.head = node
    
    def insert_end(self,data):
        if self.head is None:
            print("Linled List is empty...\nHence inserting in begining")
            self.insert_beg(data)
        else:
            node = Node(data)
            n = self.head
            while n.next is not None:
                n = n.next
            
            node.prv = n
            n.next = node
    
    def insert_betweenByKey(self,key,data):
        if self.head is None:
            print("Linked List is empty..")
        else:
            if self.head.data == key:
                self.insert_beg(data)
            else:
                n = self.head
                while n is not None:
                    if n.data == key:
                        break
                    n = n.next
                
                if n is None:
                    print(key," value not in the linked list..")
                elif n.next is None:
                    self.insert_end(data)
                else:
                    node = Node(data)
                    node.next = n.next
                    n.next.prv = node
                    n.next = node
                    node.prv = n



    def delete_front(self):
        if self.head  is None:
            print("Linked List empty..")
        else:
            n= self.head
            self.head = n.next
            n.next.prv = self.head
            n.next = n.prv = None
            print("deleted item ", n.data)
            n = None


    def delete_end(self):
        if self.head is None:
            print("Linked List is empty..")
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.prv.next = None
            print("Deleted item is : ", n.data)
            n = None
    
    def delete_betweenByKey(self, key):
        if self.head is None:
            print("Linked List is empty.")
        else:
            if self.head.data is key:
                self.delete_front()
            else:
                n = self.head
                while n is not None:
                    if n.data == key:
                        break
                    n = n.next
                if n is None:
                    print(key, " is not in the list..")
                else:
                    n.prv.next =  n.next
                    n.next.prv = n.prv
                    n.next = n.prv = None
                    print("Deleted Item is : ", n.data)
                    n = None
                


    def traversal_front(self):
        if self.head is None:
            print("Linked List is empty..")
        else:
            n = self.head
            while n is not None:
                print(n.data,"<-->",end=" ")
                n = n.next
            print("None")
        
        print()

    def traversal_rev(self):
        if self.head is None:
            print("Linked list is empty..")
        else:
            # traverse till the last node
            n = self.head
            while n.next is not None:
                n = n.next

            # traverse reverse
            while n is not self.head:
                print(n.data,"<-->", end=" ")
                n = n.prv
            print(self.head.data," <--> head")
            n = None
        print()

    

if __name__=="__main__":
    print()
    doublyLL = DoublyLL()
    list1 = ['hello', 'this', 'is', 'rachel']
    list2 = [1,2,3,4]
    list1.reverse()
    for i in list1:
        doublyLL.insert_beg(i)
    for (i,j) in zip(list1,list2):
        doublyLL.insert_betweenByKey(i,j)
   
    begList = ['(', ')', '{', '}']
    endList = ['+', '-', '*', '/']
    for i in begList:
        doublyLL.insert_beg(i)
    for i in endList:
        doublyLL.insert_end(i)
    betList = ['addition', 'subtraction', 'multiplication', 'division']

    for (i,j) in zip(endList,betList):
        doublyLL.insert_betweenByKey(i,j)
    doublyLL.traversal_front()
    doublyLL.traversal_rev()
   
    print("DELETION()...\n")
    doublyLL.delete_front()
    doublyLL.delete_front()
    doublyLL.delete_front()
    doublyLL.delete_front()

    doublyLL.traversal_front()
    doublyLL.traversal_rev()
    
    doublyLL.delete_end()
    doublyLL.delete_end()
    doublyLL.delete_end()
    doublyLL.delete_end()

    for i in list1:
        doublyLL.delete_betweenByKey(i)
        
    doublyLL.traversal_front()
    doublyLL.traversal_rev()


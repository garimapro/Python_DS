
class Node:
    def __init__(self, data = None, next = None) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insert_begining(self, data):
        print()
        print("INSERT_BEG")
        node = Node(data)
        node.next = self.head
        self.head = node
        print("Updated list :")
        self.traversal()
    
    def insert_end(self, data):
        print()
        print("INSERT_END")
        if self.head is None:
            print("List is empty..hence inserting at beginning of the list..")
            self.insert_begining(data)
        else:
            node = Node(data)
            n = self.head
            while n.next is not None:
                n = n.next
            
            n.next = node
            print("Updated List :")
            self.traversal()

    def insert_betweenByVal(self,data, value):
        print()
        print("INSERT_IN_BETWEEN")
        if self.head is None:
            print("List is empty..hence inserting at beginning of the list..")
            self.insert_begining(data)
        else:
            n = self.head
            while n is not None:
                if n.data == val:
                    break
                n = n.next
            
            if n is None:
                print("value not in the list")
            else:
                node = Node(data)
                node.next = n.next
                n.next = node
                print("Updated Linked List :")
                self.traversal()
            

    def delete_front(self):
        print()
        print("DELETE_FRONT_NODE")
        if self.head is None:
            print("Lnked list is empty..")
        else:
            print("Linked List Before Deletion : ")
            self.traversal()
            n = self.head
            self.head = n.next
            print("deleted node is : ", n.data)
            n = None
            print("Updated Linked List : ")
            self.traversal()


    def delete_end(self):
        print()
        print("DELETE_LAST_NODE")
        if self.head is None:
            print("Linked List is empty") # Underflow condition
        else:
            n = self.head
            prv = n
            while n.next is not None:
                prv = n
                n = n.next
            print("deleted item is : ", n.data)
            prv.next = None
            n = None
            print("Updated List is : ")
            self.traversal()
                

    def delete_byValue(self, key):
        print()
        print("DELETE_BY_VALUE")
        if self.head is None:
            print("Linked List is empty..")
        else:
            if self.head.data is key:
                self.delete_front()
            else:
                n = self.head
                prv = n
                while n is not None:
                    if key == n.data:
                        break
                    prv = n.next

                if n is None:
                    print(key," key not in Linked List")
                else:
                    prv.next = n.next
                    n = None
                    print("Updated Linked List :")
                    self.traversal()



    def traversal(self):
        if self.head is None:
            print("Linked List is empty..")
        else:
            node = self.head
            while node is not None:
                print(node.data, end="")
                print("-->", end="")
                node = node.next
            print()


if __name__=="__main__":
    print()
    linkedList_obj = LinkedList()
    # linkList =  [10,200,30,40,5]
    # linkList2 = ['hello', 'bye', 'day', 'night', 'morning']
    # for i in linkList:
    #     linkedList_obj.insert_begining(i)
    # # for j in linkList2:
    # #     linkedList_obj.insert_end(j)

    # for (i,j) in zip(linkList2,linkList):
    #     linkedList_obj.insert_betweenByVal(i,j)
    
    # # for (i,j) in zip(linkList,linkList2):
    # #     print(i,j)
    

  
    
    while True:
        print()
        print("Enter choice: \n1.INSERT\t2.DELETE\t3.TRAVERSAL\t4.EXIT")
        choice = int(input())
        if choice == 1:
            print("Enter the data of the node:\t")
            data = input()
            print("Choose \n1.INSERT_BEG\t2.INSERT_END\t3.INSERT_IN_BETWEEN")
            i = int(input())
            if i == 1:
                linkedList_obj.insert_begining(data)
            elif i == 2:
                linkedList_obj.insert_end(data)
            elif i == 3:
                print("Enter the value where to insert: ")
                val = input()
                linkedList_obj.insert_betweenByVal(data, val)
        
        elif choice == 2:
            print("Choose \n1.DELETE_BEG\t2.DELETE_END\t3.DELETE_IN_BETWEEN")
            i = int(input())
            if i == 1:
                linkedList_obj.delete_front()
            elif i == 2:
                linkedList_obj.delete_end()
            elif i == 3:
                print("Enter the value to be deleted: ")
                val = input()
                linkedList_obj.delete_byValue(val)

        elif choice == 3:
            linkedList_obj.traversal()
        
        elif choice == 4:
            print("THANK YO1U...")
            exit()
        
    # linkedList_obj.traversal()
    print()
# def top_t_words(words,t):

#     freqWord = words[0]

#     for i in range(1,t):
#         temp = words.count(words[i])
#         if temp >= words.count(freqWord):
#             if temp == words.count(freqWord):
#                 if words[i] < freqWord:
#                     freqWord = words[i]
#             else:
#                 freqWord = words[i]
#     return freqWord

# i = 5
# print(type(i))
# print(type("hello",i,"garima"))

# list1 = ['hello', 'this', 'is', 'rachel']
# list1.reverse()
# print(list1)

class Node:
    def __init__(self, data = None, next = None, prv = None) -> None:
        self.data = data
        self.next = None
        self.prv = None

class DoublyLL:
    def __init__(self) -> None:
        self.head = None
    
    def insert_beg(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        node.prv = self.head
    
    def printN(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            n = None
            print("n = ",n)
            print("head", self.head.data)

if __name__=="__main__":
    dll = DoublyLL()
    list1 = ['hello', 'this', 'is', 'rachel']
    list1.reverse()
    for i in list1:
        dll.insert_beg(i)
    dll.printN()
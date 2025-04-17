class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def addLast(self, val: int) -> Node:
        if not self.head:
            self.head = Node(val, None)
            return self.head
            
        temp = self.head
        while temp and temp.next:
            temp = temp.next
        temp.next = Node(val, None)
        return self.head
    
    def addFirst(self, val: int) -> Node:
        if not self.head:
            return self.addFirst(val)
        self.head = Node(val, self.head)
        return self.head

    def printList(self) -> None:
        temp = self.head
        print("start => ")
        while temp:
            print(temp.val, " -> ")
            temp = temp.next
        print("end")

    def bubbleSort(self) -> Node:
        if not (self.head and self.head.next):
            return self.head
        
        swapped = True
        while swapped:
            swapped = False
            temp = self.head
            while temp and temp.next:
                if temp.val > temp.next.val:
                    localTemp = temp.val
                    temp.val = temp.next.val
                    temp.next.val = localTemp
                    swapped = True
                temp = temp.next
        
        return self.head

    def sort_from_absolute(self) -> Node:
        temp = self.head
        while temp and temp.next:
            if temp.next.val < 0:
                to_move = temp.next
                temp.next = to_move.next
                to_move.next = self.head
                self.head = to_move
            else:
                temp = temp.next

        return self.head
    
node: LinkedList = LinkedList()
for el in [1, 2, 3, -4, 5, 6, -7, -8, -9, 10]:
    node.addLast(el)
# node.printList()
node.sort_from_absolute()
node.printList()
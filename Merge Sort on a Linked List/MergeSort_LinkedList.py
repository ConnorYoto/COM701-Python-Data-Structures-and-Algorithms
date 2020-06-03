class Node:
    
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
        
    def setHead(self, head):
        self.head = head

    def setTail(self, node):
        self.tail = node
        
    def getHead(self):
        return self.head
    
    def getTail(self):
        return self.tail
    
class MergeSortList:
    
    def __init__(self):
        self.head = None
        
    def add(self, head):
        tempNode = Node(head)
        tempNode.setTail(self.head)
        self.head = tempNode
        del tempNode
        
    def print(self):
        current = self.head
        if current is None:
            print("Empty List!!!")
            return False

        while current:
            print(str(current.getHead()), end=" ")
            current = current.tail
            if current:
                print("-->", end=" ")
        print()
        
    def sortedMerge(self, a, b):
        result = None
        
        # Base Cases for the recursion
        if a == None:
            return b
        if b == None:
            return a
        
        if a.head <= b.head:
            result = a
            result.tail = self.sortedMerge(a.tail, b)
        else:
            result = b
            result.tail = self.sortedMerge(a, b.tail)
        return result
    
    def mergeSort(self, h):
        # linkedlist <= 1 aka Base Case
        if h == None or h.tail == None:
            return h
        
        # Find middle of lsit for split
        midpoint = self.findMiddle(h)
        midpointnext = midpoint.tail
        
        # Break list in two
        midpoint.tail = None
        
        # Merge Sort Left Side of List
        leftside = self.mergeSort(h)
        
        # Merge Sort Right Side of List
        rightside = self.mergeSort(midpointnext)
        
        # Merge Left and Right Lists
        sortedList = self.sortedMerge(leftside, rightside)
        return sortedList
        

    
        
# Splitting the List down the middle for merge sort
    def findMiddle(self, head):
        if (head == None):
            return head
        
        slow = head
        fast = head
        
        while (fast.tail != None and fast.tail.tail != None):
            slow = slow.tail
            fast = fast.tail.tail
            
        return slow


# Creating Object
myList = MergeSortList()

# Creating Elements
myList.add(77)
myList.add(56)
myList.add(49)
myList.add(62)
myList.add(69)

myList.head = myList.mergeSort(myList.head)

myList.print()

# I have chosen to implement Merge Sort because it is considered as
# one of the most efficient sorting algorithms with regards to Linked Lists
# The complexity of this algorithm is O(nlogn)
    
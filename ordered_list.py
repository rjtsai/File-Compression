class Node:
    '''Node for use with doubly-linked list'''
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

    def getItem(self):
        return self.item
    
    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setNext(self, newNext):
        self.next = newNext

    def setPrev(self, newPrev):
        self.prev = newPrev

    def __repr__(self):
        return '%s' % (self.item)

class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''

    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           DO NOT have an attribute to keep track of size'''
        self.dummy = Node(None)
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy

    def is_empty(self):
        '''Returns True if OrderedList is empty
            MUST have O(1) performance'''
        if self.dummy.getNext() == self.dummy:
            return True

    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list) and returns True.
           If the item is already in the list, do not add it again and return False.
           MUST have O(n) average-case performance'''
        if self.dummy.getNext() == self.dummy:
            newNode = Node(item)
            self.dummy.setNext(newNode)
            newNode.setNext(self.dummy)
            self.dummy.setPrev(newNode)
            newNode.setPrev(self.dummy)
        else:
            newNode = Node(item)
            nxt = self.dummy.getNext()
            prev = self.dummy
            while nxt != self.dummy and newNode.getItem() > nxt.getItem():
                prev = prev.getNext()
                nxt = nxt.getNext()
            if newNode.getItem() == nxt.getItem():
                return False
            else:
                prev.setNext(newNode)
                newNode.setPrev(prev)
                newNode.setNext(nxt)
                nxt.setPrev(newNode)
        return True

            

    def remove(self, item):
        '''Removes the first occurrence of an item from OrderedList. If item is removed (was in the list) 
          returns True.  If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        if not self.search(item):
            return False
        nxt = self.dummy.getNext()
        prev = self.dummy
        while nxt != self.dummy:
            if nxt.getItem() == item:
                nxt.getNext().setPrev(prev)
                prev.setNext(nxt.getNext())
                return True
            prev = nxt
            nxt = nxt.getNext()
        


    def index(self, item):
        '''Returns index of the first occurrence of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''
        
        if not self.search(item):
            return None
        nxt = self.dummy.getNext()
        idx = 0
        while item != nxt.getItem():
            nxt = nxt.getNext()
            idx += 1
        return idx
        '''
        index = 0
        start = self.dummy
        while index < self.size():
            if start.getItem() == item:
                return index
            else:
                start= start.getNext()
                index += 1
        '''
    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        if index < 0 or index >= self.size():
            raise IndexError
        idx = 0
        nxt = self.dummy.getNext()
        prev = self.dummy
        while idx < index:
            prev = nxt
            nxt = nxt.getNext()
            idx += 1
        temp = nxt.getItem()
        prev.setNext(nxt.getNext())
        nxt.getNext().setPrev(prev)
        return temp

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        return self.sameItem(self.dummy.getNext(), item)

    def sameItem(self, nxt, item):
        if nxt == self.dummy:
            return False
        if item == nxt.getItem():
            return True
        return self.sameItem(nxt.getNext(), item)

    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        OrdList = []
        nxt = self.dummy.getNext()
        while nxt != self.dummy:
            OrdList.append(nxt.getItem())
            nxt = nxt.getNext()
        return OrdList

    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        return self.revList_helper(self.dummy.getPrev(), revList = [])

    def revList_helper(self, prev, revList):
        if prev == self.dummy:
            return revList
        else:
            revList.append(prev.getItem())
            return self.revList_helper(prev.getPrev(), revList)      


    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        return self.sizeHelper(self.dummy.getNext())

    def sizeHelper(self, node):
        if node is self.dummy:
            return 0
        return 1 + self.sizeHelper(node.getNext())

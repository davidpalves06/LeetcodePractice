class DequeNode:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None


class MyCircularDeque:

    def __init__(self, k: int):
        self.root = None
        self.count = 0
        self.length = k
        

    def insertFront(self, value: int) -> bool:
        if self.count == self.length:
            return False
        newNode = DequeNode(value)
        newNode.next = self.root
        self.root = newNode
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.count == self.length:
            return False
        newNode = DequeNode(value)
        if (self.root == None):
            self.root = newNode
        else:
            curr = self.root
            while(curr.next != None):
                curr = curr.next
            curr.next = newNode
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.count == 0:
            return False
        self.root = self.root.next
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.count == 0:
            return False
        curr = self.root
        ant = None
        while(curr.next != None):
            ant = curr
            curr = curr.next
        if (ant == None):
            self.root = None
        else:
            ant.next = None
        self.count -= 1
        return True

        

    def getFront(self) -> int:
        if (self.count == 0):
            return -1
        return self.root.value

    def getRear(self) -> int:
        if (self.count == 0):
            return -1
        curr = self.root
        while (curr.next != None):
            curr = curr.next
        return curr.value

    def isEmpty(self) -> bool:
        if (self.count == 0):
            return True
        return False

    def isFull(self) -> bool:
        if (self.count == self.length):
            return True
        return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
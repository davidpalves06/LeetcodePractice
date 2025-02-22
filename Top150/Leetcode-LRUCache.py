class ListNode:
    def __init__(self, x,val):
        self.key = x
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.values = {}
        self.capacity = capacity
        self.left,self.right = ListNode(-1,0),ListNode(-1,0)
        self.left.next,self.right.prev = self.right,self.left

    def remove(self,node):
        prev,next= node.prev,node.next
        prev.next = next
        next.prev = prev

    def insert(self,node):
        prev = self.right.prev
        prev.next = node
        self.right.prev = node
        node.prev,node.next = prev,self.right


    def get(self, key: int) -> int:
        if key in self.values:
            self.remove(self.values[key])
            self.insert(self.values[key])
            return self.values.get(key).val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.values:
            self.remove(self.values[key])
        
        self.values[key] = ListNode(key,value)
        self.insert(self.values[key])
        if (len(self.values) > self.capacity):
            lru = self.left.next
            self.remove(lru)
            del self.values[lru.key]

        return
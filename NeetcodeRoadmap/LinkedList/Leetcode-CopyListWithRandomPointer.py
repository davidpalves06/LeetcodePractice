# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyMap = {}
        curr = head
        while curr:
            copyMap[curr] = Node(curr.val)
            curr = curr.next              

        curr = head
        while curr:
            newNode = copyMap.get(curr)
            newNode.next = copyMap.get(curr.next)       
            newNode.random = copyMap.get(curr.random)
            curr = curr.next
        
        return copyMap.get(head)
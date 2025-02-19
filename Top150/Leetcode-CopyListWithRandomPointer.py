from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeMap = {}

        tracker = head
        while tracker:
            nodeMap[tracker] = Node(tracker.val)
            tracker = tracker.next
        
        tracker = head
        while tracker:
            newNode = nodeMap[tracker]
            newNode.next = nodeMap.get(tracker.next,None)
            newNode.random = nodeMap.get(tracker.random,None)
            tracker = tracker.next

        return nodeMap.get(head,None)
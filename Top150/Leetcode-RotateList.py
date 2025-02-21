from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        length = 0
        curr = head 
        while curr:
            length += 1
            curr = curr.next
        
        rotations = length - (k % length)
        if rotations == length:
            return head
        curr = head
        firstLeftNode = head
        firstRightNode = None
        ant = None
        i = 0
        while curr:
            if i == rotations:
                if ant:
                    ant.next = None
                firstRightNode = curr
            i += 1
            ant = curr
            curr = curr.next
        
        head = firstRightNode
        ant.next = firstLeftNode

        return head

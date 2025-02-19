from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        curr = head
        ant = None
        k = n
        while length - k > 0:
            ant = curr
            k += 1
            curr = curr.next
        
        if ant:
            if curr:
                ant.next = curr.next
        else:
            if curr:
                head = curr.next
            else:
                head = None
        return head
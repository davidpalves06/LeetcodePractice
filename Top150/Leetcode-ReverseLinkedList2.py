from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head

        ant = None
        startNode = None
        leftNode = None
        rightNode = None

        i = 1
        while curr:
            if i == left - 1:
                startNode = curr
            elif i == left:
                leftNode = curr
                while curr and i <= right:
                    rightNode = curr
                    tmp = curr.next
                    curr.next = ant
                    ant = curr
                    curr = tmp
                    i += 1
                if startNode:
                    startNode.next = rightNode
                else:
                    head = rightNode
                leftNode.next = curr
            i += 1
            if curr:
                curr = curr.next


        return head



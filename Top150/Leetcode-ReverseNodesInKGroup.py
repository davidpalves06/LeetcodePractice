from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next

        first = None
        curr = head

        while length >= k:
            count = 0
            leftNode = curr
            rightNode = None
            while count < k:
                tmp = curr.next
                curr.next = rightNode
                rightNode = curr
                curr = tmp
                count += 1
            
            leftNode.next = curr
            if first:
                first.next = rightNode
            else:
                head = rightNode

            first = leftNode
            length -= k

        return head 
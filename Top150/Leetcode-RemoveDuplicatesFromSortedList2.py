from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        ant = None
        while curr:
            num = curr.val
            firstNode = curr
            curr = curr.next
            duplicates = 0
            while curr and curr.val == num:
                duplicates += 1
                curr = curr.next

            if duplicates > 0:
                if ant:
                    ant.next = curr
                else:
                    head = curr
            else:
                ant = firstNode
        return head

        
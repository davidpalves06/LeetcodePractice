# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next.next

        while fast and fast.next and slow != fast:
            slow = slow.next
            fast = fast.next.next

        if slow == fast:
            return True
        else:
            return False

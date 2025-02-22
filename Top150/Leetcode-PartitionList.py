from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        biggerList = ListNode()
        tmp = biggerList
        curr = head
        ant = None
        while curr:
            if curr.val >= x:
                tmp.next = ListNode(curr.val)
                tmp = tmp.next
                if ant:
                    ant.next = curr.next
                else:
                    head = curr.next
            else:
                ant = curr
            curr = curr.next

        if ant:
            ant.next = biggerList.next
        else:
            head = biggerList.next
        return head

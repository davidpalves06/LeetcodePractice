from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def gcd(a, b):
    if (a < b):
        return gcd(b,a)
    while b != 0:
        a, b = b, a % b
    return a

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr,next = head,head.next;
        while(next != None):
            value = gcd(curr.val,next.val)
            curr.next = ListNode(value,next)
            curr,next = next,next.next;
        return head;
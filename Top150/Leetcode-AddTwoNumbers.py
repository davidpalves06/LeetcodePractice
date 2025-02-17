from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = False

        lengthL1 = 0
        lengthL2 = 0
        currL1 = l1
        currL2 = l2
        while currL1:
            lengthL1 += 1
            currL1 = currL1.next
        while currL2:
            lengthL2 += 1
            currL2 = currL2.next
        if lengthL1 < lengthL2:
            l1,l2 = l2,l1

        head = ListNode()
        currRes = head
        currL1 = l1
        currL2 = l2
        while currL1 != None:
            value = currL1.val
            currL1 = currL1.next
            if currL2 != None:
                value += currL2.val
                currL2 = currL2.next
            
            if carry:
                value += 1
                carry = False
            
            if value >= 10:
                carry = True
                value = value % 10
            
            currRes.next = ListNode(value)

            currRes = currRes.next

        if carry:
            currRes.next = ListNode(1)
            currRes = currRes.next
        
        return head.next



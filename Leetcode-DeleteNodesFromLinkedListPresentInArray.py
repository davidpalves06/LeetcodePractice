# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        numSet = set()
        for num in nums:
            numSet.add(num)
        
        ant = None;
        current = head;
        while(current != None):
            if(numSet.__contains__(current.val)):
                if(ant == None):
                    head = current.next;
                else:
                    ant.next = current.next;
            else:
                ant = current        
            current = current.next;
        return head
        
            
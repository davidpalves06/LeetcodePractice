# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
from typing import Optional


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        linkedLength = self.calculateLength(head);
        response = [];
        currentNode = head
        currentPartLength = 0
        remainingParts = k;
        partLength = math.ceil(linkedLength / k)
        while (currentNode != None):
            currentPartLength+=1;
            if (currentPartLength == partLength):
                finalNode = currentNode
                currentNode = currentNode.next
                finalNode.next = None
                response.append(head);
                currentPartLength = 0;
                head = currentNode
                linkedLength -= partLength;
                remainingParts-=1;
                if (remainingParts != 0):
                    partLength = math.ceil(linkedLength / remainingParts)
            else:
                currentNode = currentNode.next
        while (response.__len__() < k):
            response.append(None)              
        return response;
    
    def calculateLength(self,head):
        linkedLength = 0
        currentNode = head
        while(currentNode != None):
            linkedLength+=1;
            currentNode = currentNode.next;
        return linkedLength;
        
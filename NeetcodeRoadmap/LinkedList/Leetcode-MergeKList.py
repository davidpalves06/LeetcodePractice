# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List, Optional


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) < 1:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0,len(lists),2):
                list1 = lists[i]
                list2 = lists[i+1] if i + 1 < len(lists) else None
                mergedList = self.mergeLists(list1,list2)
                mergedLists.append(mergedList)
            lists = mergedLists

        return lists[0]


    def mergeLists(self,list1,list2):
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            curr = curr.next
        
        curr.next = list1 if list1 else list2
        return dummy.next
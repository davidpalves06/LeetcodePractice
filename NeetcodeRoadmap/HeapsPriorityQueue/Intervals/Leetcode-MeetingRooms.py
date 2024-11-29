from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class TreeNode:
    def __init__(self,interval):
        self.interval = interval
        self.right = None
        self.left = None

class Tree:
    def __init__(self) -> None:
        self.head = None
    
    def insert(self,node):
        if not self.head:
            self.head = node
            return True
        curr = self.head
        while curr:
            if curr.interval.start > node.interval.end:
                if not curr.left:
                    curr.left = node
                    return True
                curr = curr.left
            elif curr.interval.end <= node.interval.start:
                if not curr.right:
                    curr.right = node
                    return True
                curr = curr.right 
            else:
                return False
        
        

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        head = Tree()
        for interval in intervals:
            if not head.insert(TreeNode(interval)):
                return False
        return True
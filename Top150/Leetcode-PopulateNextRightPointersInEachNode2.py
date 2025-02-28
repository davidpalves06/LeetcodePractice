from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        queue = deque()
        queue.append(root)

        while queue:
            ant = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if ant:
                    ant.next = node
                ant = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ant.next = None

        return root
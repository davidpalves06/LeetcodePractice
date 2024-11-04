from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left,right = 0 , 0
        q = deque()
        res = []

        while right < len(nums):
            while q and q[-1] < nums[right]:
                q.pop()
            q.append(nums[right])
            if right - left + 1 >= k:
                res.append(q[0])
                if nums[left] >= q[0]:
                    q.popleft()
                left += 1
            right += 1

        return res
        
print(Solution.maxSlidingWindow(None,[1],1))
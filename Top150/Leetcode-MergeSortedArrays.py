from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i,j = 0,0

        while j < n:
            if i == m:
                while j < n:
                    nums1[i + j] = nums2[j]
                    j += 1
            else:
                if nums1[i + j] > nums2[j]:
                    k = m + n - 1
                    while k > i + j:
                        nums1[k] = nums1[k - 1]
                        k -= 1
                    nums1[i + j] = nums2[j]
                    j += 1
                else:
                    i += 1
        
        print(nums1)
        
        

(Solution.merge(None,nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
(Solution.merge(None,nums1 = [1], m = 1, nums2 = [], n = 0))
(Solution.merge(None,nums1 = [0], m = 0, nums2 = [1], n = 1))
(Solution.merge(None,nums1 = [2,0], m = 1, nums2 = [1], n = 1))
        
            
        
from typing import List



class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1,nums2
        if len(nums1) > len(nums2):
            A,B = nums2,nums1
        
        total = len(nums1) + len(nums2)
        half = total // 2
        left,right = 0,len(A) - 1

        median = None
        while median == None:
            halfA = (left + right) // 2
            halfB = half - halfA - 2

            Aleft = A[halfA] if halfA >= 0 else float("-infinity")
            Aright = A[halfA + 1] if halfA + 1 < len(A) else float("infinity")
            Bleft = B[halfB] if halfB >= 0 else float("-infinity")
            Bright = B[halfB + 1] if halfB + 1 < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    median = min(Aright,Bright)
                else:
                    median = (max(Aleft,Bleft) + min(Aright,Bright)) / 2
            else:
                if Aleft > Bright:
                    right = halfA - 1
                else:
                    left = halfA + 1
        return median
    
print(Solution.findMedianSortedArrays(None,[0,0],[0,0]))
            

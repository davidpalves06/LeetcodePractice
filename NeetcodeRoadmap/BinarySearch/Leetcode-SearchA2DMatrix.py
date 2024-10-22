from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left,right = 0,len(matrix) - 1
        targetRow = -1
        while left <= right:
            pivotIndex = left + ((right - left) // 2)
            pivotFirst = matrix[pivotIndex][0]
            pivotLast = matrix[pivotIndex][len(matrix[pivotIndex]) - 1]
            if pivotFirst <= target and pivotLast >= target:
                targetRow = pivotIndex
                break
            if pivotFirst > target:
                right = pivotIndex - 1
            if pivotLast < target:
                left = pivotIndex + 1
        
        if targetRow == -1: return False

        left,right = 0,len(matrix[targetRow]) - 1

        while left <= right:
            pivotIndex = left + ((right - left) // 2)
            pivot = matrix[targetRow][pivotIndex]
            if pivot == target:
                return True
            if pivot < target:
                left = pivotIndex + 1
            if pivot > target:
                right = pivotIndex - 1

        return False



print(Solution.searchMatrix(None,[[1,3,5,7],[10,11,16,20],[23,30,34,60]],60))

import heapq


class MedianFinder:

    def __init__(self):
        self.left,self.right = [],[]

    def addNum(self, num: int) -> None:
        if self.right and self.right[0] < num:
            heapq.heappush(self.right,num)
        else:
            heapq.heappush(self.left, -1 * num)

        if len(self.left) > len(self.right) + 1:
            largestFromLeft = -1 * heapq.heappop(self.left)
            heapq.heappush(self.right,largestFromLeft)
        if len(self.right) > len(self.left) + 1:
            largestFromRight = -1 * heapq.heappop(self.right)
            heapq.heappush(self.left,largestFromRight)

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -1 * self.left[0]
        elif len(self.right) > len(self.left):
            return self.right[0]
        else:
            return (-1 * self.left[0] + self.right[0]) / 2
from collections import defaultdict
from typing import List


class DetectSquares:
    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.pts:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)

detectSquares = DetectSquares()

detectSquares.add([5,10])
detectSquares.add([10,10])
detectSquares.add([10,5])
print(detectSquares.count([5,5]))
detectSquares.add([3,0])
detectSquares.add([8,0])
detectSquares.add([8,5])
print(detectSquares.count([3,5]))
detectSquares.add([9,0])
detectSquares.add([9,8])
detectSquares.add([1,8])
print(detectSquares.count([0,8]))
"add","add","add","count"
detectSquares.add([0,0]) 
detectSquares.add([8,0])
detectSquares.add([8,8])
print(detectSquares.count([0,8]))
[[1,9]],[[2,9]],[[2,10]],[[1,10]],[[7,8]],[[2,3]],[[2,8]],[[7,3]]
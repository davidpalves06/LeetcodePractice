import heapq
from typing import List


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        indexes = [i for i in range(len(times))]
        indexes.sort(key=lambda i: times[i][0])

        availableChairs = [i for i in range(len(times))]
        usedChairs = []

        for index in indexes:
            time = times[index]

            while usedChairs and usedChairs[0][0] <= time[0]:
                availableChair = heapq.heappop(usedChairs)[1]
                heapq.heappush(availableChairs,availableChair)


            chair = heapq.heappop(availableChairs)
            heapq.heappush(usedChairs,(time[1],chair))

            if (index == targetFriend):
                return chair



print(Solution.smallestChair(None,[[3,10],[1,5],[2,6]],0))
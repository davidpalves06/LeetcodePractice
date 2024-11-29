from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        replaceInterval = newInterval
        for interval in intervals:
            if not replaceInterval:
                res.append(interval)
                continue
            if interval[0] > replaceInterval[1]:
                res.append(replaceInterval)
                replaceInterval = []
                res.append(interval)
            elif interval[1] < replaceInterval[0]:
                res.append(interval)
            else:
                replaceInterval[0] = min(interval[0],replaceInterval[0])
                replaceInterval[1] = max(interval[1],replaceInterval[1])
        
        if replaceInterval:
            res.append(replaceInterval)
        return res
    
print(Solution.insert(None,[[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))
"""
Definition of Interval:
"""
from collections import defaultdict
from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        pointMap = defaultdict(int)

        for interval in intervals:
            pointMap[interval.start] += 1
            pointMap[interval.end] -= 1

        concurrent = 0
        res = 0
        for key in sorted(pointMap.keys()):
            concurrent += pointMap[key]
            res = max(res,concurrent)

        return res
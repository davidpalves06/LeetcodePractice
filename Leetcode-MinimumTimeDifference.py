from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutesPoints = []
        for timePoint in timePoints:
            pointSplit = timePoint.split(":");
            minutes = (int(pointSplit[0]) * 60) + (int(pointSplit[1]))
            minutesPoints.append(minutes);
            
        minutesPoints.sort();
        currentMinimum = 1500;
        for i in range(len(minutesPoints) - 1):
            firstPoint = minutesPoints[i];
            secondPoint = minutesPoints[i+1];
            if (secondPoint - firstPoint < currentMinimum):
                currentMinimum = secondPoint - firstPoint;
                if (currentMinimum == 0):
                    return currentMinimum;
        
        circularWrap =  minutesPoints[0] + 1440 - minutesPoints[len(minutesPoints) - 1];
        if (circularWrap < currentMinimum):
            return circularWrap;
        else:
            return currentMinimum;
                    
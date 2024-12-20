class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        twoStairDown = 1
        oneStairDown = 2

        for i in range(3,n+1):
            oneStairDown,twoStairDown = oneStairDown + twoStairDown,oneStairDown


        return oneStairDown 

print(Solution.climbStairs(None,10))

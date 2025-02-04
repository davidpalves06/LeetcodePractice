from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = [1] * len(ratings)

        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                res[i] = res[i-1] + 1
        
        for i in range(len(ratings) - 2,-1,-1):
            if ratings[i] > ratings[i + 1]:
                res[i] = max(res[i],res[i+1] + 1)

        return sum(res) 
    

print(Solution.candy(None,ratings = [1,0,2]))
print(Solution.candy(None,ratings = [1,2,2]))
print(Solution.candy(None,[1,3,2,2,1]))
print(Solution.candy(None,[1,2,87,87,87,2,1]))
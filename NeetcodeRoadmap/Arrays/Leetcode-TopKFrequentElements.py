from collections import Counter
from typing import List


class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     counter = Counter(nums)
    #     res = []
    #     for key,count in counter.items():
    #         print(res)
    #         inserted = False
    #         for i in range(len(res)):
    #             if (counter.get(res[i]) < count):
    #                 res.insert(i,key)
    #                 inserted = True
    #                 break

    #         if (len(res) > k):
    #             res.pop()
    #         elif len(res) < k and not inserted:
    #             res.append(key)
    #     return res

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]
        res = []
        for key,count in counter.items():
            freq[count].append(key)

        for i in range(len(nums),-1,-1):
            frequency = freq[i]
            for num in frequency:
                res.append(num)
            if (len(res) >= k):
                break
        return res[0:k]

print(Solution.topKFrequent(None,[7,7],1))
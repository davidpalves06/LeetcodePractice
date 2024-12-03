from collections import defaultdict
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOcurrence = defaultdict(int)
        
        for i in range(len(s)):
            lastOcurrence[s[i]] = i

        res = []
        begin = 0
        end = 0
        for i in range(len(s)):
            letterEnd = lastOcurrence[s[i]]

            end = max(end,letterEnd)
            
            if i == end:
                res.append(end - begin + 1)
                begin = i + 1

        return res
                


print(Solution.partitionLabels(None,"ababcbacadefegdehijhklij"))
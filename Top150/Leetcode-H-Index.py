from collections import defaultdict
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # citations.sort()
        # papers = 1
        # res = 0
        # for i in range(len(citations) - 1,-1,-1):
        #     res = max(res,min(papers,citations[i]))
        #     papers += 1

        res = 0
        paper_counts = [0] * (len(citations) + 1)

        for citation in citations:
            if citation >= len(citations):
                paper_counts[len(citations)] += 1
            else:
                paper_counts[citation] += 1

        for i in range(len(paper_counts) - 1,-1,-1):
            res += paper_counts[i]
            if res >= i:
                return i
 
print(Solution.hIndex(None,citations = [3,0,6,1,5]))
print(Solution.hIndex(None,citations = [1,3,1]))
            
        
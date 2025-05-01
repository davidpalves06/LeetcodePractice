from collections import deque


class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        
        def isPossibleMutation(gene,anotherGene):
            count = 0
            for i in range(0,8):
                if gene[i] != anotherGene[i]:
                    count += 1
                
            return count == 1

        visited = set()
        queue = deque()
        queue.append(startGene)
        res = 0
        while queue:
            for _ in range(len(queue)):
                gene = queue.popleft()
                if gene == endGene:
                    return res
                for nextGene in bank:
                    if nextGene not in visited and isPossibleMutation(gene,nextGene):
                        queue.append(nextGene)

                visited.add(gene)

            res = res + 1

        return -1
    
print(Solution.minMutation(None,startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]))
print(Solution.minMutation(None,startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]))
class Solution:
    def minSwaps(self, s: str) -> int:
        counter = 0
        swaps = 0
        for c in s:
            if c == '[':
                counter += 1
            if c == ']':
                if counter == 0:
                    swaps+=1
                    counter +=1
                else:
                    counter -= 1
        return swaps


print(Solution.minSwaps(None,"][]["))
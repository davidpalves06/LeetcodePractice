from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterMapping = {
            "2":'abc',
            "3":'def',
            "4":'ghi',
            "5":'jkl',
            "6":'mno',
            "7":'pqrs',
            "8":'tuv',
            "9":'wxyz'
        }

        res = []
        if not digits:
            return res
        def backtrack(cur,i):
            if i == len(digits):
                res.append(''.join(cur))
                return
            
            digit = digits[i]
            digitMap = letterMapping[digit]

            for mapping in digitMap:
                cur.append(mapping)
                backtrack(cur,i+1)
                cur.pop()

        backtrack([],0)
        return res
    
print(Solution.letterCombinations(None,''))
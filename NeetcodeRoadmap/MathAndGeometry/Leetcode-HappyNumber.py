class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n != 1:
            digits = list(str(n))
            newNumber = 0
            for digit in digits:
                newNumber += pow(int(digit),2)
            
            if newNumber in visited:
                return False
            visited.add(newNumber)
            n = newNumber

        return True
    
print(Solution.isHappy(None,2))
print(Solution.isHappy(None,19))
print(Solution.isHappy(None,100))
print(Solution.isHappy(None,101))

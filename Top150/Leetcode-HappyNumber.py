class Solution:
    def isHappy(self, n: int) -> bool:
        slowNumber = n
        fastNumber = n
        tmp = 0
        while fastNumber > 0:
            square = pow(fastNumber % 10, 2)
            tmp += square
            fastNumber = fastNumber // 10
        
        fastNumber = tmp

        while slowNumber != 1 and fastNumber != 1:
            if slowNumber == fastNumber:
                return False
            
            for _ in range(2):
                tmp = 0
                while fastNumber > 0:
                    square = pow(fastNumber % 10, 2)
                    tmp += square
                    fastNumber = fastNumber // 10
                fastNumber = tmp

            tmp = 0
            while slowNumber > 0:
                square = pow(slowNumber % 10, 2)
                tmp += square
                slowNumber = slowNumber // 10
            slowNumber = tmp
        return True
    
print(Solution.isHappy(None,19))
print(Solution.isHappy(None,2))
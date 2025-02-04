class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = [[] for _ in range(numRows)]
        currRow = 0
        down = True
        for c in s:
            res[currRow].append(c)
            if down and currRow == numRows - 1:
                down = False
            elif not down and currRow == 0:
                down = True
            if down:
                currRow += 1
            else:
                currRow -= 1

        zigzag = ""
        for row in res:
            zigzag += "".join(row)
        return zigzag
    
print(Solution.convert(None,s = "PAYPALISHIRING", numRows = 3))
print(Solution.convert(None,s = "PAYPALISHIRING", numRows = 4))
print(Solution.convert(None,s = "A", numRows = 1))
print(Solution.convert(None,s = "ABC", numRows = 1))
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        curr = 0
        last = 0
        for c in s:
            if c == ' ':
                if curr != 0:
                    last = curr
                curr = 0
            else:
                curr += 1
        if curr != 0:
            last = curr
        return last
    
print(Solution.lengthOfLastWord(None, s = "Hello World"))
print(Solution.lengthOfLastWord(None,s = "   fly me   to   the moon  "))
print(Solution.lengthOfLastWord(None,s = "luffy is still joyboy"))
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right = 0,0
        maxLength = 0
        charUsed = set()
        currLength = 0
        while right < len(s):
            if s[right] not in charUsed:
                charUsed.add(s[right])
                right += 1
                currLength += 1
                maxLength = max(maxLength,currLength)
            else:
                while s[right] in charUsed:
                    charUsed.remove(s[left])
                    left += 1
                    currLength -= 1
        
        return maxLength
    
print(Solution.lengthOfLongestSubstring(None,s = "abcabcbb"))
print(Solution.lengthOfLongestSubstring(None,s = "bbbbb"))
print(Solution.lengthOfLongestSubstring(None,s = "pwwkew"))

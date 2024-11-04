class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}

        left = 0
        maxRepeating = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right],0)

            maxRepeating = max(maxRepeating,count[s[right]])

            if (right - left + 1) - maxRepeating > k:
                count[s[left]] = count[s[left]] - 1
                left += 1

        return (right - left + 1)
    
print(Solution.characterReplacement(None,"ABLMBFGBIJBMZZ",1))
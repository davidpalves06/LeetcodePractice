class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedInput = ""
        for c in s:
            if c.isalpha() or c.isalnum():
                cleanedInput += c.lower()

        l,r = 0,len(cleanedInput) -1
        while l < r:
            if cleanedInput[l] != cleanedInput[r]:
                return False
            l += 1
            r -= 1
        return True
    
print(Solution.isPalindrome(None,s = "A man, a plan, a canal: Panama"))
print(Solution.isPalindrome(None,s = "A an, a plan, a canal: Panama"))
print(Solution.isPalindrome(None,s = "race a car"))
print(Solution.isPalindrome(None,s = " "))
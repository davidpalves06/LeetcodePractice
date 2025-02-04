class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        curr = ""
        for c in s:
            if c == ' ':
                if curr != "":
                    res.append(curr)
                curr = ""
            else:
                curr += c
        
        if curr != "":
            res.append(curr)
        return " ".join(res[::-1])

print(Solution.reverseWords(None,s = "the sky is blue"))
print(Solution.reverseWords(None,s = "  hello world  "))
print(Solution.reverseWords(None,s = "a good   example"))
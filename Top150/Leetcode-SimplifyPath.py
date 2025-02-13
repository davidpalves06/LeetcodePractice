class Solution:
    def simplifyPath(self, path: str) -> str:
        splittedPath = path.split("/")
        stack = []
        for dir in splittedPath:
            if dir == "..":
                if stack:
                    stack.pop()
            elif dir == ".":
                continue
            elif dir != "":
                stack.append(dir)

        res = "/"
        i = 0
        while i < len(stack):
            dir = stack[i]
            res += dir
            i += 1
            if i < len(stack):
                res += "/"
        return res 

print(Solution.simplifyPath(None,path = "/home/"))
print(Solution.simplifyPath(None,path = "/home//foo/"))
print(Solution.simplifyPath(None,path = "/home/user/Documents/../Pictures"))
print(Solution.simplifyPath(None,path = "/../"))
print(Solution.simplifyPath(None,path = "/.../a/../b/c/../d/./"))
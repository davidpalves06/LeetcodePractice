from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = {}
        res = []
        visited = set()

        for i in range(len(equations)):
            equation = equations[i]
            value = values[i]
            a,b = equation
            if (a in adjList):
                adjList[a].append({"variable":b,"value":value})
            else:
                adjList[a] = [{"variable":b,"value":value}]
            if (b in adjList):
                adjList[b].append({"variable":a,"value":1/value})
            else:
                adjList[b] = [{"variable":a,"value":1/value}]

        def dfs(a:str,b:str):
            if (a in visited):
                return -1.0
            visited.add(a)
            if (a == b):
                return 1.0
            for neighbour in adjList[a]:
                result = dfs(neighbour["variable"],b)
                if (result != -1.0):
                    return result * neighbour["value"]
            return -1.0

        for query in queries:
            a,b = query
            if a not in adjList or b not in adjList:
                res.append(-1.0)
            else:
                visited = set()
                res.append(dfs(a,b))
        return res
    
print(Solution.calcEquation(None,equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))
print(Solution.calcEquation(None,equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))
print(Solution.calcEquation(None,equations = [["a","b"],["c","d"]], values = [1.0,1.0], queries = [["a","c"],["b","d"],["b","a"],["d","c"]]))
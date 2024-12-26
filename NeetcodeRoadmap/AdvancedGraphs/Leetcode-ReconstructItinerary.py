from collections import defaultdict
import heapq
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)
        for ticket in sorted(tickets):
            source,dest = ticket
            adjList[source].append(dest)
        
        res = []
        # def dfs(node,path: list):
        #     nonlocal res
        #     if res != []:
        #         return
        #     if len(path) == len(tickets) + 1:
        #         res = path.copy()
        #         return

        #     for i,edge in enumerate(adjList[node]):
        #         adjList[node].pop(i)
        #         path.append(edge)
        #         dfs(edge,path)
        #         path.pop()
        #         adjList[node].insert(i,edge)

        def dfs(node):
            while adjList[node]:
                edge = adjList[node].pop(0)
                dfs(edge)
            res.append(node)
        dfs("JFK")
        return res[::-1]
        
print(Solution.findItinerary(None,[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
print(Solution.findItinerary(None,[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
print(Solution.findItinerary(None,[["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
print(Solution.findItinerary(None,[["JFK","SFO"],["JFK","ATL"],["SFO","JFK"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"]]))

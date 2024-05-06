import collections
import heapq
from typing import List
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u,v,w in times:
            edges[u].append((v,w))  #  v for destination and w for path in u list
        minHeap = [(0,k)] # if k = 2
        visit = set()
        t = 0
        while minHeap:
            w1,n1 = heapq.heappop(minHeap)  #w1 = 0 and n1 = 2
            if n1 in visit:
                continue
            visit.add(n1)   # visit = 2
            t = max(t,w1)  # t = 0
            for n2,w2 in edges[n1]:  # first two list of edges because n1 is 2
                if n2 not in visit:
                    heapq.heappush(minHeap,(w1+w2,n2))
        return t if len(visit) == n else -1
from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for ui, vi, ti in times:
            edges[ui].append((ti, vi))

        visited_node = set()
        total_time = 0
        #start_node
        min_heap = [(0, k)]
        heapq.heapify(min_heap)
        while min_heap:
            t1, u1 = heapq.heappop(min_heap)
            if u1 in visited_node:
                continue
            visited_node.add(u1)
            total_time = max(total_time, t1)
            for t2, u2 in edges[u1]:
                if u2 not in visited_node:
                    heapq.heappush(min_heap, (t1+t2, u2))
        return -1 if len(visited_node) != n else total_time
            



        
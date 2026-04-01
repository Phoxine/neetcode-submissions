import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for i in range(len(points)):
            distance = points[i][0] ** 2 + points[i][1] ** 2
            min_heap.append((distance, points[i][0], points[i][1]))

        min_heap = heapq.nsmallest(k, min_heap)
        # print(results)
        return [[e[1], e[2]] for e in min_heap]
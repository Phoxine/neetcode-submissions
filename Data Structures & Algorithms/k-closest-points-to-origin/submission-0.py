import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for i in range(len(points)):
            distance = points[i][0] ** 2 + points[i][1] ** 2
            min_heap.append((distance, points[i][0], points[i][1]))

        results = heapq.nsmallest(k, min_heap)
        # print(results)
        return [[result[1], result[2]] for result in results]
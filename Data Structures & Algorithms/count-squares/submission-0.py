from collections import defaultdict

# count([1,1])
# -> [2, 2]
# find [1,2], [2, 1]

# count([1, 1])
# -> [2, 1]
# 
class CountSquares:

    def __init__(self):
        self.point_storage = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.point_storage[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in list(self.point_storage.keys()):
            # only check diagonal endpoints
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            res += self.point_storage[(x, py)] * self.point_storage[(px, y)] * self.point_storage[(x, y)]
        return res

        

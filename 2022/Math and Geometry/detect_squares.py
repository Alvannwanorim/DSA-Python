from collections import defaultdict
from typing import List


class DetectSquares:
    def __init__(self) -> None:
        self.ptsCounts = defaultdict(int)
        self.pts = []
    
    def add(self, point: List[int]) -> None:
        self.ptsCounts[tuple(point)] +=1
        self.pts.append(point)
        # print(self.pts)
        # print(self.ptsCounts)
    
    def count(self, point: List[int])->int:
        res = 0

        px, py = point

        for x, y in self.pts:
            if(abs(py - y) != abs(px - x) or x == px or y == py ):
                continue
            print(self.ptsCounts[(px, y)])
            print(self.ptsCounts[(x, py)])
            res += self.ptsCounts[(x, py)] * self.ptsCounts[(px, y)]
            # print(res)
        return res

sol = DetectSquares()
sol.add([3, 10])
sol.add([11, 2])
sol.add([3, 2])
# sol.count([11, 10])
sol.count([14, 8])
sol.add([11, 2])
print(sol.count([11, 10]))
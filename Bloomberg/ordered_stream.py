from typing import List


class OrderedStream:
    def __init__(self, n: int) -> None:
        self.stream =[""] * (n + 1)
        self.ptr = 1
    
    def insert(self, id: int, value: str) -> List[str]:
        self.stream[id] = value
        res = []

        if id == self.ptr:
            while self.ptr < len(self.stream) and self.stream[self.ptr]:
                res.append(self.stream[self.ptr])
                self.ptr += 1
            
            return res
orderedStream =OrderedStream(5)
print(orderedStream.insert(3, "ccccc"))
print(orderedStream.insert(1, "aaaaa"))
print(orderedStream.insert(2, "bbbbb"))
print(orderedStream.insert(5, "eeeee"))
print(orderedStream.insert(4, "ddddd"))

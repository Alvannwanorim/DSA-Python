from typing import List
class OrderedStream:

    def __init__(self, n: int):
        self.stream= [""] * (n + 1)
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value

        res = []

        if idKey == self.ptr:
            while self.ptr < len(self.stream) and self.stream[self.ptr]:
                res.append(self.stream[self.ptr])
                self.ptr += 1
        
        return res

os = OrderedStream(5)
print(os.insert(3, "ccccc"))
print(os.insert(1, "aaaaa"))
print(os.insert(2, "bbbbb"))
print(os.insert(5, "eeeee"))
print(os.insert(4, "ddddd"))
import random


class RandomizedCollection:

    def __init__(self):
        self.numList = []
        self.hasMap = {}

    def insert(self, val: int) -> bool:
        res = val not in self.hasMap

        if res:
            self.hasMap[val] = len(self.numList)
            self.numList.append(val)
        return res
        

    def remove(self, val: int) -> bool:
        res = val in self.hasMap
        if res:
            indx = self.hasMap[val]
            lastVal = self.numList[-1]
            self.numList[indx] = lastVal
            self.numList.pop()
            del self.hasMap[val]
        return res

    def getRandom(self) -> int:
        return random.choice(self.numList)

rad = RandomizedCollection()
print(rad.insert(1))
print(rad.insert(2))
print(rad.insert(3))
print(rad.getRandom())
print(rad.getRandom())
print(rad.remove(1))
print(rad.getRandom())
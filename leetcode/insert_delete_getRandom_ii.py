from collections import defaultdict
import random


class RandomizedCollection:

    def __init__(self):
        self.numList = []
        self.hasMap = defaultdict(set)

    def insert(self, val: int) -> bool:
        res = val in self.hasMap
        indx = len(self.numList)
        self.hasMap[val].add(indx)
        self.numList.append(val)
        return res
        

    def remove(self, val: int) -> bool:
        if not self.hasMap[val]:
            return False
        index = self.hasMap[val].pop()
        last_val = self.numList[-1]
        self.numList[index] = last_val
        self.hasMap[last_val].add(index)
        self.hasMap[last_val].remove(len(self.numList) -1)
        
        if len(self.hasMap[val]) == 0:
            del self.hasMap[val]
        self.numList.pop()
        print(self.hasMap)
        return True
    

    def getRandom(self) -> int:
        return random.choice(self.numList)

rad = RandomizedCollection()
print(rad.insert(1))
print(rad.insert(2))
print(rad.insert(2))
# print(rad.getRandom())
# print(rad.getRandom())
print(rad.remove(1))
print(rad.getRandom())
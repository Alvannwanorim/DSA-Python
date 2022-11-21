from collections import defaultdict
import random


class RandomizedCollection:

    def __init__(self):
        self.numList = []
        self.hasMap = defaultdict(list)

    def insert(self, val: int) -> bool:
       return True
        

    def remove(self, val: int) -> bool:
       return False

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
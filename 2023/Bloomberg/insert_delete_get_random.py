import random 


class RandomizedSet:

    def __init__(self):
        self.table = {}
        self.stack = []

    def insert(self, val: int) -> bool:
        if not val in self.table:
            lastIndex = len(self.stack)
            self.stack.append(val)
            self.table[val] = lastIndex
            return True 
        return False


    def remove(self, val: int) -> bool:
        if val in self.table:
            valIndex = self.table[val]
            lastVal = self.stack[-1]
            self.table[lastVal] = valIndex
            self.stack[valIndex] = lastVal
            self.stack.pop()
            del self.table[val]
            return True
        return False


    def getRandom(self) -> int:
        return random.choice(self.stack)

sol = RandomizedSet()
print(sol.insert(0))
print(sol.insert(1))
print(sol.remove(0))
print(sol.insert(2))
print(sol.remove(1))
print(sol.getRandom()) 


# ["RandomizedSet","insert","insert","remove","insert","remove","getRandom"]
# [[],[0],[1],[0],[2],[1],[]]
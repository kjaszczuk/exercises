import random
class RandomizedSet:
    def __init__(self):
        self.Rset = set()

    def insert(self, val: int) -> bool:
        if val not in self.Rset:
            self.Rset.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.Rset:
            self.Rset.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        random.choice(self.Rset) # WON'T WORK CAUSE choice argument has to be subscriptable (e.g. a list)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

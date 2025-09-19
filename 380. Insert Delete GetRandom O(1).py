import random
class RandomizedSet:

    def __init__(self):
        self.lst = []

    def search(self, val):
        return val in self.lst

    def insert(self, val: int) -> bool:
        if not self.search(val):
            self.lst.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if self.search(val):
            self.lst.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.lst)
# doesn't work cause searching in list in O(n) not O(1) and list.pop() requires index as an argument not a value 



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

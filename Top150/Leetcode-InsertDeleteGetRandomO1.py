import random


class RandomizedSet:

    def __init__(self):
        self.items = {}

    def insert(self, val: int) -> bool:
        if val not in self.items:
            self.items[val] = val
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.items:
            del self.items[val]
            return True
        return False

    def getRandom(self) -> int:
        items = list(self.items.values())
        if len(items) == 1:
            return items[0]
        randomIndex = random.randint(0,len(items) - 1)
        return items[randomIndex]
        


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.insert(1))
print(obj.remove(2))
print(obj.insert(2))
print(obj.getRandom())
print(obj.remove(1))
print(obj.insert(2))
print(obj.getRandom())

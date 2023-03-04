from collections import OrderedDict


class LRUCache1(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int):
        if key not in self.cache:
            return -1
        value = self.cache[key]
        self.cache.pop(key)
        self.cache[key] = value
        return value

    def put(self, key: int, value: int):
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        else:
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)
            self.cache[key] = value

obj = LRUCache1(3)
obj.put(1, 11)
obj.put(2, 33)
obj.put(4, 178)
param_1 = obj.get(1)
print(param_1)
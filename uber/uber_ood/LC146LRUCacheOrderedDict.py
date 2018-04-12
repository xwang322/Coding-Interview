class LRUCache(object):

    def __init__(self, capacity):
        self.dictionary = collections.OrderedDict()
        self.remain = capacity
        # capacity cannot be called from another function


    def get(self, key):
        if key not in self.dictionary:
            return -1
        value = self.dictionary[key]
        self.dictionary.pop(key)
        self.dictionary[key] = value
        return value


    def put(self, key, value):
        if key in self.dictionary:
            self.dictionary.pop(key)
            self.dictionary[key] = value
        else:
            if self.remain == 0:
                self.dictionary.popitem(last=False)
                # last = False is like pop(0)
            else:
                self.remain -= 1
            self.dictionary[key] = value



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class Node(object):
    def __init__(self, k, v):
        # the role of key here is to remove the node by the node count, when updating the dictionary, based on node.key
        self.key = k
        self.value = v
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        self.head = Node(0, 0)
        self.tail = Node(float('inf'), float('inf'))
        self.capacity = capacity
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dictionary = {}

    def get(self, key):
        if key in self.dictionary:
            temp = self.dictionary[key]
            self._remove(temp)
            self._add(temp)
            return self.dictionary[key].value
        return -1

    def put(self, key, value):
        if key in self.dictionary:
            self._remove(self.dictionary[key])
            new = Node(key, value)
            self._add(new)
            self.dictionary[key] = new
        else:
            new = Node(key, value)
            self._add(new)
            self.dictionary[key] = new
        if len(self.dictionary) > self.capacity:
            temp = self.head.next
            self._remove(temp)
            del self.dictionary[temp.key]

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = p

obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
obj.get(1)
obj.put(3,3)
obj.get(2)
obj.put(4,4)
obj.get(1)
obj.get(3)
obj.get(4)
print obj.dictionary.keys(), [obj.dictionary[node].key for node in obj.dictionary], [obj.dictionary[node].value for node in obj.dictionary] 

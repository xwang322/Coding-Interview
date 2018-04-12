class Node(object):
    # for double linked list, simply deleting is not O(1), but with the dict help, it is O(1)
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        self.remain = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        # self.dictionary store the key->node relationship, this is priority
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
        if len(self.dictionary) > self.remain:
            temp = self.head.next
            self._remove(temp)
            del self.dictionary[temp.key]


    def _add(self, node):
        p = self.tail.prev
        p.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = p

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class Node(object):
    def __init__(self, count):
        self.count = count
        self.prev = None
        self.next = None


class AllOne(object):

    def __init__(self):
        self.string_int = {}
        self.int_node = {}
        self.int_string = {}
        self.head = Node(0)
        self.tail = Node(float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head
        self.int_node[0] = self.head
        self.int_node[float('inf')] = self.tail


    def inc(self, key):
        if key not in self.string_int:
            self.string_int[key] = 0
        former_count = self.string_int[key]
        former_node = self.int_node[former_count]
        self.string_int[key] += 1
        if former_node.next.count != self.string_int[key]:
            new_node = Node(self.string_int[key])
            self._add(former_node, new_node)
            self.int_node[self.string_int[key]] = new_node
            self.int_string[self.string_int[key]] = set()
            self.int_string[self.string_int[key]].add(key)
        else:
            self.int_string[self.string_int[key]].add(key)
        if former_count != 0:
            self.int_string[former_count].remove(key)
            if len(self.int_string[former_count]) == 0:
                self.int_node.pop(former_count)
                self.int_string.pop(former_count)
                self._remove(former_node)


    def dec(self, key):
        if key not in self.string_int:
            return
        later_count = self.string_int[key]
        later_node = self.int_node[later_count]
        self.string_int[key] -= 1
        if self.string_int[key] == 0:
            self.string_int.pop(key)
        else:
            if later_node.prev.count != self.string_int[key]:
                new_node = Node(self.string_int[key])
                self._add(later_node.prev, new_node)
                self.int_node[self.string_int[key]] = new_node
                self.int_string[self.string_int[key]] = set()
                self.int_string[self.string_int[key]].add(key)
            else:
                self.int_string[self.string_int[key]].add(key)
        self.int_string[later_count].remove(key)
        if len(self.int_string[later_count]) == 0:
            self._remove(self.int_node[later_count])
            self.int_node.pop(later_count)
            self.int_string.pop(later_count)


    def getMaxKey(self):
        if self.head.next == self.tail:
            return ''
        x = self.int_string[self.tail.prev.count].pop()
        self.int_string[self.tail.prev.count].add(x)
        return x


    def getMinKey(self):
        if self.head.next == self.tail:
            return ''
        x  =self.int_string[self.head.next.count].pop()
        self.int_string[self.head.next.count].add(x)
        return x

    def _add(self, former_node, node):
        temp = former_node.next
        temp.prev = node
        node.next = temp
        former_node.next = node
        node.prev = former_node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

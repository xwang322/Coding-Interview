class Node(object):
    def __init__(self, cnt):
        self.counts = cnt
        self.prev = None
        self.next = None


class AllOne(object):

    def __init__(self):
        self.key_string_value_int = {}
        self.key_int_value_node = {}
        self.key_int_value_string = {}
        self.head = Node(0)
        self.tail = Node(float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_int_value_node[0] = self.head
        self.key_int_value_node[float('inf')] = self.tail


    def inc(self, key):
        if key not in self.key_string_value_int:
            self.key_string_value_int[key] = 0

        former_count = self.key_string_value_int[key]
        former_node = self.key_int_value_node[former_count]
        self.key_string_value_int[key] += 1
        if former_node.next.counts != self.key_string_value_int[key]:
            new_node = Node(self.key_string_value_int[key])
            self._add(former_node, new_node)
            self.key_int_value_node[self.key_string_value_int[key]] = new_node
            self.key_int_value_string[self.key_string_value_int[key]] = set()
        self.key_int_value_string[self.key_string_value_int[key]].add(key)

        if former_count != 0:
            self.key_int_value_string[former_count].remove(key)
            if len(self.key_int_value_string[former_count]) == 0:
                self._remove(former_node)
                self.key_int_value_node.pop(former_count)
                self.key_int_value_string.pop(former_count)


    def dec(self, key):
        if key not in self.key_string_value_int:
            return
        later_count = self.key_string_value_int[key]
        later_node = self.key_int_value_node[later_count]
        self.key_string_value_int[key] -= 1
        if self.key_string_value_int[key] == 0:
            self.key_string_value_int.pop(key)
        else:
            if self.key_string_value_int[key] != later_node.prev.counts:
                new_node = Node(self.key_string_value_int[key])
                self._add(later_node.prev, new_node)
                self.key_int_value_node[self.key_string_value_int[key]] = new_node
                self.key_int_value_string[self.key_string_value_int[key]] = set()
            self.key_int_value_string[self.key_string_value_int[key]].add(key)

        self.key_int_value_string[later_count].remove(key)
        if len(self.key_int_value_string[later_count]) == 0:
            self._remove(later_node)
            self.key_int_value_node.pop(later_count)
            self.key_int_value_string.pop(later_count)


    def getMaxKey(self):
        if self.head.next == self.tail:
            return ''
        x = self.key_int_value_string[self.tail.prev.counts].pop()
        self.key_int_value_string[self.tail.prev.counts].add(x)
        return x


    def getMinKey(self):
        if self.head.next == self.tail:
            return ''
        x = self.key_int_value_string[self.head.next.counts].pop()
        self.key_int_value_string[self.head.next.counts].add(x)
        return x

    def _add(self, former_node, node):
        temp = former_node.next
        temp.prev = node
        node.next = temp
        former_node.next = node
        node.prev = former_node

    def _remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next



# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

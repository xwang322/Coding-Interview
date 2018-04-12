class Vector2D(object):
    # O(n) space solution, straightforward
    '''
    def __init__(self, vec2d):
        self.vec1d = [element for row in vec2d for element in row]
        self.count = 0

    def next(self):
        self.count += 1
        return self.vec1d[self.count-1]

    def hasNext(self):
        if self.count < len(self.vec1d):
            return True
        return False
    '''
    # this method O(1) space, complex but efficiency
    def __init__(self, vec2d):
        self.row = 0
        self.col = 0
        self.vec2d = vec2d

    def next(self):
        self.col += 1
        return self.vec2d[self.row][self.col-1]

    def hasNext(self):
        # use while not if is because there might be a row with []
        while self.row < len(self.vec2d) and self.col >= len(self.vec2d[self.row]):
            self.row += 1
            self.col = 0
        return self.row < len(self.vec2d)


# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())

class HitCounter(object):
    ''' using double side queue
    def __init__(self):
        from collections import deque
        self.total = 0
        self.record = deque()
        

    def hit(self, timestamp):
        if not self.record or self.record[-1][0] != timestamp:
            self.record.append([timestamp, 1])
        else:
            self.record[-1][1] += 1
        self.total += 1

    def getHits(self, timestamp):
        while self.record and self.record[0][0] <= timestamp-300:
            self.total -= self.record.popleft()[1]
        return self.total
    ''' 
    # using dict
    def __init__(self):
        self.dict = collections.defaultdict(int)
    
    def hit(self, timestamp):
        self.dict[timestamp] += 1
    
    def getHits(self, timestamp):
        startstamp = timestamp -299
        if startstamp <= 0:
            startstamp = 0
        total = 0
        for i in range(startstamp, timestamp+1):
            total += self.dict[i]
        return total
    


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
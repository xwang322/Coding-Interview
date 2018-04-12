class Logger(object):

    def __init__(self):
        self.dictionary = {}

    def shouldPrintMessage(self, timestamp, message):
        if message not in self.dictionary:
            self.dictionary[message] = timestamp
            return True
        else:
            if timestamp - self.dictionary[message] < 10:
                return False
            else:
                self.dictionary[message] = timestamp
                return True



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

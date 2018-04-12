import string
import random

class Codec:
    def __init__(self):
        self.dictionary = {}
        
    def encode(self, longUrl):
        choices = string.ascii_letters + string.digits
        tiny = 'http://tinyurl.com/' + ''.join(random.choice(choices) for i in range(6))
        self.dictionary[tiny] = longUrl
        return tiny

    def decode(self, shortUrl):
        return self.dictionary[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
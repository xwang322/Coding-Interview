import random
import string
class Codec:
    def __init__(self):
        self.dictionary = {}

    def encode(self, longUrl):
        choices_db = string.ascii_letters+string.digits
        tiny_url = 'http://tinyurl.com/'+''.join(random.choice(choices_db) for i in range(6))
        self.dictionary[tiny_url] = longUrl
        return tiny_url

    def decode(self, shortUrl):
        return self.dictionary[shortUrl]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

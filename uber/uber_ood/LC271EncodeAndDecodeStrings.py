/*
* The string may contain any possible characters out of 256 valid ascii characters.
* Your algorithm should be generalized enough to work on any possible characters.
**/
# This question different from another one in this folder is that this one might have all 256 ascii chars, so cannot be shorten than before to keep informaiton complete.
class Codec:
    def encode(self, strs):
        return ''.join(string.replace('X', 'XY') + 'XX' for string in strs)

    def decode(self, s):
        return [x.replace('XY', 'X') for x in s.split('XX')[:-1]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

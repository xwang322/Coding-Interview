class Codec:

    def encode(self, strs):
        answer = []
        for string in strs:
            answer.append(string.replace('X','XY') + 'XX')
        return ''.join(answer)


    def decode(self, s):
        answer = []
        for each in s.split('XX')[:-1]:
            answer.append(each.replace('XY', 'X'))
        return answer

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

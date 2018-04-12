class Solution(object):
    def reverseVowels(self, s):
        vowels = ['a', 'e', 'i', 'o', 'u']
        length = len(s)
        p1 = 0
        p2 = length-1
        answer = list(s)
        while True:
            while p1 < p2 and s[p1].lower() not in vowels:
                p1 += 1
            while p1 < p2 and s[p2].lower() not in vowels:
                p2 -= 1
            if p1 >= p2:
                break
            if s[p1].lower() in vowels and s[p2].lower() in vowels:
                answer[p1], answer[p2] = answer[p2], answer[p1]
            p1 += 1
            p2 -= 1
        return ''.join(answer)
        
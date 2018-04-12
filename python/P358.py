class Solution(object):
    def rearrangeString(self, s, k):
        if not s:
            return ''
        count = collections.defaultdict(int)
        for char in s:
            count[char] += 1
        stack = sorted(list(count.items()), key=lambda t:t[1])
        char, num = stack.pop()
        lst = [[char] for i in range(num)]
        while stack and stack[-1][1] == num:
            char, tempcount = stack.pop()
            for l in lst:
                l.append(char)
        rest = ''.join(c*n for c,n in stack)
        for i, r in enumerate(rest):
            lst[i%(len(lst)-1)].append(r)
        for l in lst[:-1]:
            if len(l) < k:
                return ''
        return ''.join(''.join(l) for l in lst)
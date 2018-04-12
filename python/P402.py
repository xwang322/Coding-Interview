class Solution(object):
    def removeKdigits(self, num, k):
        out = []
        for each in num:
            while k and out and out[-1] > each:
                out.pop()
                k -= 1
            out.append(each)
        return ''.join(out[:-k or None]).lstrip('0') or '0' #[:-k] will reach number kth element
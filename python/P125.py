class Solution(object):
    def isPalindrome(self, s):
        if not s:
            return True
        start, end = 0, len(s)-1
        while start < end:
            char_start = s[start].lower()
            char_end = s[end].lower()
            if char_start.isalnum() and char_end.isalnum():
                if char_start != char_end:
                    return False
                else:
                    start += 1
                    end -= 1
            else:
                if not char_start.isalnum():
                    start += 1
                else:
                    end -= 1
        return True
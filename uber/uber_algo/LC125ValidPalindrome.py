class Solution(object):
    def isPalindrome(self, s):
        if not s:
            return True
        s = s.strip()
        left = 0
        right = len(s)-1
        while left <= right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() != s[right].lower():
                    return False
                else:
                    left += 1
                    right -= 1
            elif not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
        return True
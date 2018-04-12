class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        temp = 1
        while x/temp >= 10:
            temp *= 10
        while x:
            left = x/temp
            right = x%10
            if left != right:
                return False
            x = (x%temp)/10
            temp = temp/100
        return True
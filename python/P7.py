class Solution(object):
    def reverse(self, x):
        string = str(x)
        if string[0] == '-':
            new_string = ''.join(reversed(string[1:]))
            return -int(new_string) if -int(new_string)>-2**31-1 else 0 
        else:
            new_string = string[::-1]
            return int(new_string) if int(new_string)<2**31-1 else 0
        
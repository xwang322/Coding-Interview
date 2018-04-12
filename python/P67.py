class Solution(object):
    def addBinary(self, a, b):
        ''' using Python built-in function
        if not a:
            return b
        if not b:
            return a
        bina = int(a,2)
        binb = int(b,2)
        return str(bin(bina+binb))[2:]
        '''
        if not a:
            return b
        if not b:
            return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), '1') + '0'
        else:
            return self.addBinary(a[:-1], b[:-1]) + str(int(a[-1])+int(b[-1]))
            
                
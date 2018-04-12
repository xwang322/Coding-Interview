class Solution(object):
    def isHappy(self, n):
        if not n:
            return False
        dictionary = {1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64, 9:81, 0:0}
        record = set()
        temp = []
        while True:
            n_list = list(str(n))
            for char in n_list:
                temp.append(dictionary[int(char)])
            if sum(temp) == 1:
                return True
            else:
                n = sum(temp)
                temp = []
                if n not in record:
                    record.add(n)
                else:
                    return False
            
        
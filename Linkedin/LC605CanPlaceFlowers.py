class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        if not n:
            return True
        if len(flowerbed) <= 2:
            if any(flower == True for flower in flowerbed):
                return False
            else:
                return True if n < 2 else False
        for i in range(len(flowerbed)):
            if i == 0 and flowerbed[0] == False and flowerbed[1] == False:
                flowerbed[i] = True
                n -= 1
            elif i == len(flowerbed)-1:
                if flowerbed[i] == False and flowerbed[i-1] == False:
                    flowerbed[i-1] = True
                    n -= 1
            else:
                if flowerbed[i] == False and flowerbed[i-1] == False and flowerbed[i+1] == False:
                    n -= 1
                    flowerbed[i] = True
            if n == 0:
                return True
        return False

/*
* 今天刚面的一国人小哥, 人非常nice, 给我的题, 感觉见过, 也不一定见过, 但总体不是很难, 不过想了下, 不是很难,
* 就是给很多line, 找两条line, line是垂直于x轴的, 然后中间可以蓄水最多(是哪两条line),
* 需要debug, 需要自己想testing case, 需要通过编译拿到结果
* 拿到题目后, 想了一下, input case, output case, 要和面试官互动,
*不过国人小哥很nice, 都可以自定义, 然后返回本来是需要返回哪两条line,
*但是我想了下, 返回最大的value(存水), 会相对来说比较简单点, 否则还要维护一个int[2]的数组. 
**/

class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height)-1
        answer = 0
        while left < right:
            temp = min(height[left], height[right])
            answer = max(answer, temp*(right-left))
            if temp == height[left]:
                left += 1
            else:
                right -= 1
        return answer

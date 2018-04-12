/*
* 今天上午刚面的，上来简历聊了5分钟，题就一题 李扣的 第石题，字符匹配。做之前和烙印面试官讨论了一下，做的比较顺利，但是写完代码后
* 因为是dp所以烙印完全不懂，我每行都逐一解释了解释了10分钟最后他表示懂了，所有的test case都是过了，
* 他最后结束的时候说出来他想要的答案其实是recursion。刚收到hr邮件说烙印说技术没问题，但是交流很有问题，要求第二个电话面试重点看交流。这就是烙印啊，什么都挑不到刺的时候就拿交流做文章。第二轮如果还是印度人估计结果也一样，dp这种东西如果对方完全不懂电话里不容易解释的。感觉现在的面试因素非常多，真的是不容易啊
**/

class Solution(object):
    def isMatch(self, s, p):
        dp = [[False for i in range(len(s)+1)] for j in range(len(p)+1)]
        dp[0][0] = True
        for i in range(len(p)):
            if p[i] == '*':
                if i == 0:
                    dp[i][0] = True
                elif dp[i-1][0]:
                    dp[i+1][0] = True
        for i in range(len(p)):
            for j in range(len(s)):
                if p[i] == s[j]:
                    dp[i+1][j+1] = dp[i][j]
                elif p[i] == '.':
                    dp[i+1][j+1] = dp[i][j]
                elif p[i] == '*':
                    if p[i-1] != '.' and p[i-1] != s[j]:
                        dp[i+1][j+1] = dp[i-1][j+1]
                    else:
                        dp[i+1][j+1] = dp[i-1][j+1] or dp[i][j+1] or dp[i+1][j]
                        # dp[i+1][j] is for the case '.*' the '*' is for more of '.'
                        # dp[i][j+1] is for the case p[i-1] == s[j]
                        # dp[i+1][j] is for the case '.*' the '*' is for zero of '.'
        return dp[-1][-1]

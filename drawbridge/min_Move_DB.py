/*
* minMove
*
* 两个相同长度的正整数，每次操作可以对一个数的某一位digit加1或者减1，问最少操作次数使两数相等。
* 输入为两个数组a,m，输出两个数组对应位置上两个数的最小操作和。
* */
def minMove(self, a, b):
	count  = 0
	while a!= 0:
		a1 %= 10
		b1 %= 10
		count += abs(a1-b1)
		a /= 10
		b /= 10
	return count

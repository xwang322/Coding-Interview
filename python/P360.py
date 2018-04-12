class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        if a == 0:
            if b > 0:
                return [b*num+c for num in nums]
            elif b < 0:
                return [b*num+c for num in nums[::-1]]
            else:
                return [c for num in nums]
        if a > 0:
            middle = float(-b)/float(2*a)
            abs_dis = [abs(num-middle) for num in nums]
            mid = abs_dis.index(min(abs_dis))
            start = mid-1
            end = mid+1
            answer = []
            answer.append(self.calculate(a,b,c,nums[mid]))
            while start >= 0 and end <= len(nums)-1:
                if self.calculate(a,b,c,nums[start]) <= self.calculate(a,b,c,nums[end]):
                    answer.append(self.calculate(a,b,c,nums[start]))
                    start -= 1
                else:
                    answer.append(self.calculate(a,b,c,nums[end]))
                    end += 1
            if start < 0 and end <= len(nums)-1:
                while end <= len(nums)-1:
                    answer.append(self.calculate(a,b,c,nums[end]))
                    end += 1
            else:
                while start >= 0:
                    answer.append(self.calculate(a,b,c,nums[start]))
                    start -= 1
            return answer
        elif a < 0:
            middle = float(-b)/float(2*a)
            abs_dis = [abs(num-middle) for num in nums]
            mid = abs_dis.index(min(abs_dis))
            start = mid-1
            end = mid+1
            answer = []
            answer.append(self.calculate(a,b,c,nums[mid]))
            print answer
            while start >= 0 and end <= len(nums)-1:
                if self.calculate(a,b,c,nums[start]) >= self.calculate(a,b,c,nums[end]):
                    answer.append(self.calculate(a,b,c,nums[start]))
                    start -= 1
                else:
                    answer.append(self.calculate(a,b,c,nums[end]))
                    end += 1
                print start, end
            if start < 0 and end <= len(nums)-1:
                while end <= len(nums)-1:
                    answer.append(self.calculate(a,b,c,nums[end]))
                    end += 1
            else:
                while start >= 0:
                    answer.append(self.calculate(a,b,c,nums[start]))
                    start -= 1
            return answer[::-1]
            
            
            
    def calculate(self, a, b, c, num):
        return a*num*num+b*num+c
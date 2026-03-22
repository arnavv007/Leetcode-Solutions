class Solution(object):
    def arraySign(self, nums):
        if 0 in nums:
            return 0
        else:
            num = 1
            for i in nums:
                num *= i
            return -1 if num < 0 else 1
print(Solution.arraySign(Solution, [1,2,3,-1,6,7,2,0]))
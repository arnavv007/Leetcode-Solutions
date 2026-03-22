class Solution(object):
    def moveZeroes(self, nums):
        zero = 0
        j = 0
        while j<len(nums):
            if(nums[j] == 0):
                nums.pop(j)
                zero+=1
            else:
                j+=1
        for i in range(zero):
            nums.append(0)
        return nums
print(Solution.moveZeroes(Solution, [0,0,1]))
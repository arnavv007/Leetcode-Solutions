class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        l = len(nums)
        result = [0] * l
        for j in range(l):
            for i in range(j ,l-1):
              print(i)
              if(nums[j] > nums[i+1]):
                  result[j] += 1
              elif(nums[j] < nums[i+1]):
                  result[i+1] += 1
        return result

print(Solution.smallerNumbersThanCurrent(Solution, [6,5,4,8]))
            
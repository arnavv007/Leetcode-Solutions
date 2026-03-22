class Solution(object):
    def isMonotonic(self, nums):
        prev = nums[0]
        
        if(prev < nums[len(nums) - 1]):
            for i in nums:
                if(i < prev):
                    return False
                prev = i
        elif(prev > nums[len(nums) - 1]):
            for i in nums:
                if(i> prev):
                    return False
                prev = i
        else:
            for i in nums:
                if(i != prev):
                    return False
        return True

print(Solution.isMonotonic(Solution, [1,2,3,3]))
        
    

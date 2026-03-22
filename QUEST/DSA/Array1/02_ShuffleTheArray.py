class Solution(object):
    def shuffle(self, nums, n):
        arr = []
        i=0
        j = (2*n)-1
        while(i<n):
            arr.append(nums[i])
            arr.append(nums[j])
            i+=1
            j-=1
        return arr

print(Solution.shuffle(Solution, [1,2,3,4,5,6], 3))
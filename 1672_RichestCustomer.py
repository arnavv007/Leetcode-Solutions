class Solution(object):
    def maximumWealth(self, accounts):
        maximum = 0
        for i in accounts:
            wealth = sum(i)
            if wealth > maximum:
                maximum = wealth
                
        return maximum
print(Solution.maximumWealth(Solution, [[1,2,3],[3,2,1]]))

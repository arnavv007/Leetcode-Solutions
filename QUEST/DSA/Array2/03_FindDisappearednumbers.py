class Solution(object):
    def findDisappearedNumbers(self, nums):
        l = []
        missing = []
        s1 = list(set(nums))
        for i in range(1, len(nums)+1):
            l.append(i)
        i = 0 
        j = 0
        while(i < len(s1)):
            if(s1[i] != l[j]):
                missing.append(l[j])
                i -= 1
            i += 1
            j+=1
        if(j < len(l)):
            while(j<len(l)):
                missing.append(l[j])
                j+=1
        return missing
    

print(Solution.findDisappearedNumbers(Solution, [1,1,2,2]))

class Solution(object):
    def findErrorNums(self, nums):
        correct = 0
        s = sum(set(nums))
        duplicate = abs(s-sum(nums))
        l = sorted(set(nums))
        if(l[0]!=1):
            return duplicate, 1
        for i in range(len(l)):
            if(l[i] != i+1):
                correct = i+1
                print(correct)
                break
        if(correct == 0):
            correct = len(l) +1
        print(l)
        return duplicate, correct
        

print(Solution.findErrorNums(Solution, [8,7,3,5,3,6,1,4]))
class Solution(object):
    def findTheDifference(self, s, t):
        copy_s = list(s)
        copy_t = list(t)
        j = 0
        for i in copy_t:
            if(i not in copy_s):
                return i
            else:
                copy_s.pop(copy_s.index(i))
                


print(Solution.findTheDifference(Solution, "abcd", "abcde"))

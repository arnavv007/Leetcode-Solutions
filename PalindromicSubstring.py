class Solution(object):
    def longestPalindrome(self, s):
        list = []
        for i in s:
            list.append(i)
        list2 = list.reverse()
        return list2

print(Solution.longestPalindrome(Solution, "babad"))

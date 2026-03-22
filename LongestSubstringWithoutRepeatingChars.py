class Solution(object):
    def lengthOfLongestSubstring(self, s):
        dummy_string = ""
        dummy_count = 0
        longest_string = ""
        count = 0
        for i in s:
            if i in longest_string and count > dummy_count:
                dummy_string = longest_string
                longest_string = ""
                dummy_count = count
                count = 0
            if i not in longest_string:
                longest_string += i
                count += 1
        print(dummy_count)

Solution.lengthOfLongestSubstring(Solution, "abcabcbb")
        

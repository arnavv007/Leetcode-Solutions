class Solution(object):
    def repeatedSubstringPattern(self, s):
        j = 1
        new_string = ""
        while j <= len(s) / 2:
            r = int(len(s) / j)
            substring = s[0:j]
            new_string += substring*r
            if(new_string == s):
                return True
            else:
                new_string = ""
            j+=1
        return False

print(Solution.repeatedSubstringPattern(Solution, "abcabcabcabc"))
class Solution(object):
    def lengthOfLastWord(self, s):
        s = list(s)
        length = 0
        End = len(s)-1
        
        while(True):
            if(s[End] == " "):
                End -= 1
            else:
                while(End >-1 and s[End] != " "):
                    length += 1
                    End -= 1
                break
        return length
print(Solution.lengthOfLastWord(Solution, "a"))
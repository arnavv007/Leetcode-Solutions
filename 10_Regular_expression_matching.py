class Solution(object):
    def isMatch(self, s, p):
        prev_char = "" 
        dummy_str = ""
        j = 0
        p1 = list(p)
        for i in s:
            if(p1[j] == i):
                dummy_str += i
                prev_char = i
                j += 1
            elif(p1[j] == "."):
                dummy_str += i
                j += 1
            elif(p1[j] == "*" and (prev_char == i or prev_char == ".")):
                dummy_str += i
            else:
                j+=1
        return dummy_str, p1

print(Solution.isMatch(Solution, "sssiss", "s*is*"))
                 


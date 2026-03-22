class Solution(object):
    def toLowerCase(self, s):
        for i in s:
            if(ord(i) >= 65 and ord(i) <= 90):
                print("y")
                string = s.replace(i, "1")
        return string
print(Solution.toLowerCase(Solution, "HE"))
class Solution(object):
    def isPalindrome(self, x):
        My_list = list(str(x))
        i = 0
        j = len(My_list) - 1
        while(i<j):
            if(My_list[i] == My_list[j]):
                i+=1
                j-=1
            else:
                return False
        return True

print(Solution.isPalindrome(Solution, 1000021))        


class Solution(object):
    def isPowerOfTwo(self, n):
        if(n==1 or n==2):
            return True
        elif(n%2 != 0):
            return False
        while(n>2):
            n = n/2
        return True if n==2 else False
        
    

print(Solution.isPowerOfTwo(Solution, 1056))
            

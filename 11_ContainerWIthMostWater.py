class Solution(object):
    def maxArea(self, height):
        j = a = len(height) - 1
        i = area = 0
        while i<len(height) and j>-1:
            if(height[i] * a < height[i+1] * a):

                i+=1
                a-=1
            elif(height[j] * a < height[j-1]):
                j-=1
                a-=1
            
        area = min(height[i], height[j]) * a
        return area


print(Solution.maxArea(Solution, [3, 6 ,1]))
            


                
               
        
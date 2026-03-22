class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        if(len(arr)==2):
            return True
        arr.sort()
        i = 0
        j = 1
        while j < len(arr)-1:
            if((arr[j] - arr[i]) != (arr[j+1] - arr[i+1])):
                return False
            i+=1
            j+=1
        return True
    
print(Solution.canMakeArithmeticProgression(Solution, [13,12,-12,9,9,16,7,-10,-20,0,18,-1,-20,-10,-8,15,15,16,2,15]))

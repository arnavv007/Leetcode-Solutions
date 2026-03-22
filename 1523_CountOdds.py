class Solution(object):
    def countOdds(self, low, high):
        number = int((high-low)/2)
        if low%2 != 0:
            number+=1
        if high%2 != 0:
            number+=1
        return number

print(Solution.countOdds(Solution, 8 , 10))
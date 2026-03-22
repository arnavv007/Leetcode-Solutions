class Solution(object):
    def romanToInt(self, s):
        Integer_Sum = 0
        Roman_Values = {'I' : 1,
                        'V' : 5,
                         'X' : 10,
                         'L' : 50,
                         'C' : 100,
                         'D' : 500,
                         'M' : 1000}
        prev = 1001
        for i in s:
            element = Roman_Values.get(i)
            
            if(element>prev):
                Integer_Sum -= 2*prev 
                Integer_Sum += element
            else:
                Integer_Sum += element

            prev = element
        return Integer_Sum

print(Solution.romanToInt(Solution, "MCMXCIV"))

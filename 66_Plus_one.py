class Solution(object):
    def plusOne(self, digits):
        string = "" 
        for i in digits:
            string += str(i)
        number = str(int(string) + 1)
        array = []
        for i in number:
            array.append(int(i))


print(Solution.plusOne(Solution, [9,9,9]))
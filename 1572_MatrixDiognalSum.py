class Solution(object):
    def diagonalSum(self, mat):
        length = len(mat)
        Sum = 0
        r, c = 0, 0
        R, C = length - 1,-(length)
        
        for i in range(length):
            Sum += mat[r][c]
            r, c = r+1, c+1
            Sum += mat[R][C]
            R, C = R-1, C+1
        centre = int((length-1)/2)
        return Sum if length % 2 == 0 else Sum - mat[centre][centre]



print(Solution.diagonalSum(Solution, [[7,9,8,6,3],
                                      [3,9,4,5,2],
                                      [8,1,10,4,10],
                                      [9,5,10,9,6],
                                      [7,2,4,10,8]]))
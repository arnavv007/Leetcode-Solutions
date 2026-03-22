class Solution(object):
    def setZeroes(self, matrix):
        len_c, len_r = len(matrix[0]), len(matrix)
        r, c = 0, 0
        zeroes = []
        for i in matrix:
            for j in i:
                if(j==0):
                    L = [r,c]
                    zeroes.append(L)
                r+=1
            c+=1
            r=0
        for c in zeroes:
            for i in range(len_r):
                matrix[i][c[0]] = 0
            for j in range(len_c):
                matrix[c[1]][j] = 0
        print(len_c, len_r)
        print(zeroes)
        return matrix
            
print(Solution.setZeroes(Solution, [[0,1,2,2],
                                    [3,4,1,2],
                                    [1,3,1,5]]
                                    ))
                


class Solution(object):
    def spiralOrder(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        arr = []
        r, c = 0,0
        decrement = 0
        a, b = 0,-1
        sign = 1
   
        for i in range(m-1):
            if(sign == -1):
                decrement+=1
                a, b = a-1, b-1
                r, c = a, b
            for i in range(n-decrement):
               print(arr)
               arr.append(matrix[r][c])
               c += sign
            r+=sign
            c-=sign
           
            for i in range(m-decrement):
               print(arr)
               arr.append(matrix[r][c])
               r += sign
            sign *= -1
        return arr

print(Solution.spiralOrder(Solution, [[7,3,1,9],
                                      [2,4,6,9],
                                      [6,9,6,6],
                                      [9,5,8,5]]))
            
            
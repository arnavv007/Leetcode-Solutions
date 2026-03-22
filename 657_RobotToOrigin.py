class Solution(object):
    def judgeCircle(self, moves):
        # coordinate = [0,0]
        
        # for i in moves:
        #     if(i=="U"):
        #         coordinate[1] += 1
        #     elif(i=="D"):
        #         coordinate[1]-=1
        #     elif(i=="R"):
        #         coordinate[0] += 1
        #     else:
        #         coordinate[0] -= 1
        # print(coordinate)
        # return True if coordinate == [0,0] else False
    
        # or

        return True if moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R") else False

print(Solution.judgeCircle(Solution, "UD"))
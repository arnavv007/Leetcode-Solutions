class Solution(object):
    def isRobotBounded(self, instructions):
        dirX, dirY = 0, 1
        x, y = 0, 0
        for i in instructions:
            if i == "G":
                x, y = x + dirX, y + dirY
            elif i == "L":
                dirX, dirY = -1*dirY, dirX
            
            else:
                dirX, dirY = dirY, dirX*-1
        return (x,y) == (0,0) or (dirX, dirY) != (0, 1)


print(Solution.isRobotBounded(Solution, "GR"))
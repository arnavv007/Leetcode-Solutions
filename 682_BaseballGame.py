class Solution(object):
    def calPoints(self, operations):
        L = []
        prev = -1
        for i in operations:
          
            if(i == "C"):
                L.pop()
                prev-=1
              
            elif(i== "D"):
                L.append(int(L[prev])*2)
                prev+=1
               
            elif(i == "+"):
                print(prev)
                L.append(int(L[prev]) + int(L[prev-1]))
                prev+=1
              
            else:
                L.append(int(i))
                prev+=1
            print(L, prev)
                
        return sum(L)
            


print(Solution.calPoints(Solution, ["1","C"]))
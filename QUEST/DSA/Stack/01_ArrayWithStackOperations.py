class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
       l = []
       j = 0
       i = 1
       length = len(target)
       if not target:
           return []
       while(i<n+1):
            l.append("push")
            if(target[j] != i):
               l.append("pop")
            else:
               j+=1
               if(j == length):
                   break
            i+=1

       return l

print(Solution.buildArray(Solution, [], 5))  

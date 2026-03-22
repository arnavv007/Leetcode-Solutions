class Solution(object):
    def strStr(self, haystack, needle):
   
        index = 0
        if needle in haystack:
            a = list(needle)
            b = list(haystack)
            for i in b:
                if(i==a[0]):
                    k = index
                    for i in a:
                        if(i==b[k]):
                            if(b[k] == a[len(a) - 1]):
                                return index
                            k+=1
                            
                        else:
                            break

                index+=1
        else:
            return -1
      
                        
print(Solution.strStr(Solution, "Leetcode", "codee"))
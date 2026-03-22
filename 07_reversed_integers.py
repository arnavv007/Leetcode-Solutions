class Solution(object):
    def reverse(self, x):
        My_list = list(str(x))
        new_list = ''
        i = len(My_list) - 1
        negative = False
        if(My_list[0] == '-'):
            My_list.pop(0)
            i-=1
            negative = True

        while(i!=-1):
            new_list += My_list[i]
            i-=1
        
        result = int(new_list)
        if(result<-2**31 or result > 2**31):
            return 0
        if(negative==True):
            result-=result*2
        return result
        

print(Solution.reverse(Solution, -123))

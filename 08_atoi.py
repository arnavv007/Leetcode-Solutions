class Solution(object):
    def myAtoi(self, s):
        valid_numbers = ["0","1","2","3","4","5","6","7","8","9", "-","+"]
        new_string = ''
        negative = False
        decimal = False
        for i in s:
            if i not in valid_numbers and i!= " ":
                break
            elif i!= " ":
                if new_string != "" and (i=="-" or i=="+"):
                    break
                new_string += i
            elif i==" " and new_string != "":
                break
            
        
        if new_string == "" or new_string == "+" or new_string == "-":
            return 0
        if(int(new_string) < -2**31):
            new_string = "-2147483648"
        elif(int(new_string) > 2**31 -1):
            new_string = "2147483647"
       
        
        return int(new_string)

          
    
            

print(Solution.myAtoi(Solution, "+-2"))


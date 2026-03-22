def solution(l1, l2):
    length = len(l1) - 1
    carry = False
    list = []
    while(length > -1):
        sum = l1[length] + l2[length]
        if(carry):
            list.append(sum + 1)
            
        if(sum > 9):
           list.append(sum - 10)
           carry = True
        elif(not carry and sum<10):
            list.append(sum)
        

        length-=1
    
    
    j = len(list) - 1
    while(j > -1):
        print(list[j])
        j-=1


    


l1 = [2, 4, 3]
l2 = [5, 6, 4]
solution(l1, l2)
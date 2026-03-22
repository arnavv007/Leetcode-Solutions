class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        change = []
        for i in bills:
            if i == 5:
                change.append(5)
            elif i == 10:
                if 5 in change:
                    change.remove(5)
                    change.append(10)
                else:
                    return False
            else:
                if (5 in change and 10 in change):
                    change.remove(5)
                    change.remove(10)
                elif change.count(5) >= 3:
                    change.remove(5)
                    change.remove(5)
                    change.remove(5)
                else:
                    return False
        return True
    
print(Solution.lemonadeChange(Solution, [5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]))
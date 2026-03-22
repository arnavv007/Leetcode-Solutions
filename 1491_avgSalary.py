class Solution(object):
    def average(self, salary):
        maximum_salary = 0
        minimum_salary = 10000000000
        Total_salary = 0
        for i in salary:
            if i < minimum_salary:
                minimum_salary = i
            if i > maximum_salary:
                maximum_salary = i
            Total_salary += i
        Total_salary -= (maximum_salary + minimum_salary)
        average_salary = Total_salary/(len(salary) - 2)
        return average_salary

print(Solution.average(Solution, [48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000]))
        


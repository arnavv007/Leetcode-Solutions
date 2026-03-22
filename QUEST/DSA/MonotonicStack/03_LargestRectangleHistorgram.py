class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
#         def FindSmallest(start, end):
#             small = 999999999
#             for i in range(start,end+1):
#                 if(heights[i]<small):
#                     small = heights[i]
#             return small
        
#         LENGTH = len(heights)
#         k = 0
#         Largest = heights[0]
#         Large = 0

#         for i in range(LENGTH):
#             if(heights[i] > Largest):
#                 Largest = heights[i]
#             print(Largest)
        
#         print("\n")
#         for i in range(1,LENGTH):
#             start = k
#             end = i
#             for j in range(LENGTH-i):
#                 print(f"Start:{start}\nEnd:{end}")
#                 smallest = FindSmallest(start,end)
#                 print(f"Smallest:{smallest}\ni:{i}")
#                 Area = smallest * (i+1)
#                 print(f"Area:{Area}")
#                 if(Area>Largest):
#                     Largest = Area
#                 start+=1
#                 end+=1
#                 print(Largest)
        
#         return Largest
           
  
        stack = []  # stores indices
        max_area = 0
        heights.append(0)  # sentinel to flush stack

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
                print(max_area)
            
            stack.append(i)

        return max_area

print(Solution.largestRectangleArea(Solution, [1,2,3,4,5]))
            
def sort(array,  length):
        i = 0
        while(i < length - 1):
            swaps = 0
            for j in range(length - i - 1):
                if(array[j] < array[j + 1]):
                    temp = array[j]
                    array[j] = array[j + 1]
                    array[j+1] = temp
                    swaps+=1
        
            if(swaps == 0):
                break
            i+=1
    
        return array
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        Median_list = []
        j = 0
        for i in nums1:
            Median_list.append(i)
            j+= 1
        
        for k in nums2:
            Median_list.append(k)
            j+= 1
        sort(Median_list, j)
        if(j%2):
            index = int(j/2)
            return Median_list[index]
        
        else:
            index1 = int(j/2-1)
            index2 = int(j/2)
            median = (Median_list[index1] + Median_list[index2]) / 2
            return median

nums1 = [1,2]
nums2 = [3,4]
print(Solution.findMedianSortedArrays(Solution, nums1, nums2))


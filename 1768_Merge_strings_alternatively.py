class Solution(object):
    def mergeAlternately(self, word1, word2):
        new_string = ""
        string1 = list(word1)
        string2 = list(word2)
        i = 0
        
        maximum = max(len(word1), len(word2))
        if(len(word1)>len(word2)):
            longest_word = word1
        elif(len(word1) < len(word2)):
            longest_word = word2
        while i<min(len(word1), len(word2)):
            new_string+=string1[i]
            new_string+=string2[i]
            i+=1
        while i < maximum:
            new_string += longest_word[i]
            i+=1
        return new_string
print(Solution.mergeAlternately(Solution, "abc", "pqrsiut"))
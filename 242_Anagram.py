class Solution(object):
    def isAnagram(self, s, t):
        letters = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i not in letters:
                letters[i] = 1
            else:
                letters[i] += 1
        
        for j in t:
            if j in letters and letters.get(j) != 0:
                letters[j] -= 1
            else:
                return False

        return letters, True

print(Solution.isAnagram(Solution, "ab", "a"))
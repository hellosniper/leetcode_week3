# Edit Distance.py
# D[i,j]: Edit Distance between word1[0:i] and word2[0:j]

# Question:  #Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)
#             You have the following 3 operations permitted on a word:
#              a) Insert a character
#              b) Delete a character
#              c) Replace a character
# Question from: https://oj.leetcode.com/problems/edit-distance/
# Sulotion: 
# Author: DongDing 
# Date: 2014/07/21
# Time complexity:  O(mn)
# space complexity:  O(mn)  
# Tag: # Dynamic programming  
# Comment: 


class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        # initialize the tabulation
        D = [[0 for j in range(len(word2)+1)] for i in range(len(word1)+1)]
        D[0] = [j for j in range(len(word2)+1)]
        for i in range(len(word1)+1):
            D[i][0] = i
        # edit the tabulation
        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                D1 = D[i-1][j] +1
                D2 = D[i][j-1] +1
                if word1[i-1] == word2[j-1]:
                    D3 = D[i-1][j-1] # D(i-1,j-1) + distance
                else:
                    D3 = D[i-1][j-1] + 1
                
                D[i][j] = min([D1,D2,D3])
        return D[len(word1)][len(word2)]
word1 = 'ab'
word2 = 'bc'
a = Solution()
print a.minDistance(word1, word2)

# Jump Game.py
# Question:  # Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.
# For example:
# A = [2,3,1,1,4], return true.
# A = [3,2,1,0,4], return false.
#           
# Question from: https://oj.leetcode.com/problems/jump-game/
# Sulotion:  interatively visit every position keep track of the furthest positon that be reached by the postition before this

# Author: DongDing 
# Date: 2014/07/06
# Time complexity:  O(n)
# space complexity:  O(1)  
# Tag: # array # Dynamic programming  
# Comment: 
#




class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        jump = 0
        for i in range(len(A)):
            if jump< A[i]:
                jump = A[i]
            if i == len(A)-1:
                return True
            if jump == 0:
                return False
            jump -= 1
        return True

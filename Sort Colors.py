# Sort Colors.py 
# Question:  #Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
# Note: You are not suppose to use the library's sort function for this problem.
# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
# Could you come up with an one-pass algorithm using only constant space?
#           
# Question from: https://oj.leetcode.com/problems/sort-colors/
# Sulotion:  interatively visit every position keep track of the furthest positon that be reached by the postition before this

# Author: DongDing 
# Date: 2014/07/15
# Time complexity:  O(n)
# space complexity:  O(1)  
# Tag: # array # Dynamic programming  
# Comment: 


class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        if not A:
            return    
        i = 0   # current index
        z = 0   # last 0 
        t = len(A) - 1     #first 2       
        while i <= t:
            curr = A[i]
            A[i] = 1
            if curr == 0:
                
                A[z] = 0
                z+=1
                #continue
            elif curr == 1:
                pass
            elif curr == 2:
                if t == i:
                    A[i] = 2
                #swap
                tmp = A[t]
                A[t] = curr
                A[i] = tmp
                t-=1
                continue
            i += 1
            
A = [2]
a = Solution()
a.sortColors(A)
print A
    #straight forward solution
    #def sortColors(self, A):
        #if not A:
            #return
        #zero = 0
        #one = 0
        #two = 0
        #for i in range(len(A)):
            #if A[i] == 0:
                #zero+=1
            #elif A[i] == 1:
                #one+=1
            #elif A[i] == 2:
                #two +=1
        #for i in range(zero):
            #A[i] = 0
        #for i in range(one):
            #A[i+zero] = 1
        #for i in range(two):
            #A[i+zero+one] = 2           


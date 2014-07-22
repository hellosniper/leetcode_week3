# Gray Code.py

# Question:  #The gray code is a binary numeral system where two successive values differ in only one bit.
# Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. 
# A gray code sequence must begin with 0.
# For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
#00 - 0
#01 - 1
#11 - 3
#10 - 2
# Question from: https://oj.leetcode.com/problems/gray-code/
# Sulotion:
# Author: DongDing 
# Date: 2014/07/22
# Time complexity:  O(n)
# space complexity:  O(n)  
# Tag: # recursive # list  
# Comment: 



class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]
        firstpart = self.grayCode(n-1)
        temp = []
        temp.extend(firstpart)
        secondepart = self.reverse_plus(temp,n-1)
        firstpart.extend(secondepart)
        return firstpart
    def reverse_plus(self,list1,n):
        list2 = []
        base = 1<<n
        for i in range(len(list1)):
            list2.append(list1.pop() + base)
        return list2
    
a = Solution()
print a.grayCode(10)


##class Solution:
### @return a list of integers
##def grayCode(self, n):
    ##num = 2**n
    ##return map(lambda x:(x>>1)^x,[x for x in range(num)])

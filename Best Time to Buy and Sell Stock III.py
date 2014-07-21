# Best Time to Buy and Sell Stock III.py 
# Question:  #Say you have an array for which the ith element is the price of a given stock on day i.
#             Design an algorithm to find the maximum profit. You may complete at most two transactions.
#             Note:
#                You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# Question from: https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
# Sulotion: find the min_price and maximum profit for one transaction,  then find the next transaction(1.before the first one, 2. within, 3. after)
# Author: DongDing 
# Date: 2014/07/20
# Time complexity:  O(n)
# space complexity:  O(1)  
# Tag: # array  
# Comment: 


class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        # max profit for one transaction,
        min_price = 9223372036854775807 #sys.maxint
        profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
                temp = i
            if profit < prices[i]-min_price:
                profit = prices[i]-min_price
                max_index = i
                min_index = temp
        # max profit before the transaction,        
        profit1 = 0
        min_price1 = 9223372036854775807 #sys.maxint
        for i in range(min_index):
            if prices[i] < min_price1:
                min_price1 = prices[i]              
            if profit1 < prices[i]-min_price1:
                profit1 = prices[i]-min_price1
        # max profit after the transaction,       
        min_price1 = 9223372036854775807 #sys.maxint    
        for i in range(max_index+1, len(prices)):
            if prices[i] < min_price1:
                min_price1 = prices[i]               
            if profit1 < prices[i]-min_price1:
                profit1 = prices[i]-min_price1
                                
        # max profit within the transaction,   
        min_price1 = 9223372036854775807 #sys.maxint 
        for i in range(max_index,min_index-1,-1):
            if prices[i] < min_price1:
                min_price1 = prices[i]                
            if profit1 < prices[i]-min_price1:
                profit1 = prices[i]-min_price1            
             
        return profit + profit1

prices = [2,4,1]   
a = Solution()
print a.maxProfit(prices)

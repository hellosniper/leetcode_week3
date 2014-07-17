# Best Time to Buy and Sell Stock II.py 
# Question:  #Say you have an array for which the ith element is the price of a given stock on day i.
#             Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times).
#             However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# Question from: https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Sulotion: for each day find the local min to buy, local max to sell
# Author: DongDing 
# Date: 2014/07/17
# Time complexity:  O(n)
# space complexity:  O(1)  
# Tag: # greedy algorithm # array  
# Comment: 

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        result = 0
        bought = False
        buy_price = 0
        
        for i in range(1,len(prices),1):
            if prices[i-1] < prices[i]:
                if bought == False:
                    buy_price = prices[i-1]
                    bought = True
                else:
                    pass
            elif prices[i-1] > prices[i]:
                if bought == False:
                    #buy_price = prices[i-1]
                    pass
                else:
                    result+= prices[i-1]- buy_price
                    bought = False
            if i == len(prices)-1:#last one
                if bought == True:
                    result+= prices[i]- buy_price
                    bought = False
        return result

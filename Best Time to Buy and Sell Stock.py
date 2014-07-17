# Best Time to Buy and Sell Stock.py 
# Question:  #Say you have an array for which the ith element is the price of a given stock on day i.
#             If you were only permitted to complete at most one transaction 
#             (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit
# Question from: https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Sulotion: for each day find the min_price and maximum profit
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
        min_price = 9223372036854775807 #sys.maxint
        profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            if profit < prices[i]-min_price:
                profit = prices[i]-min_price
        return profit

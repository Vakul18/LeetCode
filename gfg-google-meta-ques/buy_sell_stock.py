"""
Stock Buy and Sell – Multiple Transaction Allowed

The cost of stock on each day is given in an array price[]. Each day you may decide to either buy or sell the stock i at price[i], you can even buy and sell the stock on the same day. Find the maximum profit that you can get.

Note: A stock can only be sold if it has been bought previously and multiple stocks cannot be held on any given day.
"""
from typing import List


class Solution:
  def maximumProfit(self, prices) -> int:
    max_prof = 0
    for i in range(1, len(prices)):
      prof = prices[i] - prices[i-1]
 
      if prof > 0:
        max_prof += prof

    return max_prof
      
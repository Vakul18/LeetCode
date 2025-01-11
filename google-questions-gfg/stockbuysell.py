"""
Given an array are denoting the cost of stock on each day, the task is to find the maximum total profit if we can buy and sell the stocks any number of times.

Note: We can only sell a stock which we have bought earlier and we cannot hold multiple stocks on any day.

arr = [1,2,3] -> 2

arr = [0, 290, 1, 300] -> 290 + 299

arr = [1000, 10, 1, 290, 1000, 1, 300]

0 : buy, 1 : sell
dp[0][1] = float('-inf'), dp[0][0] = -1000

max_profit

dp[i][0] = dp[i-1][1] - arr[i]
dp[i][1] = dp[i-1][0] + arr[i]



[1000, 10, 1, 290, 1000, 1, 300]

      0
     / \
   0     -1000
  /  \       /\
 0   -10  -990   -1000
/ \   / \
0 -1 -10 -9

buysell(arr, i, state, val)
 if state == 0:
  value = max(buysell(arr, i+1, 1, val - arr[i]), buysell(arr, i+1, 1, val))
 else
  value = max(buysell(arr, i+1, 1, val + arr[i]), buysell(arr, i+1, 1, val))
 return val

[1000, 10, 1, 300, 299, 1000, 1, 300]

[1000, 10, 1, 300, 299, 1000]

1,1000 -> 999
1,300 - 299,1000 -> 299+701 = 1000

100 180 260 310 40 535 695
210 + 655

"""


class Solution:
    def stockBuySell(self, arr):
        left = 0
        right = 0
        profit = 0
        idx = 1

        while(idx < len(arr)):
            if arr[idx] <= arr[right]:
                profit += arr[right]-arr[left]
                left = idx
                right = idx
            else:
                right += 1					
            idx += 1
        profit += arr[right]-arr[left]        
        return profit







 
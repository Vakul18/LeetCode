"""
Given an array arr[] such that each element is in the range [0, 9] find the minimum possible sum of two numbers formed using the elements of the array. All digits in the given array must be used to form the two numbers. Return a string without leading zeroes.


Input: arr[] = [6, 8, 4, 5, 2, 3]
Output: "604"
Explanation: The minimum sum is formed by numbers 358 and 246. 346 258
Input: arr[] = [5, 3, 0, 7, 4]
Output: "82"
Explanation: The minimum sum is formed by numbers 35 and 047. 057 34 - 37 45 - 0 3
Input: arr[] = [9, 4]
Output: "13"
Explanation: The minimum sum is formed by numbers 9 and 4.


arr = [0, 1, 2, 3, 4, 5]

0247 1358

0358 1247


0 3 4 5 7

047 35

05 34



"""
sys.set_int_max_str_digits(10000)
class Solution:
  def minSum(self, arr):
    arr_s = sorted(arr)
    num1 = 0
    num2 = 0
    for i,num in enumerate(arr_s):
      if i%2 == 0:
        num1 = num1*10 + num
      else:
        num2 = num2*10 + num

    return num1 + num2

---------


class Solution:

    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0

            total = n1 + n2 + carry
            carry = total // 10
            result.append(str(total % 10))

            i -= 1
            j -= 1

        # Join and strip leading zeros from the result
        return ''.join(result[::-1]).lstrip('0') or '0'

    def minSum(self, arr):
        n = len(arr)
        arr.sort()

        ans1 = ans2 = ''

        for i in range(0, n - 1, 2):
            ans1 += str(arr[i])
            ans2 += str(arr[i + 1])

        if n % 2:
            ans1 += str(arr[-1])

        # Use the custom addStrings function to return the sum as a string
        return self.addStrings(ans1, ans2)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.minSum(arr)
        print(ans)
        tc -= 1

        print("~")

# } Driver Code Ends

	

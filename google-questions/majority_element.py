"""
Given an array arr. Find the majority element in the array. If no majority exists, return -1.

A majority element in an array is an element that appears strictly more than arr.size()/2 times in the array.
 
[1,1,2] -> 1
n = 3


[2,2,2,4,4,4,4] -> 4
n = 7
n/2 = 3

[2,4,2,2,4]
n = 5
[1,0] -> -1


[2, 1, 1]
n=3

[2,1,1,1]

[4,4,2,6,4]

[2,4,2,4,4] -> 4
n = 5

[4,2,2,6,4] -> -1

[2,4,4,2,4,4,2]
n = 7


"""
class Solution:
    def majorityElement(self, arr):
        n = len(arr)
        if n == 0:
            return -1

        element = arr[0]
        count = 1
        for idx in range(1,n):
            if count == 0:
                element = arr[idx]
                count = 1
            else:
                if arr[idx] == element:
                    count += 1
                else:
                    count -=1
        
        lastElementCount = 0
        for currElement in arr:
            if element == currElement:
                lastElementCount += 1
        
        if lastElementCount > n/2:
            return element
        else:
            return -1
        













       
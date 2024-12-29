"""
Minimum Platforms

You are given the arrival times arr[] and departure times dep[] of all trains that arrive at a railway station on the same day. Your task is to determine the minimum number of platforms required at the station to ensure that no train is kept waiting.

At any given time, the same platform cannot be used for both the arrival of one train and the departure of another. Therefore, when two trains arrive at the same time, or when one arrives before another departs, additional platforms are required to accommodate both trains.

arr[] = [900, 840, 20, 50], dep[] = [1120, 999, 40, 60]
arr[] = [20, 50, 840, 900], dep[] = [40, 60, 999, 1120]


platformNo = 1

min  = 900
max = 1120
idx =

        root
        //\
50-60   20-40  900-1120
         /\
     840-999

i = 1, j = 0
50 > 40
 i = 2
 count = 2


"""

class Solution:    

    def minimumPlatform(self,arr,dep):
        arr.sort()
        dep.sort()
        
        i = 1
        j = 0
        
        no_of_platforms = 1
        count = 1
        while i < len(arr) and j < len(dep):
            if arr[i] <= dep[j]:
                count += 1
                i += 1
                no_of_platforms = max(no_of_platforms, count)
            else :
                j += 1
                count -= 1

        return no_of_platforms
            
"""
You are given an array arr[] of integers, where each element arr[i] represents the number of pages in the ith book. You also have an integer k representing the number of students. The task is to allocate books to each student such that:

Each student receives atleast one book.
Each student is assigned a contiguous sequence of books.
No book is assigned to more than one student.
The objective is to minimize the maximum number of pages assigned to any student. In other words, out of all possible allocations, find the arrangement where the student who receives the most pages still has the smallest possible maximum.

Note: Return -1 if a valid assignment is not possible, and allotment should be in contiguous order (see the explanation for better understanding).


[23,1,45], 2 -> [23,1] [45] -> 45
[23,100, 15],2 -> [23] [100,15] -> 115
[100, 23, 15],2 -> [100] [23, 15] -> 100
[100, 23, 15], 3 -> [100] [23] [15] -> 100
[100, 23, 15, 2000], 3 -> 2000


[100, 23, 15, 2000], 3
[[100 , 23], 15, 2000] [100 , [23, 15], 2000] [100 , 23, [15, 2000]]

[100, 23, 15, 2000, 4000], 3
[[100 , 23, 15], 2000, 4000] [100 , [23, 15, 2000], 4000] [100 , 23, [15, 2000, 4000]]
[[100 , 23], [15, 2000], 4000] [100 , [23, 15], [2000, 4000]] 

dp[i][j][k]
i : arr indx covered
j : jth bin entries

i 0 to k : students
 j 0 to n books
  
   
"""
class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        n = len(arr)
        if k > n:
            return -1
        low = max(arr)
        high = sum(arr) 

        while low <= high:
            mid = (low+high)//2
            count = self.count_students(arr, mid)

            if count <= k:
                high = mid-1
            else:
                low = mid + 1
        return low

    def count_students(self, arr, pageSize):
        students = 1
        pagePerStudent = 0
        for pages in arr:
            if pagePerStudent + pages <= pageSize:
                pagePerStudent += pages
            else:
                students += 1
                pagePerStudent = pages

        return students
        





             
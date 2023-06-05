/*
https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/828/
Given an m x n matrix, return all elements of the matrix in spiral order.


1 2  3  4
5 6  7  8   (4*3) 2
9 10 11 12

[] -> []

[1] -> [1]

1
2 (2*1) 1 -> 1-2 

 1  2  3  4  5    
 6  7  8  9  0 -> 1 2 3 4 5 0 -5 -4 -3 -2 -1 6 1
-1 -2 -3 -4 -5

1 2 3 
4 5 6 (3*3) 2 -> 1-2-3-6-0-8-7-4-5-6 K-0>1
7 8 0

m=3
n=3

k = 1 
5-

[1, 2, 3, 4]
[5, 6, 7, 8] (3*4) -> 1-2-3-4-8-12-11-10-9-5-6-7
[9,10,11,12]

m=3
n=4

k=0
1-2-3-4-8-12-11-10-9-5

k=1
6-7-

[6,9,7]
m=1, n=3
k=0 6-9-7-

7
9
6

m=3,n=1
k = 0
7-9-6-

*/

public class Solution{
	   public IList<int> SpiralOrder(int[][] matrix) {
	   var res = new List<int>();
	   int m = matrix.Length;
	   int n = matrix[0].Length;
       int k = 0 ;
       	while(k < n-k && k < m-k){
       		for(int topCol = k; topCol<n-k; topCol++){
       			res.Add(matrix[k][topCol]);
       		}

       		if(m-k-k <2)
       		{
       			k++;
       			continue;
       		}
       		
       		for(int rightRow = k+1; rightRow < m-k; rightRow++){
       			res.Add(matrix[rightRow][n-k-1]);
       		}

       		if(n-k-k <2)
       		{
       			k++;
       			continue;
       		}

       		for(int bottomCol = n-k-2; bottomCol >= k; bottomCol--){
       			res.Add(matrix[m-k-1][bottomCol]);
       		}

       		for(int leftRow = m-k-2; leftRow > k; leftRow--){
       			res.Add(matrix[leftRow][k]);
       		}
       		k++;
       }
       return res;
    }
}
/* 
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/
1 2 3    7 4 1
4 5 6 -> 8 5 2
7 8 9    9 6 3 

1 4 7
2 5 8
3 6 9

1  2  3  4     9  5  1
5  6  7  8 -> 10  6  2
9 10 11 12    11  7  3
              12  8  4

1 5  9 
2 6 10 
3 7 11
4 8 12


 1  2  3  4    13   9  5  1
 5  6  7  8 -> 14  10  6  2
 9 10 11 12    15  11  7  3
13 14 15 16    16  12  8  4

1 5 9  13
2 6 10 14 
3 7 11 15
4 8 12 16 
*/
public class Solution{
	public void Rotate(int[][] matrix){
		// Transpose
		int n = matrix.Length;
		for(int i = 0 ; i<n;i++){
			for(int j = i ; j<n;j++){
				int temp = matrix[i][j];
				matrix[i][j] = matrix[j][i];
				matrix[j][i] = temp;
			}
		}
		
		// Reverse rows
		for(int i = 0 ; i<n;i++){
			for(int j = 0 ; j<(n/2);j++){
				int temp = matrix[i][j];
				matrix[i][j] = matrix[i][n-j-1];
				matrix[i][n-j-1] = temp;
			}
		}
		
	}
}


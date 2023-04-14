//https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/777/
//Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
public class Solution {
    public void SetZeroes(int[][] matrix) {
        var zeroRows = new HashSet<int>();
        var zeroCols = new HashSet<int>();
        for(int i=0; i<matrix.Length;i++)
        {
            for(int j=0; j<matrix[i].Length;j++)
            {
                if(matrix[i][j]==0)
                {
                    zeroRows.Add(i);
                    zeroCols.Add(j);
                }
            }   
        }
        foreach(int row in zeroRows)
        {
            for(int j=0; j<matrix[row].Length;j++)
            {
                matrix[row][j] = 0;
            }
        }

        foreach(int col in zeroCols)
        {
            for(int i=0; i<matrix.Length;i++)
            {
                matrix[i][col] = 0;
            }
        }
    }
}


//

public class Solution {
    public void SetZeroes(int[][] matrix) {
        var zeroRows = new HashSet<int>();
        var zeroCols = new HashSet<int>();
        for(int i=0; i<matrix.Length;i++)
        {
            for(int j=0; j<matrix[i].Length;j++)
            {
                if(matrix[i][j]==0)
                {
                    zeroRows.Add(i);
                    zeroCols.Add(j);
                }
            }   
        }

        for(int i=0; i<matrix.Length;i++)
        {
            for(int j=0; j<matrix[i].Length;j++)
            {
                if(zeroRows.Contains(i) || zeroCols.Contains(j))
                {
                    matrix[i][j]=0;
                }
            }   
        }
    }
}

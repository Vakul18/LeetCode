/*
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/769/
1. duplicate element in 3*3 box
2. duplicate element in a row
3. duplicate element in a col
4. valid sudoku

[["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]
*/

public class Solution{
	public bool IsValidSudoku(char[][] board){
		// Row, col
		for(int i = 0 ; i<9;i++){
			var colSet = new bool[9];
			var rowSet = new bool[9];
			for(int j = 0 ; j<9 ; j++){
				//Console.WriteLine($" i,j = {i},{j}");
				if(board[i][j]!='.'){
					//Console.WriteLine($"row board[i][j] = {board[i][j]}");
                    int rowValue = Int32.Parse(board[i][j].ToString())-1;
                    //Console.WriteLine($"row value = {rowValue}");
					if(!rowSet[rowValue]){
						rowSet[rowValue] = true;
					}
					else{
						return false;
					}
				}
				if(board[j][i]!='.'){
                    //Console.WriteLine($"col board[j][i] = {board[j][i]}");
					int colValue = Int32.Parse(board[j][i].ToString())-1;
                    //Console.WriteLine($"col value = {colValue}");
					if(!colSet[colValue]){
						colSet[colValue] = true;
					}
					else{
						return false;
					}
				}
				
				
			}
		}
		
		// 3*3 boxes
		for(int k = 0 ; k<9 ; k=k+3){
			for(int l = 0 ; l<9 ; l=l+3){
				var boxSet = new bool[9];
				for(int i = k ; i<k+3;i++){
					for(int j = l ; j<l+3;j++){
						if(board[i][j]=='.')
							continue;
                        //Console.WriteLine($"box board[i][j] = {board[i][j]}");
						int val = Int32.Parse(board[i][j].ToString())-1;
                        //Console.WriteLine($"val = {val}");
						if(!boxSet[val]){
							boxSet[val] = true;
						}
						else{
							return false;
						}		
					}
				}
			}
		}
		
		return true;	
		
	}
} 




public class Solution{
	public bool IsValidSudoku(char[][] board){
		var hs = new HashSet<string>();
		for(int i=0;i<9;i++){
			for(int j=0; j<9;j++){
				char n = board[i][j];
				if(n!='.'){
					if(!hs.Add($"row-{i}-{n}") || !hs.Add($"col-{j}-{n}") || !hs.Add($"box-{i/3}-{j/3}-{n}"))
						return false;
				}
				
			}
		}
		return true;
	}
}

/*
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
------------------------
 1 0 1    0 1 0
 0 1 0 -> 0 0 0
 1 1 1    1 1 1


[0,1,0]    0 0 0
[0,0,1] -> 1 0 1
[1,1,1]    0 1 1
[0,0,0]    0 1 0
*/
public class Solution {
    public void GameOfLife(int[][] board) {
    	List<Cell> stateChanges = new List<Cell>();

        for(int i=0; i<board.Length; i++){
        	for(int j=0; j<board[0].Length; j++){
        		int neighbours = GetNeighbours(board,i,j);
        		int state = GetNextState(neighbours);
        		if(state!=-1 && state != board[i][j]){
        			stateChanges.Add(new Cell{r = i, c = j, State = state});
        		}
        	}
        }

        foreach(var stateChange in stateChanges){
        	board[stateChange.r][stateChange.c] = stateChange.State;
        }
    }

    public int GetNeighbours(int[][] board,int r, int c){
    	int[] offset = {-1, 0, 1};
    	int neighboursCount = 0;
    	for(int i=0; i<offset.Length; i++){
    		for(int j=0; j<offset.Length; j++){
    			if(i==1 && j==1){
    				continue;
    			}
    			int row = r+ offset[i];
    			int col = c+ offset[j];
    			if((row>=0 && row<board.Length) && (col>=0 && col<board[0].Length) && (board[row][col] == 1)){
    				neighboursCount++;
    			}
    		}
    	}
    	return neighboursCount;
    }

    public int GetNextState(int neighbours){
    	if(neighbours == 3){
    		return 1;
    	}
    	else if(neighbours >=2 && neighbours <3){
    		return -1;
    	}
    	else{
    		return 0;
    	}
    }

    public class Cell{
    	public int r {get; set;}
    	public int c {get; set;}
    	public int State {get; set;}
    }
}
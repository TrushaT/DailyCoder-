'''
Date - 15/01/2020

Link to the problem : https://leetcode.com/problems/game-of-life/

The board is made up of an m x n grid of cells, where each cell has an initial state: 
live (represented by a 1) or dead (represented by a 0). 
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) 
using the following four rules (taken from the above Wikipedia article):
Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

'''
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        cells = [(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)]
        rows = len(board)
        cols = len(board[0])
        
        for m in range(rows):
            for n in range(cols):
                no_of_ones = 0 
                
                for i in cells:
                    r = (m + i[0])
                    c = (n + i[1])
                    
                    if (r< rows and r>=0 ) and (c < cols and c >= 0) and abs(board[r][c]) ==1 : 
                        no_of_ones += 1
                        
                    # print(m,n,no_of_ones)
                    
                if board[m][n] == 1 and (no_of_ones < 2 or no_of_ones > 3):
                    board[m][n] = -1

                if board[m][n] == 0 and no_of_ones == 3 :
                    board[m][n] = 2
                        
        
        for i in range(rows):
            for j in range(cols) :
                if board[i][j] > 0 :
                    board[i][j] = 1
                else :
                    board[i][j] = 0 

                
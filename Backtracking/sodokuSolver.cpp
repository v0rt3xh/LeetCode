/**
 * Review  
 * 0037 Sudoku solver
 * 
 */

class Solution 
{
private:
    bool backtrack(vector<vector<char>>& board) 
    {
        for (int i = 0; i < board.size(); i++) 
        {
            for (int j = 0; j < board[0].size(); j++) 
            {
                if (board[i][j] != '.') continue;
                // 9 numbers to try
                for (char k = '1'; k <= '9'; k++) 
                {
                    if(isvalid(i, j, k, board)) // Check if the number is possible
                    {
                        board[i][j] = k;
                        if (backtrack(board)) return true;
                        board[i][j] = '.';
                    }
                }
                return false; // Have tried 9 numbers, cannot proceed, end
            }
        }
        return true; // Why? Did not even encouter false, good to go.
    }
    
    bool isvalid(int row, int col, char number, vector<vector<char>>& board) 
    {
        // Check row possible?
        for (int i = 0; i < 9; i++) 
        {
            if (board[row][i] == number) return false;
        }
        // Check column possible?
        for (int j = 0; j < 9; j++) 
        {
            if (board[j][col] == number) return false;
        }
        // Check subbox
        int start_row = 3 * (row / 3), start_col = 3 * (col / 3);
        for (int i = start_row; i < start_row + 3; i++) 
        {
            for (int j = start_col; j < start_col + 3; j++) 
            {
                if (board[i][j] == number) return false;
            }
        }
        return true;
    }
public:
    void solveSudoku(vector<vector<char>>& board) 
    {
        backtrack(board);
    }
};
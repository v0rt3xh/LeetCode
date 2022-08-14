/**
 * 0051 N-Queens
 * Cpp version.
 */

class Solution 
{
public:
    vector<vector<string>> solveNQueens(int n) 
    {
        // Prepare the sets we need. Auto just for simplicity. 
        auto solutions = vector<vector<string>>(); // Result
        auto queens = vector<int> (n, -1); // Column position of each queen
        auto columns = unordered_set<int>();
        auto diagonals = unordered_set<int>();
        auto offDiagonals = unordered_set<int>();
        backtrack(solutions, queens, n, 0, columns, diagonals, offDiagonals);
        return solutions;
    }
    
    void backtrack(vector<vector<string>>& solutions, vector<int>& queens, int n, int row, unordered_set<int> columns, unordered_set<int> diagonals, unordered_set<int> offDiagonals) 
    {
        // Termination point
        if (row == n) 
        {
            vector<string> board = generateBoard(queens, n);
            solutions.push_back(board);
            return;
        }
        // Traverse through columns
        for (int i = 0; i < n; i++) 
        {
            // Column check
            if (columns.find(i) != columns.end()) 
            {
                continue;
            }
            // Diagonal check
            if (diagonals.find(row - i) != diagonals.end()) 
            {
                continue;
            }
            if (offDiagonals.find(row + i) != offDiagonals.end()) 
            {
                continue;
            }
            queens[row] = i; // Try this position
            columns.insert(i);
            diagonals.insert(row - i);
            offDiagonals.insert(row + i);
            backtrack(solutions, queens, n, row + 1, columns, diagonals, offDiagonals);
            queens[row] = -1; // Backtrack
            columns.erase(i);
            diagonals.erase(row - i);
            offDiagonals.erase(row + i);
        }
    }
    
    vector<string> generateBoard(vector<int>& queens, int n) 
    {
        auto board = vector<string>();
        for (int i = 0; i < n; i++) 
        {
            string row = string(n, '.');
            row[queens[i]] = 'Q';
            board.push_back(row);
        }
        return board;
    }
};
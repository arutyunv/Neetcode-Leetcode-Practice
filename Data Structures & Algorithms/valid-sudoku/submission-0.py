### Hash Set (One Pass) Approach ###

"""
Instead of checking rows, columns, and 3×3 boxes separately, we can validate the entire Sudoku board in one single pass.
For each cell, we check whether the digit has already appeared in:
    * the same row
    * the same column
    * the same 3×3 box
We track these using three hash sets:

    * rows[r] keeps digits seen in row r
    * cols[c] keeps digits seen in column c
    * squares[(r // 3, c // 3)] keeps digits in the 3×3 box

(Note: // is integer (floor) division in Python
It divides and then throws away the decimal part, keeping only the whole number, so r, c = 0, 1, 2 // 3 = 0 square box)

If a digit appears again in any of these places, the board is invalid.

"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create 9 sets for rows and columns
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        
        # Use a normal dictionary for 3x3 squares
        # Key = (row_group, col_group), e.g. (0,0), (0,1), ..., (2,2)
        # Value = set of digits seen in that square
        squares = {}

        # Go through every cell in the board
        for r in range(9):
            for c in range(9):
                val = board[r][c]

                # Skip empty cells
                if val == ".":
                    continue

                # Identify which 3x3 box this cell belongs to
                # Example: cell (4,7) -> (1,2)
                key = (r // 3, c // 3)

                # If this square hasn't been seen before, create a set for it
                if key not in squares:
                    squares[key] = set()

                # Check if the value already exists in:
                # - the current row
                # - the current column
                # - the current 3x3 square
                if val in rows[r]:
                    return False
                if val in cols[c]:
                    return False
                if val in squares[key]:  # keeps digits in the 3×3 box
                    return False

                # Add the value to the corresponding row, column, and square
                rows[r].add(val)
                cols[c].add(val)
                squares[key].add(val)  # store digit in its 3×3 box

        # No duplicates found → valid Sudoku
        return True
from typing import List

"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.


"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      help_hash = {i:[] for i in range(9)}
      for i in range(9):
        if not self.unique_nine(board[i]):
          return False

      for i in range(9):
        for j in range(9):
          help_hash[j].append(board[i][j])
      for e in help_hash.keys():
         if not self.unique_nine(help_hash[e]):
          return False
      
      one, two, three = [], [], []
      for i in range(9):
        one.extend(board[i][0:3])
        two.extend(board[i][3:6])
        three.extend(board[i][6:])
      
        if (i+1) % 3 == 0:
          if not self.unique_nine(one) or not self.unique_nine(two) or not self.unique_nine(three):
            return False
          one, two, three = [],[],[]

      return True



    def unique_nine(self,numbers):
      hash_table = {}
      for i in range(9):
        if not numbers[i] in hash_table:
          if numbers[i] != ".":
            hash_table[numbers[i]] = True
        else:
          return False
      return True   
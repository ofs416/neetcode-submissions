from collections import Counter
import copy

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        col_list = copy.deepcopy(board)
        for i in range(0,9):
            for j in range(0,9):
                col_list[i][j] = board[j][i]

        seg_list = [[] for _ in range(9)]
        for seg_row in range(0,3):
            for seg_col in range(0,3):
                seg_index = seg_row * 3 + seg_col
                for row in range(0,3):
                    for col in range(0,3):
                        seg_list[seg_index].append(board[seg_row*3+row][seg_col*3+col])

        
        def check(temp_board: List[List[str]]) -> bool:
            for c in temp_board:
                count = Counter(c)
                del count["."]
                if any(v > 1 for v in count.values()):
                    return False 

            return True

        return check(board) & check(seg_list) & check(col_list)
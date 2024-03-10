class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowHash = collections.defaultdict(set)  # key = row number
        colHash = collections.defaultdict(set)  # key = col number
        boxHash = collections.defaultdict(set)  # key = tuple representing box number (0,0), (0,1), (0,2)
                                                # (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                
                if (board[i][j] in rowHash[i] or
                    board[i][j] in colHash[j] or
                    board[i][j] in boxHash[(i//3, j//3)]):
                    return False
                
                rowHash[i].add(board[i][j])
                colHash[j].add(board[i][j])
                boxHash[(i//3, j//3)].add(board[i][j])
        
        return True

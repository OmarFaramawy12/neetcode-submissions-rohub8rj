from collections import defaultdict

class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        find duplicates in each row and column
        I- Time Complexity: O(n^2)
            1- find duplicates if exist in each  row + digits allowed only (1-9)
            2- find duplicates if exist in each column  + digits allowed only (1-9)
            3- Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates
            - Main Trick for checking for squares:
                1- have 9 squares got indexed -> {(0,0) , (0,1) , (0,2)
                                                  (1,0) , (1,1) , (1,2)                 
                                                  (2,0) , (2,1) , (2,2)}
                2- Mop each pair of row & column or original matrix (suduko) -> to the indices that represent the squares
                    - Mathematical Formula: (row // 3 , col // 3) -> gives us the mapped square
        
        II- Space Complexity:
            1- use 3 HashMap 
                a- Hashmap for each Column (n Columns)
                b- Hashmap for each Row (n Rows)
                c- Hashmap for each 3*3 squares (n Sqaures)
            2- Hashmap will have the following structure:
                a- Row & Column Case: -> Hashmap key will be the row and Column number respectively
                 & valuewill be Hashset to track duplicates in each row or column
                
                B- 3*3 Square Matrices:
                    - key will be tuple (row // 3 , column // 3)
                    - value: hashset to track the 9 elements in every sqaure
        
        
        
        '''

        # step-1: check evry row + column (i -> rows , j -> columns)
        cols_map = defaultdict(set) # key will be column no
        rows_map = defaultdict(set) # key will be row no
        squares_map = defaultdict(set) # key will be tuple (row // 3 , col // 3)
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == ".":
                    continue
                # Step-1 cheking for duplicates by checking hashmap
                if (board[row][col] in rows_map[row] or
                    board[row][col] in cols_map[col] or
                    board[row][col] in squares_map[row // 3 , col // 3 ]):
                    return False
                rows_map[row].add(board[row][col])
                cols_map[col].add(board[row][col])
                squares_map[row // 3  , col // 3].add(board[row][col])
        return True





        
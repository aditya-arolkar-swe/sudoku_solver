class Board:
    SQUARE_COORDS = [
        [0, 0], [3, 0], [6, 0],
        [0, 3], [3, 3], [6, 3],
        [0, 6], [3, 6], [6, 6],
    ]
    def __init__(self, board_str: str):
        """
        Enter a string like so:
            "63     98"
            "  7  4  6 "
            "     817 "
            "4 8   3  "
            "  38 69  "
            "  2   7 6"
            " 761     "
            " 5  3 6  "
            "34     57"
        
        blank spaces = empty cells
        filled spaces = set number 
        """
        self.board = []
        for line in board_str.split('\n'):
            if len(line) == 0:
                continue
            
            line = line.replace("\"", "")

            if len(line) > 9:
                print(line)
            
            curr_row = [0] * 9
            self.board.append(curr_row)
            for i, char in enumerate(line):
                if char == ' ':
                    continue
                curr_row[i] = int(char)
        
        self.refresh()

    def refresh(self):
        self.squares = [self.get_square_nums(x, y) for x, y in self.SQUARE_COORDS]
        self.columns = [self.get_col_nums(i) for i in range(9)]

    def __str__(self):
        board_str = ''
        for i, row in enumerate(self.board):
            if i % 3 == 0:
                board_str += (' - ' * 3 + '|') * 3 + '\n'
            for j, char in enumerate(row):
                if j % 3 == 0 and j > 0:
                    board_str += '|'

                board_str += f' {char} ' if char != 0 else '   '
            
            board_str += '\n'
        
        return board_str
    
    def get_col_nums(self, col_idx: int) -> list[int]:
        return [self.board[i][col_idx] for i in range(9)]
    
    @staticmethod
    def has_repeats(nums: list[int]) -> bool:
            nums_set = set()
            for n in nums:
                if n == 0:
                    continue
                if n in nums_set:
                    return True
                nums_set.add(n)
            
            return False
    
    def coords_to_square_idx(self, x: int, y: int) -> int:
        for i, (square_x, square_y) in enumerate(self.SQUARE_COORDS):
            if square_x <= x < square_x + 3 and square_y <= y < square_y + 3:
                return i

    def get_square_nums(self, square_x: int, square_y: int) -> set[int]:
        """

        square_x = x coordinate of top left of square
        square_y = y coordinate of top left of square

        0-based index

        """
        square = []

        for y, row in enumerate(self.board):
            for x, val in enumerate(row):
                if square_x <= x < square_x + 3 and square_y <= y < square_y + 3:
                    square.append(val)
        
        return square
    
    def set_val(self, x, y, val) -> None:
        self.board[y][x] = val
        self.refresh()

    def is_valid(self) -> bool:
        # if every row doesn't repeat 1 -> 9
        for row in self.board:
            if self.has_repeats(row):
                print(f' [Err] Row {row} has repeats!')
                return False

        # if every column doesn't repeat 1 -> 9
        for col in self.columns:
            if self.has_repeats(col):
                print(f' [Err] Column {col} has repeats!')
                return False

        # if every square doesn't repeat 1 -> 9
        for square in self.squares:
            if self.has_repeats(square):
                print(f' [Err] Square {x}, {y}: {square} has repeats!')
                return False
        
        return True

    def is_solved(self, verbose: bool = False) -> bool:
        if not self.is_valid:
            return False
        
        # if every row has 1 -> 9
        for row in self.board:
            if sum(row) != 45:
                if verbose:
                    print(f' [Err] Row {row} does not have 1->9!')
                return False

        # if every column doesn't repeat 1 -> 9
        for col in self.columns:
            if sum(col) != 45:
                if verbose:
                    print(f' [Err] Column {col} does not have 1->9!')
                return False

        # if every square doesn't repeat 1 -> 9
        for square in self.squares:
            if sum(square) != 45:
                if verbose:
                    print(f' [Err] Square {x}, {y}: {nums} does not have 1->9!!')
                return False
        
        return True

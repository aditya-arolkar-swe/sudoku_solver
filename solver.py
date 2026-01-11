from board import Board

class Solver:
    def __init__(self, board: Board):
        self.b: Board = board
        self.guesses = [r.copy() for r in self.b.board.copy()]

        for y, row in enumerate(self.b.board):
            for x, val in enumerate(row):
                if val == 0:
                    self.guesses[y][x] = set()

    def populate_guesses(self):
        for y, row in enumerate(self.guesses):
            for x, val in enumerate(row):
                if type(val) != int:
                    # reset the guesses on each refresh
                    self.guesses[y][x] = set()

                    # get the column, row and square
                    column = self.b.columns[x]
                    square = self.b.squares[self.b.coords_to_square_idx(x, y)]

                    possible_nums_from_row = [num for num in range(1, 10) if num not in row]

                    for n in possible_nums_from_row:
                        # print(n, type(n))
                        if n not in column and n not in square:
                            # print('got here')
                            self.guesses[y][x].add(n)
    
    def check_guesses_and_set(self) -> bool:
        should_refresh = False
        for y, row in enumerate(self.b.board):
            for x, val in enumerate(row):
                if type(self.guesses[y][x]) == set and len(self.guesses[y][x]) == 1:
                    print(f' -> Cell [{x}, {y}] can only be {self.guesses[y][x]}')
                    new_num = self.guesses[y][x].pop()
                    self.b.set_val(x, y, new_num)
                    self.guesses[y][x] = new_num

                    should_refresh = True

        return should_refresh

    def solve(self) -> None:
        should_loop = True
        i = 1
        while should_loop:
            if self.b.is_solved():
                print("=" * 30)
                print(' '*8 + ' === SOLVED ===' + ' '*8)
                print("=" * 30)
                print(self.b)
                return
            
            print( '-'*10 + f' Loop {i} ' + '-'*10)
            print(self.b)
            self.populate_guesses()
            should_loop = self.check_guesses_and_set()
            i += 1

        print( '-'*25 + f' Current Guesses ' + '-'*25)
        for row in self.guesses:
            print(row)

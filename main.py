from board import Board
from solver import Solver

if __name__ == "__main__":
#     board_str = """
# "63     98"
# "  7 4  6 "
# "     817 "
# "4 8   3  "
# "  38 69  "
# "  2   7 6"
# " 761     "
# " 5  3 6  "
# "34     57"
# """

#     board_str = """
# 431 96287
# 97 8 4 56
# 68  731  
#  6 78 41 
#  5413986 
#  13 42 9 
#   842  31
# 12 3 8 74
# 34796 528
# """

    board_str = """
  53  28 
649 82 1 
8321 9456
1 7 389 2
32 945 78
9 472 3 5
2914 6837
 6 89 521
 78  36  
"""

    board = Board(board_str)
    s = Solver(board)
    s.solve()

    
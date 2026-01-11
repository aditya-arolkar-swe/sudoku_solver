# Sudoku Solver

## Strat A - Simple Guessing Elimination 
 - Accumulates all possible legal numbers for each cell 
 - If any cell has only 1 possible number, assign that to the board
 - repeat until either board is solved or there are no trivial assignments

Strat A works to solve medium difficulty instantly. Hard difficulty would involve more sophisticated logic

## Strat B - Hypothesize then Pan out
 - hypothesize a number in a certain cell where 2 or more are possible
 - pan out the rest of the board's guesses using strat A
 - arrive at:
    - solved board 
    - impossible board
        - revert back all moves after hypothesis and try another hypothesis
    - board with no trivial guesses
        - apply a second degree guess
 - repeat all possible hypotheses until solved 

 Needs implementation...
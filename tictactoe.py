"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x = 0
    o = 0

    # count the number of Xs and Os
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == X:
                x += 1
            elif board[i][j] == O:
                o += 1

    # return the correct turn based on count
    if x == 5:
        return 5
    elif x > o:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    #initialise set
    acts = set()

    # loop through all board positions, checking if it has been filled
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == None:
                acts.add((i,j))

    return acts

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # make a deepcopy
    boardplus = deepcopy(board)

    # find out whose turn it is
    move = player(board)

    # raise exception if action is not valid
    if board[action[0]][action[1]] != None:
        raise ValueError("Function -> 'result': Not a valid action input into board.")

    # create the result
    if move == O:
        boardplus[action[0]][action[1]] = move
    else:
        boardplus[action[0]][action[1]] = move

    return boardplus

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    size = len(board)

    # initialize row and column counts
    row = [0]*size
    col = [0]*size
    diagback = [0]
    diagfor = [0]

    #loop through all board positions
    for i in range(size):
        for j in range(size):
            # count the respect positions
            if board[i][j] != None:
                if board[i][j] == X:
                    row[i] += 1
                    col[j] += 1
                    if i == j:
                        diagback[0] += 1
                    if i + j == 2:
                        diagfor[0] += 1
                else:
                    col[j] += -1
                    row[i] += -1
                    if i == j:
                        diagback[0] += -1
                    if i + j == 2:
                        diagfor[0] += -1

    # check if there are three in a row
    if max(row) == 3 or max(col) == 3 or diagfor[0] == 3 or diagback[0] == 3:
        return X
    elif min(row) == -3 or min(col) == -3 or diagfor[0] == -3 or diagback[0] == -3:
        return O
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == None:
                return False

    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    champ = winner(board)

    if champ == X:
        return 1
    elif champ == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board) == True:
        return None

    # check whose turn it is
    if player(board) == X:
        # set a tmp variable
        tmp = -math.inf

        #loop through all possible actions at k = 1
        for action in actions(board):
            # receive the final value of that action
            val = min_player(result(board, action))
            # exit loop if that action is optimal
            if val == 1:
                return action
            #else find which of the remaining actions have the max value
            elif val > tmp:
                tmp = val
                act = action
        #return the act that maximises the value
        return act

    else:
        tmp = math.inf
        for action in actions(board):
            val = max_player(result(board, action))
            if val == -1:
                return action
            elif val < tmp:
                tmp = val
                act = action

        return act

def min_player(board):
    # return the utility at the end of recursion
    if terminal(board):
        return utility(board)

    v = math.inf
    # loop through all possible action for k = 2 (the first time this function is called, thereafter k = 3... 4...)
    for action in actions(board):
        v = min(v, max_player(result(board, action)))
        # pruning
        if v == -1:
            return v
    return v

def max_player(board):

    if terminal(board):
        return utility(board)

    v = -math.inf
    for action in actions(board):
        v = max(v, min_player(result(board, action)))
        if v == 1:
            return v
    return v

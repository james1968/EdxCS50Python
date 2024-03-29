from typing import *
import copy
import random

# global variable for bold and blue text
bold_start = "\033[1m"
bold_end = "\033[0;0m"
blue_text = '\033[96m'
blue_text_end = '\033[0:0m'

def location2index(loc: str) -> Tuple[int, int]:
    '''converts chess location to corresponding x and y coordinates'''
    # check the first coordinate is a letter from a - z
    try:
        if loc[0].isalpha():
            pass
        else:
            return "The first coordinate must be a letter"
    except ValueError as e:
        return "The first coordinate must be a letter"

    '''Populate tuple with x, y coordinates.  Check that second coordinate is an integer and it is no longer
    than the length of the board.'''
    try:
        int(loc[1:])
        if int(loc[1:]) > 26:
            return "Invalid y value is larger than board size."
        coords = ((int(ord(loc[0].lower())) - 96), int(loc[1:]))
    except Exception as e:
        return "Second item must be an integer."


    return coords

def index2location(x: int, y: int) -> str:
    '''converts  pair of coordinates to corresponding location'''
    '''Check input variables are ints and that the values are less than the max length of the
    board and return ValueError'''
    if type(x) != int or type(y) != int:
        print("x or y coordinate must be an integer")
        raise ValueError

    if x > 26 or y > 26:
        print("x or y coordinate must be less than maximum board length")
        raise ValueError


    str_coord = (chr(x + 96) + str(y))
    return str_coord


class Piece:
    pos_X: int
    pos_Y: int
    side: bool  # True for White and False for Black

    def __init__(self, pos_X: int, pos_Y: int, side: bool):
        '''sets initial values'''
        self.pos_X = pos_X
        self.pos_Y = pos_Y
        self.side = side


Board = Tuple[int, List[Piece]]


def is_piece_at(pos_X: int, pos_Y: int, B: Board) -> bool:
    '''checks if there is piece at coordinates pox_X, pos_Y of board B'''
    '''check to see if the coordinates being checked are too long for the board and raise and error'''
    '''validation check to ensure coordinates are not longer than the board length'''

    # check the X and Y coordinates to see if piece is on the board.
    for i in B[1]:
        X = i.pos_X
        Y = i.pos_Y
        if X == pos_X and Y == pos_Y:
            return True
    return False


def piece_at(pos_X: int, pos_Y: int, B: Board) -> Piece:
    '''
    returns the piece at coordinates pox_X, pos_Y of board B
    assumes some piece at coordinates pox_X, pos_Y of board B is present'''

    '''Return the piece at the submitted coordinates'''
    if is_piece_at(pos_X, pos_Y, B):
        for i in B[1]:
            if pos_X == i.pos_X and pos_Y == i.pos_Y:
                return i
    else:
        return False


class Rook(Piece):
    def __init__(self, pos_X: int, pos_Y: int, side: bool):
        '''sets initial values by calling the constructor of Piece'''
        Piece.__init__(self, pos_X, pos_Y, side)


    def can_reach(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''
        checks if this rook can move to coordinates pos_X, pos_Y
        on board B according to rule [Rule2] and [Rule4](see section Intro)
        Hint: use is_piece_at'''

        # check there is a Rook at the coordinates of the piece.
        try:
            piece_at(self.pos_X, self.pos_Y, B)
        except AttributeError as A:
            print("There is no Rook at these coordinates")
            raise AttributeError

        # for the Rook either the X or Y coord has to be the same for it to be able to move to a square.
        if self.pos_X != pos_X and self.pos_Y != pos_Y:
            return False

        # if there is a piece of the same colour at the x and y coordinates piece can't move there.
        if is_piece_at(pos_X, pos_Y, B) and piece_at(pos_X, pos_Y, B).side == self.side:
            return False

        '''these conditions check the horizontal and vertical from left to right and bottom to top for pieces
        of the same colour that might block the piece moving'''
        if pos_X == self.pos_X or pos_Y == self.pos_Y:
            if pos_X > self.pos_X:
                for i in range(pos_X-1, self.pos_X, -1):
                    if is_piece_at(i, pos_Y, B):
                        return False
                return True
            if pos_Y > self.pos_Y:
                for j in range(pos_Y-1, self.pos_Y, -1):
                    if is_piece_at(pos_X, j, B):
                        return False
                return True

            '''These conditions check the horizontal and vertical from right to left and top to bottom for pieces of the
            same colour that might block the piece moving'''
            if self.pos_X > pos_X:
                for i in range(pos_X+1, self.pos_X):
                    if is_piece_at(i, pos_Y, B):
                        return False
                return True
            if self.pos_Y > pos_Y:
                for j in range(pos_Y+1, self.pos_Y):
                    if is_piece_at(pos_X, j, B):
                        return False
                return True


    def can_move_to(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''
        checks if this rook can move to coordinates pos_X, pos_Y
        on board B according to all chess rules

        Hints:
        - firstly, check [Rule2] and [Rule4] using can_reach
        - secondly, check if result of move is capture using is_piece_at
        - if yes, find the piece captured using piece_at
        - thirdly, construct new board resulting from move
        - finally, to check [Rule5], use is_check on new board
        '''
        r_check_side: bool = self.side
        size: int = B[0]
        # make sure the piece can reach  square in question
        if not self.can_reach(pos_X, pos_Y, B):
            return False
        # create two pieces one for the piece to be moved and one for the moved piece
        r_new_list_pieces: list[Piece] = copy.deepcopy(B[1])
        r_moved_piece: Piece = type(self)(pos_X, pos_Y, self.side)

        # remove the piece that is to be moved from the board
        if self.can_reach(pos_X, pos_Y, B) and not is_piece_at(pos_X, pos_Y, B):
            for i in r_new_list_pieces:
                if i.pos_X == self.pos_X and i.pos_Y == self.pos_Y and type(i) == type(self) and i.side == self.side:
                    r_new_list_pieces.remove(i)

        # remove the piece to be moved and the captured piece from the board
        elif self.can_reach(pos_X,pos_Y,B) and is_piece_at(pos_X, pos_Y,B):
            r_cap_piece: Piece = piece_at(pos_X, pos_Y, B)
            for i in r_new_list_pieces:
                if i.pos_X == r_cap_piece.pos_X and i.pos_Y == r_cap_piece.pos_Y and type(i) == type(r_cap_piece) and i.side == r_cap_piece.side:
                    r_new_list_pieces.remove(i)
            for i in r_new_list_pieces:
                if i.pos_X == self.pos_X and i.pos_Y == self.pos_Y and type(i) == type(self) and i.side == self.side:
                    r_new_list_pieces.remove(i)

        # add the moved piece to the board
        r_new_list_pieces.append(r_moved_piece)

        # create a new board with the moved piece on and return if it is not check
        r_temp_board: Board = (size, r_new_list_pieces)

        if is_check(r_check_side, r_temp_board):
            return False
        else:
            return True

    def move_to(self, pos_X: int, pos_Y: int, B: Board) -> Board:
        '''
        returns new board resulting from move of this rook to coordinates pos_X, pos_Y on board B
        assumes this move is valid according to chess rules
        '''



        r_new_piece: Piece = Rook(pos_X, pos_Y, self.side)

        # create a copy of the board to use to move the pieces on
        r_new_board_pieces = copy.deepcopy(B[1])
        r_cap_piece = piece_at(pos_X, pos_Y, B)
        r_new_board: Board = (B[0], r_new_board_pieces)

        # move the pieces on the board, removing the original piece and any captured pieces
        if self.can_move_to(pos_X, pos_Y, B):
            for i in r_new_board_pieces:
                if type(i) == type(self) and i.pos_X == self.pos_X and i.pos_Y == self.pos_Y and i.side == self.side:
                    r_new_board_pieces.remove(i)
                if r_cap_piece:
                    if type(i) == type(r_cap_piece) and i.pos_X == r_cap_piece.pos_X and i.pos_Y == r_cap_piece.pos_Y and i.side == r_cap_piece.side:
                        r_new_board_pieces.remove(i)

            r_new_board_pieces.append(r_new_piece)

        return r_new_board


class Bishop(Piece):
    def __init__(self, pos_X: int, pos_Y: int, side: bool):
        '''sets initial values by calling the constructor of Piece'''
        Piece.__init__(self, pos_X, pos_Y, side)

    def can_reach(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''checks if this bishop can move to coordinates pos_X, pos_Y on board B according to rule [Rule1] and [Rule4]'''

        # checks for difference between x and y values to ensure can move diagonally from left to right.
        if ((self.pos_X - pos_X) - (self.pos_Y - pos_Y)) == 0:
            if not is_piece_at(pos_X, pos_Y, B) or piece_at(pos_X, pos_Y, B).side != self.side:
                if pos_X > self.pos_X and pos_Y > self.pos_Y:
                    for i in range(1, pos_X):
                        if is_piece_at(self.pos_X+i, self.pos_Y+i, B) and piece_at(self.pos_X+i, self.pos_Y+i, B).side == self.side:
                            return False
                    return True
                if pos_X < self.pos_X and pos_Y < self.pos_Y:
                    for i in range(1, self.pos_X):
                        if is_piece_at(self.pos_X-i, self.pos_Y-i, B) and piece_at(self.pos_X-i, self.pos_Y-i, B) == self.side:
                            return False
                    return True

        # checks for difference between x and y values to ensure can move diagonally from right to left.
        if ((self.pos_X - pos_X) + (self.pos_Y - pos_Y)) == 0:
            if not is_piece_at(pos_X, pos_Y, B) or piece_at(pos_X, pos_Y, B).side != self.side:
                if pos_X < self.pos_X and pos_Y > self.pos_Y:
                    for i in range(1, pos_Y):
                        if is_piece_at(self.pos_X-i, self.pos_Y+i, B) and piece_at(self.pos_X-i, self.pos_Y+i, B) == self.side:
                            return False
                    return True
                if pos_X > self.pos_X and pos_Y < self.pos_Y:
                    for i in range(1, self.pos_Y):
                        if is_piece_at(self.pos_X+i, self.pos_Y-i, B) and piece_at(self.pos_X+i, self.pos_Y-i, B) == self.side:
                            return False
                    return True
        return False

    def can_move_to(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''checks if this bishop can move to coordinates pos_X, pos_Y on board B according to all chess rules'''
        if not self.can_reach(pos_X, pos_Y, B):
            return False

        b_move_piece: Piece = type(self)(pos_X, pos_Y, self.side)
        b_check_side: bool = self.side
        b_new_list: list[Piece] = copy.deepcopy(B[1])
        size: int = B[0]

        # moves pieces on a new temp board
        if self.can_reach(pos_X, pos_Y, B) and not is_piece_at(pos_X, pos_Y, B):
            for i in b_new_list:
                if i.pos_X == self.pos_X and i.pos_Y == self.pos_Y and type(i) == type(self) and i.side == self.side:
                    b_new_list.remove(i)
            b_new_list.append(b_move_piece)

        if self.can_reach(pos_X, pos_Y, B) and is_piece_at(pos_X, pos_Y, B):
            b_cap_piece: Piece = piece_at(pos_X, pos_Y, B)
            for i in b_new_list:
                if i.pos_X == self.pos_X and i.pos_Y == self.pos_Y and type(i) == type(self) and i.side == self.side:
                    b_new_list.remove(i)
                if i.pos_X == b_cap_piece.pos_X and i.pos_Y == b_cap_piece.pos_Y and type(i) == type(b_cap_piece) and i.side == b_cap_piece.side:
                    b_new_list.remove(i)
            b_new_list.append(b_move_piece)

        b_temp_board: Board = (size, b_new_list)

        # checks for check on the temp board created above and returns boolean
        if is_check(b_check_side, b_temp_board):
            return False
        else:
            return True

    def move_to(self, pos_X: int, pos_Y: int, B: Board) -> Board:
        '''
        returns new board resulting from move of this bishop to coordinates pos_X, pos_Y on board B
        assumes this move is valid according to chess rules
        '''
        b_new_piece: Piece = Bishop(pos_X, pos_Y, self.side)
        b_new_board_pieces = copy.deepcopy(B[1])
        b_cap_piece = piece_at(pos_X, pos_Y, B)
        b_new_board: Board = (B[0], b_new_board_pieces)

        # moves piece to new position and removes captured piece if applicable
        if self.can_move_to(pos_X, pos_Y, B):
            for i in b_new_board_pieces:
                if type(i) == type(self) and i.pos_X == self.pos_X and i.pos_Y == self.pos_Y and i.side == self.side:
                    b_new_board_pieces.remove(i)
                if b_cap_piece:
                    if type(i) == type(b_cap_piece) and i.pos_X == b_cap_piece.pos_X and i.pos_Y == b_cap_piece.pos_Y and i.side == b_cap_piece.side:
                        b_new_board_pieces.remove(i)

            b_new_board_pieces.append(b_new_piece)

        return b_new_board


class King(Piece):
    def __init__(self, pos_X: int, pos_Y: int, side: bool):
        '''sets initial values by calling the constructor of Piece'''
        Piece.__init__(self, pos_X, pos_Y, side)

    def can_reach(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to rule [Rule3] and [Rule4]'''

        # uses absolute values to check that the king can move one space horizontally or vertically
        if abs(self.pos_X - pos_X) + abs(self.pos_Y - pos_Y) <= 1:
            if not is_piece_at(pos_X, pos_Y, B) or piece_at(pos_X, pos_Y, B).side != self.side:
                return True
            else:
                return False

        # uses absolute values to see if KIng can move one space vertically left to right and right to left
        if abs(self.pos_X - pos_X) == 1 and abs(self.pos_Y - pos_Y) == 1:
            if not is_piece_at(pos_X, pos_Y, B) or piece_at(pos_X, pos_Y, B).side != self.side:
                return True
            else:
                return False
        return False

    def can_move_to(self, pos_X: int, pos_Y: int, B: Board) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to all chess rules'''

        if not self.can_reach(pos_X, pos_Y, B):
            return False
        k_move_piece: Piece = type(self)(pos_X, pos_Y, self.side)
        k_check_side: bool = self.side
        k_new_list: List[Piece] = copy.deepcopy(B[1])
        size: int = B[0]

        # moves piece and captured piece if applicable on a temp board and checks for "check".
        if self.can_reach(pos_X, pos_Y, B) and not is_piece_at(pos_X, pos_Y, B):
            for i in k_new_list:
                if i.pos_X == self.pos_X and i.pos_Y == self.pos_Y and type(i) == type(self) and i.side == self.side:
                    k_new_list.remove(i)
            k_new_list.append(k_move_piece)

        elif self.can_reach(pos_X, pos_Y, B) and is_piece_at(pos_X, pos_Y, B):
            k_cap_piece: Piece = piece_at(pos_X, pos_Y, B)
            for i in k_new_list:
                if i.pos_X == self.pos_X and i.pos_Y == self.pos_Y and type(i) == type(self) and i.side == self.side:
                    k_new_list.remove(i)
                if i.pos_X == k_cap_piece.pos_X and i.pos_Y == k_cap_piece.pos_Y and type(i) == type(k_cap_piece) and i.side == k_cap_piece.side:
                    k_new_list.remove(i)
            k_new_list.append(k_move_piece)

        k_temp_board: Board = (size, k_new_list)
        if is_check(k_check_side, k_temp_board):
            return False
        else:
            return True

    def move_to(self, pos_X: int, pos_Y: int, B: Board) -> Board:
        '''
        returns new board resulting from move of this king to coordinates pos_X, pos_Y on board B
        assumes this move is valid according to chess rules
        '''
        k_new_piece: Piece = King(pos_X, pos_Y, self.side)
        k_new_board_pieces = copy.deepcopy(B[1])
        k_cap_piece = piece_at(pos_X, pos_Y, B)
        k_new_board: Board = (B[0], k_new_board_pieces)

        # moves the piece in question and removes a captured piece and returns a new board.
        if self.can_move_to(pos_X, pos_Y, B):
            for i in k_new_board_pieces:
                if type(i) == type(self) and i.pos_X == self.pos_X and i.pos_Y == self.pos_Y and i.side == self.side:
                    k_new_board_pieces.remove(i)
                if k_cap_piece:
                    if type(i) == type(k_cap_piece) and i.pos_X == k_cap_piece.pos_X and i.pos_Y == k_cap_piece.pos_Y and i.side == k_cap_piece.side:
                        k_new_board_pieces.remove(i)

            k_new_board_pieces.append(k_new_piece)

        return k_new_board


def is_check(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is check for side
    Hint: use can_reach
    '''

    king_x: int = 0
    king_y: int = 0

    # create a temporary copy to use to beck for check.
    check_temp_board: Board = copy.deepcopy(B[1])

    # get coordinates of the king for the side in question
    for i in check_temp_board:
        if type(i) == King and i.side == side:
            king_x = i.pos_X
            king_y = i.pos_Y

    # checks if any opposition pieces can reach the square that the king is on and returns true to confirm check
    oppo_pieces: List[Piece] = []
    for j in check_temp_board:
        if j.side != side:
            oppo_pieces.append(j)
    for k in oppo_pieces:
        if k.can_reach(king_x, king_y, B):
            return True
    return False


def is_checkmate(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is checkmate for side

    Hints:
    - use is_check
    - use can_reach - NOTE: THIS HINT IS WRONG IT SHOULD BE USE "can_move_to" as that checks if move results in check.
    '''

    # need to see if the side has check and if so then to see if the King can move to any squarea
    if is_check(side, B):
        temp_list: Board = copy.deepcopy(B[1])

        # find the king and create the King piece to use to see if it can move to another square
        for i in temp_list:
            if type(i) == King and i.side == side:
                king: Piece = type(i)(i.pos_X, i.pos_Y, side)
        for j in range(1, B[0] + 1):
            for k in range(1, B[0] + 1):
                if king.can_move_to(j, k, B):
                    return False
        return True
    else:
        return False

def is_stalemate(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is stalemate for side

    Hints:
    - use is_check
    - use can_move_to
    '''

    size: int = B[0]
    pieces: List[Piece] = B[1]

    # checks if not check whether the side in question has any pieces that can move to any square
    if not is_check(side, B):
        for p in pieces:
            if p.side == side:
                for i in range(1, size+1):
                    for j in range(1, size+1):
                        if p.can_move_to(i, j, B):
                            return False

    return True


def read_board(filename: str) -> Board:
    '''
    reads board configuration from file in current directory in plain format
    raises IOError exception if file is not valid (see section Plain board configurations)
    '''
    board_play: Board = tuple()
    board: List[str] = []
    infile = open(filename, "r")
    line = infile.readline()
    line_count: int = 0
    while line != "":
        line_count += 1
        board.append(line.rstrip())
        line = infile.readline()

    if line_count > 3:
        print(bold_start + "WARNING: " + bold_end + "input file has too many lines, only the board size and white and black pieces have been processed.")

    # creates an list of list that has all the pieces from the input file in their own list
    board_arr = [int(board[0]), board[1].split(","), board[2].split(",")]
    board_play += (board_arr[0],)
    pieces_arr: List[Piece] = []

    # loop through the list of pieces and convert from "a1" format to "xy" format and create new pieces for each side
    for i in range(1, 3):

        # creates peices for white
        if i == 1:
            for j in range(0, len(board_arr[i])):
                board_arr[i][j] = board_arr[i][j].strip()
                xy_loc = location2index(board_arr[i][j][1:])
                if board_arr[i][j][0] == "B":
                    pieces_arr.append(Bishop(xy_loc[0], xy_loc[1], True))
                if board_arr[i][j][0] == "R":
                    pieces_arr.append(Rook(xy_loc[0], xy_loc[1], True))
                if board_arr[i][j][0] == "K":
                    pieces_arr.append(King(xy_loc[0], xy_loc[1], True))

        # creates pieces for black
        if i == 2:
            for j in range(0, len(board_arr[i])):
                board_arr[i][j] = board_arr[i][j].strip()
                xy_loc = location2index(board_arr[i][j][1:])
                if board_arr[i][j][0] == "B":
                    pieces_arr.append(Bishop(xy_loc[0], xy_loc[1], False))
                if board_arr[i][j][0] == "R":
                    pieces_arr.append(Rook(xy_loc[0], xy_loc[1], False))
                if board_arr[i][j][0] == "K":
                    pieces_arr.append(King(xy_loc[0], xy_loc[1], False))
            board_play += (pieces_arr,)

    return board_play


def save_board(filename: str, B: Board) -> None:
    '''saves board configuration into file in current directory in plain format'''
    file = open(filename,"w")
    file.write(str(B[0]) + "\n")
    file_line_1: str = ""

    # loops through the board input and converts from Piece format to input file "a1" format
    for i in range(1, len(B)):
        for j in range(0, len(B[1])):

            # converts white pieces
            if B[i][j].side == True:
                if type(B[i][j]) == Rook:
                    file_line_1 += "R" + index2location(B[i][j].pos_X, B[i][j].pos_Y) + ", "
                if type(B[i][j]) == King:
                    file_line_1 += "K" + index2location(B[i][j].pos_X, B[i][j].pos_Y) + ", "
                if type(B[i][j]) == Bishop:
                    file_line_1 += "B" + index2location(B[i][j].pos_X, B[i][j].pos_Y) + ", "
        file.write(file_line_1[:-2])
        file.write("\n")
    file_line_2: str = ""
    for i in range(1, len(B)):
        for j in range(0, len(B[1])):
            # converts black pieces
            if B[i][j].side == False:
                if type(B[i][j]) == Rook:
                    file_line_2 += "R" + index2location(B[i][j].pos_X, B[i][j].pos_Y) + ", "
                if type(B[i][j]) == King:
                    file_line_2 += "K" + index2location(B[i][j].pos_X, B[i][j].pos_Y) + ", "
                if type(B[i][j]) == Bishop:
                    file_line_2 += "B" + index2location(B[i][j].pos_X, B[i][j].pos_Y) + ", "
        file.write(file_line_2[:-2])
    file.close()

def find_black_move(B: Board) -> Tuple[Piece, int, int]:
    '''
    returns (P, x, y) where a Black piece P can move on B to coordinates x,y according to chess rules
    assumes there is at least one black piece that can move somewhere

    Hints:
    - use methods of random library
    - use can_move_to
    '''
    size: int = B[0]

    # Obtain a list of all black pieces on the board to select from for the move.
    black_pieces: List[Piece] = []
    for i in B[1]:
        if not i.side:
            black_pieces.append(i)

    ''' generate a random black piece and random coords and test to see if a valid move.
    If valid create return the resulting piece'''
    while True:
        black_move_x: int = random.randint(1, size)
        black_move_y: int = random.randint(1, size)
        piece_to_move = random.choice(black_pieces)
        if piece_to_move.can_move_to(black_move_x, black_move_y, B):
            return (piece_to_move, black_move_x, black_move_y)
        else:
            True

def conf2unicode(B: Board) -> str:
    '''converts board cofiguration B to unicode format string (see section Unicode board configurations)'''
    size: int = B[0]
    board_matrix: List[List] = []

    # create a matrix with spaces \u2001 for the pieces to go on
    for i in range(0, size):
        board_matrix.append([])
        for j in range(0, size):
            board_matrix[i].append("\u2001")

    # populate the matrix with the pieces.  Bear in matrix starts at 0, hence pos_X-1  and pos_Y-1. Return as a string
    for i in range(1, len(B)):
        for j in range(0, len(B[i])):
            X = B[i][j].pos_X-1
            Y = B[i][j].pos_Y-1
            if type(B[i][j]) == Bishop and B[i][j].side == True:
                board_matrix[Y][X] = "\u2657"
            if type(B[i][j]) == Rook and B[i][j].side == True:
                board_matrix[Y][X] = "\u2656"
            if type(B[i][j]) == King and B[i][j].side == True:
                board_matrix[Y][X] = "\u2654"
            if type(B[i][j]) == Bishop and B[i][j].side == False:
                board_matrix[Y][X] = "\u265D"
            if type(B[i][j]) == Rook and B[i][j].side == False:
                board_matrix[Y][X] = "\u265C"
            if type(B[i][j]) == King and B[i][j].side == False:
                board_matrix[Y][X] = "\u265A"
    board_string: str = ""

    # print the board.  Note to print from bottom left need to reverse through the matrix which starts top right.
    for i in range(len(board_matrix)-1, -1, -1):
        for j in range(0, len(board_matrix[i])):
            board_string += board_matrix[i][j]
        if i > 0:
            board_string += "\n"
    print(board_string)
    return board_string


def main() -> None:
    '''
    runs the play

    Hint: implementation of this could start as follows:
    filename = input("File name for initial configuration: ")
    '''
    filename: str = input(bold_start + "File name for " + bold_end + "initial configuration: ")
    run: bool = True
    # First while loop checks the file is present in the directory and if so creates board to play on.
    while run == True:
        try:
            open(filename, "r")
        except IOError:
            filename = input(
                "This " + bold_start + "is not " + bold_end + "a valid " + bold_start + "file. File name for " + bold_end + "initial configuration: ")
        else:
            board_in_play: Board = copy.deepcopy(read_board(filename))
            print("The initial " + bold_start + "configuration is: " + bold_end)
            conf2unicode(board_in_play)
            run = False
    # main game loop, starts with white move or saving file if quit is entered.
    while True:
        white_move = input("Next " + blue_text + "move " + blue_text_end + "of White: ")

        if white_move.strip().lower() == "quit":
            filename_store = input(bold_start + "File name to " + bold_end + "store the configuration: ")
            save_board(filename_store, board_in_play)
            print("The game configuration saved.")
            return False

        # creates white piece to move and checks that the move is valid and creates new board it it is.
        str_len_half = int(len(white_move) / 2)
        white_x_loc = white_move[:str_len_half]
        white_y_loc = white_move[str_len_half:]
        white_piece_move_from: Tuple[int, int] = location2index(white_x_loc)
        white_piece_move_to: Tuple[int, int] = location2index(white_y_loc)
        white_to_X: int = white_piece_move_to[0]
        white_to_Y: int = white_piece_move_to[1]
        white_piece: Piece = piece_at(white_piece_move_from[0], white_piece_move_from[1], board_in_play)
        white_input: bool = True
        while white_input:
            if not white_piece:
                white_move = input(
                    "This " + bold_start + "is not " + bold_end + "a valid move. " + bold_start + "Next " + bold_end + "move " + bold_start + "of " + bold_end + "White: ")
                if white_move.strip().lower() == "quit":
                    filename_store = input(bold_start + "File name to " + bold_end + "store the configuration: ")
                    save_board(filename_store, board_in_play)
                    print("The game configuration saved.")
                    return False
                white_piece_move_from: Tuple(int) = location2index(white_move[:2])
                white_piece_move_to: Tuple(int) = location2index(white_move[2:])
                white_to_X: int = white_piece_move_to[0]
                white_to_Y: int = white_piece_move_to[1]
                white_piece: Piece = piece_at(white_piece_move_from[0], white_piece_move_from[1], board_in_play)
            if not white_piece.can_move_to(white_to_X, white_to_Y, board_in_play) or not piece_at(
                white_piece_move_from[0], white_piece_move_from[1], board_in_play):
                white_move = input("This " + bold_start + "is not " + bold_end + "a valid move. " + bold_start + "Next " + bold_end + "move " + bold_start + "of " + bold_end + "White: ")
                if white_move.strip().lower() == "quit":
                    filename_store = input(bold_start + "File name to " + bold_end + "store the configuration: ")
                    save_board(filename_store, board_in_play)
                    print("The game configuration saved.")
                    return False
                white_piece_move_from: Tuple(int) = location2index(white_move[:2])
                white_piece_move_to: Tuple(int) = location2index(white_move[2:])
                white_to_X: int = white_piece_move_to[0]
                white_to_Y: int = white_piece_move_to[1]
                white_piece: Piece = piece_at(white_piece_move_from[0], white_piece_move_from[1], board_in_play)
            else:
                white_input = False

        if white_piece.can_move_to(white_to_X, white_to_Y, board_in_play):
            board_in_play = white_piece.move_to(white_to_X, white_to_Y, board_in_play)
            print("The " + bold_start + "configuration after " + bold_end + "White's move is: ")
            conf2unicode(board_in_play)


        if is_checkmate(False, board_in_play):
            print("Game " + bold_start + "over. " + bold_end + "White wins.")
            return False

        if is_stalemate(True, board_in_play):
            print("Game " + bold_start + "over. " + bold_end +  "Draw")
            return False

        # creates black move and creates new board if valid
        black_piece_move = find_black_move(board_in_play)
        black_to_move: Piece = black_piece_move[0]
        black_X: int = black_piece_move[1]
        black_Y: int = black_piece_move[2]
        black_to_move.move_to(black_X, black_Y, board_in_play)
        black_orig_loc: str = index2location(black_to_move.pos_X, black_to_move.pos_Y)
        black_loc: str = index2location(black_X, black_Y)
        print(bold_start + "Next " + bold_end + "move " + bold_start + "of " + bold_end + "Black " + bold_start + "is " + bold_end + f"{black_orig_loc + black_loc}. The " + bold_start + "configuration after " + bold_end + "Black's move " + bold_start + "is:" + bold_end)
        board_in_play = black_to_move.move_to(black_X, black_Y, board_in_play)
        conf2unicode(board_in_play)


        if is_checkmate(True, board_in_play):
            print("Game " + bold_start + "over. " + bold_end + "Black wins.")
            return False

        if is_stalemate(False, board_in_play):
            print("Game " + bold_start + "over. " + bold_end +  "Draw")
            return False

if __name__ == '__main__':  # keep this in
    main()


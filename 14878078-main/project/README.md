Reduced Chess
    #### Video Demo:  https://youtu.be/AhUccLM5rDI
    #### Description:
    Reduced version of chess played from the command line


Only the bishop, king and rook pieces will be involved in play. The game will be played between Black and White, as usual. However, the board size will be S x S, where S is a number between 2 and 26, instead of the usual 8 x 8. (We only set the limit 26 to avoid visualisation/printing problems for large boards and denotation.) Also, rather unusually, each side (Black or White) may play with any number, including 0, of the allowed pieces in any positions, as long as they fit the board. E.g., there can be 5 black rooks and 15 white bishops on the board in a play. But, each side has exactly one king, as usual in chess.

White starts the game, after which Black and White alternate by moving one of own pieces according to the usual chess rules, that are:

[Rule1] A bishop can move any number (1 or more) of squares diagonally, but cannot leap over other pieces.
[Rule2] A rook can move any number of squares along a row (also called rank in chess terminology) or column (also called file), but cannot leap over other pieces. Also, we disallow castling to simplify the coursework.
[Rule3] The king moves one square in any direction, including diagonal, on the board.
As usual, as a result of any move, the piece that is moved either occupies a previously empty board location, or captures the other side's piece. In that case, the former piece occupies the latter's position, while the latter piece is removed from the board. Clearly, we have the following:

[Rule4] A piece of side X (Black or White) cannot move to a location occupied by a piece of side X.
Check for side X is a configuration of the board when X's king can be captured by a piece of the other side Y (in one move). Another chess rule we obey is:

[Rule5] A piece of side X cannot make a move, if the configuration resulting from this move is a check for X.
Checkmate for side X is a configuration of the board when the king of a side X (Black or White) is in check and there is no move available for X to eliminate the check situation.

Stalemate for side X is a configuration of the board when the side X is not in check and there is no move available for X.

Every game results in a win of side X, or a draw, or it runs infinitely. Side X wins if the game reaches a configuration which is a checkmate for the opposite side. Draw occurs if the game reaches a configuration which is a stalemate for either Black or White.

Notation and Symbols
The columns will be designated by small letter characters from a to z and the rows by numbers from 1 to 26. The leftmost column is a and the bottom row is 1.

Board configurations
We will need plain board configurations that are stored in files (on the PC) and unicode board configurations that are printed on the screen.

Plain board configurations
Each plain board configuration is determined by a sequence of of piece locations, where a piece location is a string of the form Xcr and X is either equal

to K, to indicate king, or
to R to indicate rook, or
to B to indicate bishop,
and cr indicates the column and row of a location of the piece. E.g., Be14 says that there is a bishop in column e and row 14.

Now, to store a configuration of the whole board in a file, we will use the following format:

the first line of the file contains a single number representing the size of the board S
the second line of the file contains piece locations of White pieces separated by ,
the third line of the file contains piece locations of Black pieces separated by ,
the last , on either line can be omitted and there may be arbitrarily many spaces before and after any ,
See the file board_examp.txt for an example. A file is valid if it is syntactically correct as specified above, the configuration encoded in it has exactly one king for White and exactly one king for Black, there are no different pieces in the same location, and each location is within the S x S square.

Unicode board configurations
To designate the pieces, we will use the chess unicode characters:

piece	character	escape sequence
white king	♔	\u2654
white rook	♖	\u2656
white bishop	♗	\u2657
black king	♚	\u265A
black rook	♜	\u265C
black bishop	♝	\u265D
space of matching width	 	\u2001
Note In Python code, you can use the characters "directly" by copy/pasting from the table above (except the space), or by the escape sequence. E.g.,

print("♔")
or

print("\u2654")
will print ♔ and

"♔"=="\u2654"
will print True.

When outputting the configuration of an S x S board on the screen, we will use the format, where the output has S lines and each line is a string of the form ln[0] ln[1] ... ln[S-1] representing the correspoinding row. So, each ln[i] is either one of ♔, ♖, ♗, ♚, ♜, ♝, or the space of the matching width (\u2001). For example, the plain boad configuration stored in the file board_examp.txt corresponds to the following unicode board configuration:

♖ ♔  
 ♜  ♜
 ♚ ♜ 
♖   ♗
♗    
Moves
It will be needed to specify moves of pieces. To indicate the moves, we will use the strings of the form crCR, where cr indicates the column and row of the origin of the move, and CR indicates the row and column of the destination of the move. For example, a1b2 says that the piece located in the column a and row 1 moves to the column b and row 2. Note that the string crCR can have length between 4 and 6.

Requirements
Note: the requirements below are mandatory to follow. You will lose marks if your implementation does not meet these requirements

In this coursework, you will implement a Python program, in which a human user will play the specific version of chess described above against the computer. The human always plays with White and computer always plays with Black.

Initiation
When the program is executed, it first promts the user to provide a file name that stores a plain board configuration:

File name for initial configuration:
The user inputs the file name or types QUIT to terminate the program. If this file is not valid (see Plain board configurations), the program states that and prompts to provide a file name again:

This is not a valid file. File name for initial configuration:
The user inputs the file name or types QUIT to terminate the program. This continues until the user provides a valid file or terminates the program. If a valid file is provided, the plain board configuration it contains, becomes the initial configuration of the play. This configuration is printed on the screen in unicode format. For example,

The initial configuration is:
♖ ♔  
 ♜  ♜
 ♚ ♜ 
♖   ♗
♗    
Play rounds
Each round is a move of White followed by a move of Black. In each round, the program prints:

Next move of White:
The user can indicate a move in the format described above (see Moves), e.g.

Next move of White: a1b2
Instead of making a move, White can print QUIT to indicate that they want to stop the game and save the current configuration in a file. If the user prints QUIT, the program prompts the user to provide a name of the file to store the current configuration:

File name to store the configuration:
After specifying the file name, the program saves the current configuration in the plain format. The program prints the confirmation:

The game configuration saved.
and terminates.

If the user inputed a move, the program checks if this move is valid chess move (see Intro). If this is not the case, the program prompts the user to provide another input:

This is not a valid move. Next move of White:
This continues until the user inputs a valid chess move or QUIT to save the configuration and terminate the program. When a valid chess move is inputed, the program prints the next configuration of the game (after White's move), e.g.,

The configuration after White's move is:
♖ ♔  
 ♜  ♜
 ♚ ♜ 
♖♗  ♗
     
Now, the current configuration may be a checkmate or stalemate for Black (or none of those). If it is a checkmate the program prints:

Game over. White wins.
and terminates. If it is a stalemate, the program prints:

Game over. Draw.
and terminates. Otherwise, the program computes the next valid move for Black, using any method you like, prints the move and the configuration after this move, e.g.:

Next move of Black is e3c3. The configuration after Black's move is:
♖ ♔  
 ♜♜  
 ♚ ♜ 
♖♗  ♗
     
The current configuration may be a checkmate or stalemate for White (or none of those). If it is a checkmate the program prints:

Game over. Black wins.
and terminates. If it is a stalemate, the program prints:

Game over. Draw.
and terminates. Otherwise, a new round of the game occurs.
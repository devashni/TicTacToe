# Function to build ROWS for a visual square matrix board for Tic-Tac-Toe
def print_row(matrix_row):
    new_row = ""
    # The element in a matrix_row can be a mark type or a space
    for element in matrix_row:
        new_row  += " " + element + " " + "|" 
    return new_row[:-1]

# Function to print cell/column index at TOP of the matrix
def print_cloumn_index(matrix):
    # Start with 2 spaces - because the rows below, will use an extra space on the left for the
    # row index, and another space after that as a seperator
    new_index_row = " " + " "
    for i in range (0, len(matrix)):
        new_index_row += " " + str(i) + " " + " "
    return new_index_row

# Printing a FULL visual square matrix board for Tic Tac Toe with cell indexes
def print_board(matrix):
    print (print_cloumn_index(matrix))
    for i in range (0, len(matrix)):
        # This prints the row indexes + space + the rest of the row
        print (str(i) + " " + print_row(matrix[i]))
        # This prints a line made of dashes and plus after each row, minus the last
        if i < len(matrix)-1: 
            print ("  ---+---+---")

# Checking if the input coordinates for the move is within bounds for nxn matrix defined here
def is_within_bounds(lst_coordinates, matrix):
    matrix_size = len(matrix)
    if (lst_coordinates[0] >= 0 and lst_coordinates[0] < matrix_size)and(lst_coordinates[1] >= 0 and lst_coordinates[1] < matrix_size):
        return True
    return False

# Getting Player's move. Return will be "Row,Column" format as input by user
def get_player_move(player_name,matrix):
    while True:
        move = input(player_name + " Enter your move. Provide Row,Column. Enter -1,-1 to exit, when done: ")
        moves = move.split(",")
        moves_rows_and_columns_lst = [int(moves[0]), int(moves[1])]
      
        if moves_rows_and_columns_lst == [-1,-1]:
            return moves_rows_and_columns_lst
        elif matrix[int(moves[0])][int(moves[1])] != " ":
            print ("These coordinates are taken. Enter a valid input.")
            continue
        elif not is_within_bounds(moves_rows_and_columns_lst, matrix):
            print ("This input is invalid.")
        else:
            return moves_rows_and_columns_lst


# This function does the following: 
# 1. Gets player's move.
# 2. Records all valid moves on matrix board, and returns True.
# 3.If player wants to exit and enters [-1,-1], it returns False
def perform_player_move_and_return_result(matrix, player_name, mark_type):
      player_moves = get_player_move(player_name, matrix)
      
      # Checking if player wants to EXIT game
      if player_moves == [-1,-1]: 
          return False
     # Placing player mark "o" or "x" at the matrix postion provided by the player above
      matrix[player_moves[0]][player_moves[1]] = mark_type
      return True

# Checking each matrix row for win based on mark type "x" or "o"
def check_row_for_win(given_row, mark_type):
    counter = 0
    for x in given_row:
        if x == mark_type:
            counter += 1
    if counter == 3: # 3 = square_matrix_size (make this a user input variable)
        return True
    return False

# Checking each matrix column for win based on mark type "x" or "o"
def check_col_for_win(matrix, col_num, mark_type):
    for i in range (0, len(matrix)):
        if matrix[i][col_num] != mark_type:
            return False
    return True

# Checking matrix diagonal (top-left to bottom-right) for win based on mark type "x" or "o"
def check_diagonal_top_left_to_bottom_right_for_win(matrix, mark_type):
    for i in range (0, len(matrix)):
        # top-left to bottom-right matrix diagonal cell pattern: [0,0], [1,1],[2,2]...[n,n]
        if matrix[i][i] != mark_type:
            return False
    return True

# Tricky one: Checking matrix diagonal (top-right to bottom-left) for win based on mark type "x" or "o"
def check_diagonal_top_right_to_bottom_left_for_win(matrix, mark_type):
    col_num = len(matrix)-1
    for i in range (0, len(matrix)):
        # top-right to bottom-left 4X4 matrix diagonal cell pattern: 
        # Identifying pattern: [0,3],[1,2],[2,1],[3,0] == [0,len-1],[0+1,len-1-1],[0+1+1,len-1-1-1],[0+1+1+1,len-1-1-1-1]
        # this means 'rows' can be i
        if matrix[i][col_num] != mark_type:
            col_num = col_num - 1
            return False
    return True

# Checking the FULL Tic-Tac-Toe matrix board for win
def check_board_for_win(matrix, mark_type):

    # Check Rows for win
    for single_row in matrix:
        #check_row_for_win function below checks a single row at a time, hence loop above
        if check_row_for_win(single_row, mark_type) == True: 
            return True
    
    # Check Columns for win 
    for i in range (0, len(matrix)):
        # square matrix -> num of rows = num of columns; hence i = column number
        if check_col_for_win(matrix, i , mark_type) == True:
            return True

    # Check diagonal (top-left to bottom-right) for win
    if check_diagonal_top_left_to_bottom_right_for_win(matrix, mark_type) == True: 
            return True

    # Check diagonal (top-right to bottom-left) for win
    if check_diagonal_top_right_to_bottom_left_for_win(matrix, mark_type) == True: 
            return True

    # No win found, return false
    return False


# This is the main program, calling all functions and playing the game. This whole program plays
# the game by asking each player for their move in "Row,Column" format, printing the updated
# Matrix board, checking for exit conditons and if a player has won
matrix = [  [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]

print("Let's play Tic Tac Toe!")

total_played_moves = 0
# Keep looping forever. Only "break" if any player gives [-1,-1] as input or all moves are played.
while True:
    # Placing player mark "" at the matrix postion provided above by the player and printing current board
    if perform_player_move_and_return_result(matrix, "Player O", "o") == False:
        break

    print_board(matrix)
    if check_board_for_win(matrix, "o") == True:
        print ("Congratulations!! Player O has won this game.")
        break
    total_played_moves += 1
    if (total_played_moves > 8):
        print("No more moves left. This game is a draw.")
        break

    # Placing player mark "x" at the matrix postion provided above by the player and printing current board
    if perform_player_move_and_return_result(matrix, "Player X", "x") == False:
        break
    print_board(matrix)

    if check_board_for_win(matrix, "x") == True:
        print ("Congratulations!! Player x has won this game.")
        break
    total_played_moves += 1
    if (total_played_moves > 8):
        print("No more moves left. This game is a draw.")
        break

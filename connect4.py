import random
import os

def clear_screen():
	"""
	Clears the terminal for Windows and Linux/MacOS.

	:return: None
	"""
	os.system('cls' if os.name == 'nt' else 'clear')

def print_rules():
	"""
	Prints the rules of the game.

	:return: None
	"""
	print("================= Rules =================")
	print("Connect 4 is a two-player game where the")
	print("objective is to get four of your pieces")
	print("in a row either horizontally, vertically")
	print("or diagonally. The game is played on a")
	print("6x7 grid. The first player to get four")
	print("pieces in a row wins the game. If the")
	print("grid is filled and no player has won,")
	print("the game is a draw.")
	print("=========================================")

def validate_input(prompt, valid_inputs):
	"""
	Repeatedly ask user for input until they enter an input
	within a set valid of options.

	:param prompt: The prompt to display to the user, string.
	:param valid_inputs: The range of values to accept, list
	:return: The user's input, string.
	"""
	while True:
		# Keeps prompting user for a input in the restriction of valid_input.
		user_input = input(prompt)

		if user_input in valid_inputs:
			# Return the input if valid.

			return user_input
		
		# Print statement and restart the loop if invalid.
		else:
			print("Invalid input, please try again.")

		# 'user_input' is returned.

def create_board():
	"""
	Returns a 2D list of 6 rows and 7 columns to represent
	the game board. Default cell value is 0.

	:return: A 2D list of 6x7 dimensions.
	"""
	board = []
	# Setting row and column as variables so it's easier to change.
	row = 6
	column = 7

	for i in range(row):
		# Create a row with column(7) * [0], append to board.
		'''
		[[0, 0, 0, 0, 0, 0, 0]]
		'''

		board.append([0] * column)
		# Iterate this row(6) times.

		'''
		[[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0]]
		'''

	return board

	# 'board' is returned.

def print_board(board):
	"""
	Prints the game board to the console.

	:param board: The game board, 2D list of 6x7 dimensions.
	:return: None
	"""
	# Takes board as input from create_board.
	# Storing length of row and column into variables 'rows' and 'columns'.
	rows = len(board)
	columns = len(board[0])

	# The first three rows can be printed just by using print function.
	print('========== Connect4 =========')
	print('Player 1: X       Player 2: O\n')
	print('  1   2   3   4   5   6   7')

	# Creating the cells 
	for i in range(rows):
		# Prints '---' corresponding to the number of columns.
		print(' ---' * columns)

		for j in range(columns):
			# For every empty cell denoted [0], print '|   ', keep on the same row. 
			if board[i][j] == 0:
				print('|   ', end='')

			# For every player 1's input, print '| X ', this looks like:
			# |   | X |...
			elif board[i][j] == 1:
				print('| X ', end='')

			# For every player 2's input, print '| O ', this looks like:
			# |   | X | O |...
			elif board[i][j] == 2:
				print('| O ', end='')

		# Finish the row with |
		print('|')

	# Iterate this process row(6) times

	# The finishing lines
	print(' ---' * columns)
	print('=============================')

	# Nothing is returned. 

def drop_piece(board, player, column):
	"""
	Drops a piece into the game board in the given column.
	Please note that this function expects the column index
	to start at 1.

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player who is dropping the piece, int.
	:param column: The index of column to drop the piece into, int.
	:return: True if piece was successfully dropped, False if not.
	"""
	# Takes board, player, column as input.
	# len(board) - 1 gives 5 if there are 6 rows, as row counting starts from 0. 
	i = len(board) - 1
	
	# Iterate through each row to see if the slot is 0, if yes, replace with 'player' and return True
	while i >= 0:

		# column - 1 because counting starts from 0.
		# Starts with board[5][6], the bottom most cell in the column, which was input by user.
		if board[i][column - 1] == 0:
			board[i][column - 1] = player

			# Return true after making a change.
			return True
		else:
			i -= 1

	return False

	# True or False is returned. 

def execute_player_turn(player, board):
	"""
	Prompts user for a legal move given the current game board
	and executes the move.

	:return: Column that the piece was dropped into, int.
	"""
	while True:
		# Prompt player for input in integer.
		column = int(input(f'Player {player}, please enter the column you would like to drop your piece into: '))

		# Check if column input is valid.
		if str(column) in ["1", "2", "3", "4", "5", "6", "7"]:
			if drop_piece(board, player, column):
				# If drop_piece function returns True (Meaning dropping is valid), return column.
				return column

			# If drop_piece returns False, column is full.
			else:
				print("That column is full, please try again.")

		# Else, input is not in 'valid_input', print invalid input. 
		else:
			print("Invalid input, please try again.")

		# 'column' is returned.

def end_of_game(board):
	"""
	Checks if the game has ended with a winner
	or a draw.

	:param board: The game board, 2D list of 6 rows x 7 columns.
	:return: 0 if game is not over, 1 if player 1 wins, 2 if player 2 wins, 3 if draw.
	"""
	# Storing number of rows and columns into variables
	rows = len(board)
	columns = len(board[0])

	# If the piece dropped makes a connected 4 with 3 consecutive identical pieces, return the piece (1/2)
	# If there is 0 on the board, return 0 (Game continuing)
	# Else, game must be draw, return 3

	# Check for 4 of the same digit in a column
	for i in range(rows - 3):
		# Can check a maximum of 3 times
		for j in range(columns):
			if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] != 0:
				return board[i][j]

	# Check for 4 of the same digit in a row
	for i in range(rows):
		# Can check a maximum of 4 times
		for j in range(columns - 3):
			if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] != 0:
				return board[i][j]
		
	# Check for 4 of the same digit backward leaning
	for i in range(rows - 3):
		# Vertical max for connected 4 is 3
		for j in range(columns - 3):
			# Horizontal max for connected 4 is 4
			if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] != 0:
				return board[i][j]
	
	# Check for 4 of the same digit forward leaning
	for i in range(rows - 3):
		# 4 connected cells is only possible from the 4th to 7th column
		for j in range(3, columns):
			if board[i][j] == board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3] != 0:
				return board[i][j]

	# If there's a [0] on the board, game is still going, return 0
	for i in range(rows):
		for j in range(columns):
			if board[i][j] == 0:
				return 0
				
	# If no 4 in a row, or no [0] on the board (full board), return 3
	return 3

	# 0, 1, 2 or 3 are returned. 

def local_2_player_game():
	"""
	Runs a local 2 player game of Connect 4.

	:return: None
	"""
	# Creating the board everytime, this step is fixed.
	clear_screen()
	board = create_board()
	print_board(board)

	# This loop prompts user 1 and 2 for moves, until win, lose or draw is decided.
	# The 'stop' variable is used to terminate the outer loop.
	stop = 0
	while stop < 1:
		for i in range(1, 3):
			# Prompt player 1 or 2 for a move.
			column = execute_player_turn(i, board)

			# Clear the screen and print the board
			clear_screen()
			print_board(board)

			# Prints a statement of move just made
			print(f'Player {i} dropped a piece into column {column}')

			# Check for win, loss, or draw 
			result = end_of_game(board)
			if result == 1 or result == 2:
				print(f'Player {result} has won!')
				# Break the loop if result is determined. 
				stop = 2
				break
			elif result == 3:
				print(f'This game is a draw!')
				stop = 2
				break

			# Nothing is returned

def main():
	"""
	Defines the main application loop.
    User chooses a type of game to play or to exit.

	:return: None
	"""
	# Print the menu
	print('=============== Main Menu ===============')
	print('Welcome to Connect 4!')
	print('1. View Rules')
	print('2. Play a local 2 player game')
	print('3. Play a game against the computer')
	print('4. Exit')
	print('=========================================')

	# Prompting user for an option from (1/2/3/4)
	option = input('Please select an option (1/2/3/4): ')

	# Direct user to the page for rules using print_rules function.
	if option == '1':
		clear_screen()
		print_rules()
		# Asking user if they want to return to main menu
		return1 = input('Press 1 to return: ')
		if return1 == '1':
			clear_screen()
			main()
		else:
			# Unexpected input will result in exit
			return 1
	
	# If option two is selected, direct user to local_2_player_game function.
	elif option == '2':
		clear_screen()
		local_2_player_game()
		# Asking user if they want to return to main menu
		return1 = input('Press 1 to return: ')
		if return1 == '1':
			clear_screen()
			main()
		else:
			# Unexpected input will result in exit
			return 1

	# Option 3 wll direct user to game_against_cpu function.
	elif option == '3':
		clear_screen()
		game_against_cpu()

	# Option 4 will result in the termination of the program. 
	elif option == '4':
		return 1
	
	# 1 is returned if input is invalid.

def cpu_player_easy(board, player):
	"""
	Executes a move for the CPU on easy difficulty. This function 
	plays a randomly selected column.

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player whose turn it is, integer value of 1 or 2.
	:return: Column that the piece was dropped into, int.
	"""
	while True:
		# Setting a random integer from 1 to 7 (inclusive) to the variable column.
		column = random.randint(1, 7)

		# drop_piece drops the piece and returns True if dropping is valid.
		if drop_piece(board, player, column):
			return column
		
		# column is returned.

# Analyse Medium (Helper Function 1)
def analyse_medium(board, player): 
	'''
	This function is a helper function designed to find the best move for the medium cpu.
	It takes board and player as inputs, check if the piece dropped will a form a connected 4
	with 3 other consecutive pieces. 
	Returns: True is connected 4 will form.
	'''
	# Storing length of row and column into variables. 
	rows = len(board)
	columns = len(board[0])
	
	# Check for vertical 4 digit wins
	for i in range(rows - 3):
		for j in range(columns):
			# If three consecutive digits, and board[i][j], form a connected 4, return true. 
			if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] == player:
				return True

	# Check for horizontal 4 digit wins
	for i in range(rows):
		for j in range(columns - 3):
			# If three consecutive digits, and board[i][j], form a connected 4, return true. 
			if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == player:
				return True

	# Check for backward leaning 4 digit wins
	for i in range(rows - 3):
		for j in range(columns - 3):
			# If three consecutive digits, and board[i][j], form a connected 4, return true. 
			if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == player:
				return True

	# Check for forward leaning 4 digit wins
	for i in range(rows - 3):
		for j in range(3, columns):
			# If three consecutive digits, and board[i][j], form a connected 4, return true. 
			if board[i][j] == board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3] == player:
				return True

	return False

	# True is returned if a connected 4 will form.

def cpu_player_medium(board, player):
	"""
	Executes a move for the CPU on medium difficulty. 
	It first checks for an immediate win and plays that move if possible. 
	If no immediate win is possible, it checks for an immediate win 
	for the opponent and blocks that move. If neither of these are 
	possible, it plays a random move.

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player whose turn it is, integer value of 1 or 2.
	:return: Column that the piece was dropped into, int.
	"""
	# 4 steps involved.
	# Check if only one column left > Check for winning moves > Check for defending moves > Random move

	# Storing the number of rows and columns into variables 'row' and 'column'.
	row = len(board)
	column = len(board[0])

	# 1. Check if only one column left
	# 'count' counts the numebr of columns that is invalid to drop. 
	count = 0

	# Iterate through each column.
	for i in range(1, column + 1):

		# For every row in board, replicate it using slice.
		# ie. board[0] = [0, 0, 0, 0, 0, 0, 0]
		# Replicate a temporary board so drop_piece doesn't change the board.

		temp = [row[:] for row in board]

		# Everytime drop_piece returns False, the column is full.
		if drop_piece(temp, player, i) == False:
			count += 1

	# When count is 1 less than the number of columns, only one column is not full.
	if count == column - 1:
		# Iterate through each column again and return the valid column.
		for i in range(1, column + 1):
			if drop_piece(board, player, i):
				return i

	# 2. Check for winning moves
	for i in range(1, column + 1):

		# Create a new board with the same rows.
		temp = [row[:] for row in board]

		# If dropping is valid
		if drop_piece(temp, player, i):

			# If there is a winning move for cpu, play it.
			if analyse_medium(temp, player):
				drop_piece(board, player, i)
				return i

    # 3. Check for blocking moves
	for i in range(1, column + 1):

		# Create a new board with the same rows.
		temp = [row[:] for row in board]

		# If dropping is valid
		if drop_piece(temp, player % 2 + 1, i):

			# If there is a winning move for player, block it.
			if analyse_medium(temp, player % 2 + 1):
				drop_piece(board, player, i)
				return i 

	# 4. If no winning/defending moves, and no single column, return a random column.
	i = random.randint(1, 7)
	if drop_piece(board, player, i):
		return i

# Analyse Three (Helper Function 2, Check for connect 3)
def analyse_three(board, player): 
	'''
	This function analyses the board and finds the move that connects three identical cells in a row.
	Takes board and player as input.
	'''
	# Storing the number of rows and columns into variables 'row' and 'column'.
	rows = len(board)
	columns = len(board[0])
	
	# Check for vertical 3 connected cells
	for i in range(rows - 3):
		for j in range(columns):
			# If two consecutive digits, and board[i][j], form a connected 3, return true. 
			if board[i][j] == board[i+1][j] == board[i+2][j] == player and i > 0:
				return True

	# Check for horizontal 3 connected cells
	for i in range(rows):
		for j in range(columns - 3):
			# If two consecutive digits, and board[i][j], form a connected 3, return true.
			if board[i][j] == board[i][j+1] == board[i][j+2] == player:
				return True

	# Check for backward leaning 3 connected cells
	for i in range(rows - 3):
		for j in range(columns - 3):
			# If two consecutive digits, and board[i][j], form a connected 3, return true.
			if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == player:
				return True

	# Check for forward leaning 3 connected cells
	for i in range(rows - 3):
		for j in range(3, columns):
			# If two consecutive digits, and board[i][j], form a connected 3, return true.
			if board[i][j] == board[i+1][j-1] == board[i+2][j-2] == player:
				return True

	return False

# Analyse Hard (Helper Function 3)
def analyse_hard(board, player):
	'''
	This function check the patterns in 'board' that contains 'player' against 
	the list of patterns provided, prioritises the highest weighing pattern and returns True. 
	'''
	# Storing the number of rows and columns into variables 'row' and 'column'.
	rows = len(board)
	columns = len(board[0])
	
	# Set a weight to every pattern
	weight = {
		(player, player, player, player): 150,
		(player, player, player, 0): 100,
		(0, player, player, player): 100,
		(player, player, 0, player): 50,
		(player, 0, player, player): 50,
		(player, player, 0, 0): 10,
		(player, 0, player, 0): 10,
		(0, player, player, 0): 10,
		(player, 0, 0, player): 10,
		(0, 0, player, player): 10,
	}

	# Check for vertical 4 digit wins
	for i in range(rows - 3):
		for j in range(columns):
			# Stroing the pattern of 'player' into 'key.
			key = (board[i][j], board[i+1][j], board[i+2][j], board[i+3][j])
			# If key is in the list of patterns in 'weight', prioritise the highest weighing pattern and return True. 
			if key in weight:
				if weight[key] > 50:
					return True
				elif key.count(player) == 3:
					if weight[key] > 10:
						return True
					elif key.count(player) == 2:
						return True

	# Repeat for horizontal and diagonal

	# Check for horizontal 4 digit wins
	for i in range(rows):
		for j in range(columns - 3):
			key = (board[i][j], board[i][j+1], board[i][j+2], board[i][j+3])
			if key in weight:
				if weight[key] > 50:
					return True
				elif key.count(player) == 3:
					if weight[key] > 10:
						return True
					elif key.count(player) == 2:
						return True

	# Check for backward leaning 4 digit wins
	for i in range(rows - 3):
		for j in range(columns - 3):
			key =(board[i][j], board[i+1][j+1], board[i+2][j+2], board[i+3][j+3])
			if key in weight:
				if weight[key] > 50:
					return True
				elif key.count(player) == 3:
					if weight[key] > 10:
						return True
					elif key.count(player) == 2:
						return True

	# Check for forward leaning 4 digit wins
	for i in range(rows - 3):
		for j in range(3, columns):
			key = (board[i][j], board[i+1][j-1], board[i+2][j-2], board[i+3][j-3])
			if key in weight:
				if weight[key] > 50:
					return True
				elif key.count(player) == 3:
					if weight[key] > 10:
						return True
					elif key.count(player) == 2:
						return True
					
	# If no patterns are the same, return False	
	return False

	# True returned if pattern is found, False otherwise. 


# Block horizontal (Helper function 4)
def block_horizontal(board):
	'''
	This function checks for patterns like '0011100', as medium cpu
	is unable to detect that pattern as a loss. The medium cpu would
	only block when 3 is connected in a row, for most cases it works,
	however this is an exception. 
	'''
	# Check the bottom row of the board, block the player according to pattern observed.
	weight = {
		(0, 0, 0, 1, 0, 0, 0): 100,
		(0, 0, 1, 0, 0, 0, 0): 80,
		(0, 1, 0, 0, 0, 0, 0): 80,
		(0, 0, 0, 0, 1, 0, 0): 80,
		(0, 0, 0, 0, 0, 1, 0): 80,
		(0, 0, 0, 0, 0, 0, 1): 80,
		(1, 0, 0, 0, 0, 0, 0): 80
	}

	# Block horizontal 4s
	key = (board[5][0], board[5][1], board[5][2], board[5][3], board[5][4], board[5][5], board[5][6])
	if key in weight:
		if weight[key] > 90:
			return 5
		elif weight[key] > 70:
			return 4

	return False

# This makes sure that block_horizontal function only runs once
block_count = 0

def cpu_player_hard(board, player):
	"""
	Executes a move for the CPU on hard difficulty.
	This function creates a copy of the board to simulate moves.
	<First check if there is only one empty column, then check for winning
	moves and blocking moves (this part is the same as analyse_medium), 
	if none of these are possible, the cpu should play according to the 
	weighings set to the key patterns. If not, play a move that connects
	3 pieces in a roll, otherwise, prioritise the piece in the middle (3, 4, 5),
	finally if none of the above apply, play a random move.
	
	This is an improvement upon the medium cpu as instead of playing a random move
	when there are no opportunities to win or block a win, it employs more strategies
	such as weighing patterns and centering middle which both outweights medium cpu.
	In addition, medium cpu has a problem in that it doesn't detect horizontal 4s properly,
	ie. if the pattern is 0011100, cpu would block as 0211100 or 0011120, but both of these
	will result in a win for player 1. Hence, I used a function block_horizontal to detect that,
	so that when play 1 plays a move other than column 4, cpu will play column 4, and when player 1 
	plays column 4, cpu will block it by playing column 5.>

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player whose turn it is, integer value of 1 or 2.
	:return: None
	"""
	# 6 steps involved.
	# Check if only one column left > Check for winning moves > Check for defending moves > Play high weighing moves > Prioritise center > Random move

	# Storing the number of rows and columns into variables 'row' and 'column'.
	row = len(board)
	column = len(board[0])

	# 1. Check if only one column left
	count = 0
	# Iterate through each column.
	for i in range(1, column + 1):

		# For every row in board, replicate it using slice.abs
		# ie. board[0] = [0, 0, 0, 0, 0, 0, 0]
		# Replicate a temporary board so drop_piece doesn't change the board.
		temp = [row[:] for row in board]

		# Everytime drop_piece returns False, the column is full.
		if drop_piece(temp, player, i) == False:
			count += 1

	# When count is 1 less than the number of columns, only one column is not full.
	if count == column - 1:
		# Iterate through each column again and return the valid column.
		for i in range(1, column + 1):
			if drop_piece(board, player, i):
				return i

	# 2. Check for winning moves
	for i in range(1, column + 1):
		# Create a new board with the same rows
		temp = [row[:] for row in board]

		# If dropping is valid
		if drop_piece(temp, player, i):

			# If there is a winning move for cpu, play it
			if analyse_medium(temp, player):
				drop_piece(board, player, i)
				return i

    # 3. Check for blocking moves
	for i in range(1, column + 1):
		# Create a new board with the same rows
		temp = [row[:] for row in board]

		# If dropping is valid
		if drop_piece(temp, player % 2 + 1, i):

			# If there is a winning move for player, block it
			if analyse_medium(temp, player % 2 + 1):
				drop_piece(board, player, i)
				return i 
	
	# Check for horizontal patterns, preventing 4s in horizontal for player using block_horizontal function.
	global block_count
	if block_count == 0:
		block = block_horizontal(board)
		if block_horizontal(board) != False:
			drop_piece(board, player, block)
			block_count += 1
			return block

	# 4. Play the move with the highest weighing. 
	for i in range(1, column + 1):
		# Create a new board with the same rows
		temp = [row[:] for row in board]

		# If dropping is valid
		if drop_piece(temp, player, i):

			# Play the highest weighting move
			if analyse_hard(temp, player):
				drop_piece(board, player, i)
				return i

	# If not, connect 3 in a roll
	for i in range(1, column + 1):
		# Create a new board with the same rows
		temp = [row[:] for row in board]

		# If dropping is valid
		if drop_piece(temp, player, i):

			# If there is a possibility to connect 3, play it
			if analyse_three(temp, player):
				drop_piece(board, player, i)
				return i
	
	# 5. Prioritise center 
	# Create a temporary board, only drop if row is above 4. 
	temp = [row[:] for row in board]
	if drop_piece(temp, player, 4) and board[3][4] == 0:
		drop_piece(board, player, 4)
		return 4
	elif drop_piece(temp, player, 3) and board[3][3] == 0:
		drop_piece(board, player, 3)
		return 3
	elif drop_piece(temp, player, 5) and board[3][5] == 0:
		drop_piece(board, player, 5)
		return 5
	elif drop_piece(temp, player, 2) and board[3][2] == 0:
		drop_piece(board, player, 2)
		return 2
	elif drop_piece(temp, player, 6) and board[3][6] == 0:
		drop_piece(board, player, 6)
		return 6

	# 6. If no winning/defending moves, and no single column, return a random column
	i = random.randint(1, 7)
	if drop_piece(board, player, i):
		return i
	
	# 'i' column is returned. 

# CPU Selection (Helper Function 5)
def cpu_selection(cpu_difficulty):
	'''
	This function is used with game_with_cpu function to pass in the 
	steps that prompt user and cpu to play a move after user selects a 
	cpu difficulty. 
	'''
	clear_screen()
	board = create_board()
	print_board(board)

	while True:
		# Prompt the player for a column to drop
		column = execute_player_turn(1, board)

		# Clear the screen and print the board
		clear_screen()
		print_board(board)

		# Print message
		print(f'Player 1 dropped a piece into column {column} ')

		# Check for win or draw
		result = end_of_game(board)
		if result == 1 or result == 2:
			print(f'Player {result} has won!')
			play_again = input('Press 1 to exit: ')
			if play_again == '1':
				break
			else:
				break

		elif result == 3:
			print(f'This game is a draw!')
			play_again = input('Press 1 to exit: ')
			if play_again == '1':
				break
			else:
				break

		# Repeat for cpu 
		column = cpu_difficulty(board, 2)

		# Clear the screen and print the board
		clear_screen()
		print_board(board)
		print(f'Player 2 dropped a piece into column {column} ')
		result = end_of_game(board)

		# Check for win or draw
		if result == 1 or result == 2:
			print(f'Player {result} has won!')
			play_again = input('Press 1 to exit: ')
			if play_again == '1':
				break
			else:
				break

		elif result == 3:
			print(f'This game is a draw!')
			play_again = input('Press 1 to exit: ')
			if play_again == '1':
				break
			else:
				break

def game_against_cpu():
	"""
	Runs a game of Connect 4 against the computer.

	:return: None
	"""
	# Implement your solution below
	# Set option screen by printing
	clear_screen()
	print('=============== Difficulty ===============')
	print('Please select a difficulty!')
	print('1. Easy')
	print('2. Medium')
	print('3. Hard')
	print('=========================================')

	# Prompt for an option for difficulty
	option = input('Please select an option (1/2/3): ')

	# Direct user to easy cpu if option is 1
	if option == '1':
		cpu_selection(cpu_player_easy)

	# Direct user to medium cpu if option is 2
	elif option == '2':
		cpu_selection(cpu_player_medium)

	# Direct user to hard cpu is option is 3.
	elif option == '3':
		cpu_selection(cpu_player_hard)


# Run the main function to start the game. 
if __name__ == "__main__":
	main()

import random

# CLEAR SCREEN FUNCTION
# Clears the screen 
def clear_screen():
	import os
	os.system('cls' if os.name == 'nt' else 'clear')

# STARTING SCREEN 
# I set the number of rows and columns mandatory to larger than 3 because it's the minimum requirement for any number of connected ks. 
# Similarly, I set a restriction to the number of players, as otherwise there will be too many letters on the board, which will look too messy.
clear_screen()
print('==================== Welcome to Connect.k ===================')
while True:
	rules = str(input('Press k to view rules: '))
	if rules == 'k':
		print('=========================== Rules ===========================')
		print('1. Number of rows and columns cannot be less than 3.')
		print('2. Number of tokens has to be less than the number of rows.')
		print('3. Number of human and cpu players combined cannot be more than 5.')
		print('4. Levels of cpus are restricted to easy, medium and hard.')
		break
while True:
	print('=============================================================')
	start = str(input('Press k to start: '))
	if start == 'k':
		break

# Setting initial values for all variables, so that a loop can be created if incorrect inputs are given
row_number = 0
column_number = 0
tokens = 0
player_number = 6
cpu_number = 0
cpu_level = 'none'

# Prompting user for inputs
while row_number < 3 or column_number < 3 or tokens >= row_number or player_number + cpu_number > 5:
	try:
		clear_screen()
		print('======================= Configurations ======================')
		row_number = int(input('Please enter the number of rows of the game board: '))
		column_number = int(input('Please enter the number of columns of the game board: '))   
		tokens = int(input('Please enter the number k of tokens that need to be connected in order to win: '))   
		player_number = int(input('Please enter the number of players: '))
		cpu_number = int(input('Please enter the number of CPU players: '))
		print('=============================================================')
		print(f'The number of rows is set to {row_number}')
		print(f'The number of columns is set to {column_number}')
		print(f'The number of tokens is set to {tokens}')
		print(f'The number of players is set to {player_number}')
		print(f'The number of cpus is set to {cpu_number}')
		print('=============================================================')
		if cpu_number == 0:
			start = str(input('Press k to start: '))
			if start == 'k':
				break
	except ValueError:
		print('Please enter a valid integer!')

# Start the game if cpu number is 0, otherwise prompt user to input a difficulty
if cpu_number != 0:
	while True:
		try:
			cpu_level = str(input('Please enter the level of CPU players (easy/medium/hard): '))
			break
		except ValueError:
			print('Please enter a valid level!')

# CREATE BOARD FUNCTION
# Create a board based on row and column inputs
def create_board():
	board = []
	# Setting row and column as variables so it's easier to change.
	row = row_number
	column = column_number

	for i in range(row):

		'''
		[[0, 0, 0, 0, 0, 0, 0]]
		'''

		board.append([0] * column)
		# column is taken from column_number, which is user input from before.
		# Create a row with (column) * [0], append to board.
		# Iterate this (row) times.

		'''
		[[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0]]
		'''

	return board
	# 'board' Variable is returned.

# PRINT BOARD FUNCTION
def print_board(board):
	# Takes board as input from create_board.
	# Storing length of row and column into variables 'rows' and 'columns'.
	rows = len(board)
	columns = len(board[0])

	# This is to print the first three rows of the board according to the length of column from input. 
	print('==' * (columns - 3) + f' Connect...{tokens} ' + '==' * (columns - 3))
	for i in range(1, columns + 1):
		print(f'  {i} ', end = '')
	print()

	# Creating the cubicles 
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

			# Repeated for players 3, 4 and 5, if there are 5 human players. 
			
			elif board[i][j] == 3:
				print('| A ', end='')

			elif board[i][j] == 4:
				print('| B ', end='')
			
			elif board[i][j] == 5:
				print('| C ', end='')

		# Finish the row with |
		print('|')

	# Iterate this process (row) times

	# The finishing lines
	print(' ---' * columns)
	print('====' * columns + '=')
	# Nothing is returned. 

# DROP PIECE FUNCTION
def drop_piece(board, player, column):
	# len(board) - 1 gives 5 if there are 6 rows, as row counting starts from 0. 
	i = len(board) - 1
	
	# Iterate through each row to see if the slot is 0, if yes replace with 1 and return True
	while i >= 0:

		# column - 1 because counting starts from 0.
		if board[i][column - 1] == 0:
			board[i][column - 1] = player

			# Return true after making a change.
			return True
		else:
			i -= 1

	return False
	# True or False is returned. 

# EXECUTE PLAYER TURN FUNCTION
def execute_player_turn(player, board): 
	while True:
		# Prompt player for input in integer.
		column = int(input(f'Player {player}, please enter the column you would like to drop your piece into: '))

		# Append all column numbers into a list called total [1,2,3,4,5,6,7...]
		total = []
		column_count = len(board[0])
		for i in range(1, column_count + 1):
			total.append(i)

		# If the column is in the list 'total' and is a valid drop, drop the piece.
		if column in total:
			if drop_piece(board, player, column):
				# If drop_piece function returns True, return column.
				return column

				# If drop_piece returns False, column is full.
			else:
				print("That column is full, please try again.")

		# Else, input is not in 'valid_input', print invalid input. 
		else:
			print("Invalid input, please try again.")
			# column is returned.

# END OF GAME FUNCTION
def end_of_game(board): 

	# Storing number of rows and columns into variables
	rows = len(board)
	columns = len(board[0])

	# Check for (token) of the same digit in a column
	# Iterate through each column
	for i in range(rows - (tokens - 1)):
		for j in range(columns):
			# Check for the correct number of tokens in a roll, based on the user input 'tokens'.
			for k in range(1, tokens):
				# If the cell is 0, or if the adjacent cell is not the same, break the loop (k loop) and check the next cell.
				if board[i][j] != board[i + k][j] or board[i][j] == 0:
					break
			# else is outside the k loop to ensure it only returns after k loop finishes running and there are no breaks. 
			else: 
				return board[i][j]

	# Repeat for row and diagonals.

	# Check for (token) of the same digit in a row
	for i in range(rows):
		for j in range(columns - (tokens - 1)):
			for k in range(1, tokens):
				if board[i][j] != board[i][j + k] or board[i][j] == 0:
					break
			else:
				return board[i][j]

	# Check for (token) of the same digit backward leaning
	for i in range(rows - (tokens - 1)):
		for j in range(columns - (tokens - 1)):
			for k in range(1, tokens):
				if board[i][j] != board[i + k][j + k] or board[i][j] == 0:
					break
			else:
				return board[i][j]

	# Check for (token) of the same digit forward leaning
	for i in range(rows - (tokens - 1)):
		for j in range((tokens - 1), columns):
			for k in range(1, tokens):
				if board[i][j] != board[i + k][j - k] or board[i][j] == 0:
					break
			else:
				return board[i][j]

	# If there's a [0] on the board, game is still going, return 0
	for i in range(rows):
		for j in range(columns):
			if board[i][j] == 0:
				return 0
				
	# If no k in a row, or no [0] on the board (full board), return 3
	return 3
	# 0, 1, 2 or 3 are returned.


# LOCAL PLAYER GAME FUNCTION
def local_player_game():

	# Creating the board everytime, this step is fixed.
	clear_screen()
	board = create_board()
	print_board(board)

	j = 0
	while j < 1:
		# Iterate through each player, asking for input.
		for i in range(1, player_number + 1):
			column = execute_player_turn(i, board)

			clear_screen()
			print_board(board)

			# Prints a statement of move just made
			print(f'Player {i} dropped a piece into column {column}')

			# Check for win, loss, draw of continued game. 
			result = end_of_game(board)
			winner = []
			for i in range(1, player_number + 1):
				winner.append(i)
			if result in winner:
				print(f'Player {result} has won!')
				j = 2
				break
			elif result == 3:
				print(f'This game is a draw!')
				j = 2
				break
		# Nothing is returned

# EASY CPU FUNCTION
def cpu_player_easy(board, player):
	while True:
		# Setting a random integer from 1 to the number of columns (inclusive) to the variable column.
		column_number = len(board[0])
		column = random.randint(1, column_number)

		# drop_piece drops the piece and returns True if dropping is valid.
		if drop_piece(board, player, column):
			return column
		# column is returned.

# ANALYSE MEDIUM (Similar to end_of_game)
# Takes board and player as input, if there is a winning move, return True.
# Note that player input is not necessary, because blocking can be done by see whcih drop is valid. However it's added for clearer explanation.
def analyse_medium(board, player): 
	rows = len(board)
	columns = len(board[0])

	# Check for (token) of the same digit in a column
	for i in range(rows - (tokens - 1)):
		for j in range(columns):
			for k in range(1, tokens):
				# Iterate (token) times, if there is a break (different consecutive numbers) or if the cell is 0, break and check for the next cell. 
				# Note that cell cannot be 0 as that would result in 0000...
				if board[i][j] != board[i + k][j] or board[i][j] == 0:
					break
			# If no break and not 0, return True
			else: 
				return True
	
	# Repeat for rows and diagonals

	# Check for (token) of the same digit in a row
	for i in range(rows):
		for j in range(columns - (tokens - 1)):
			for k in range(1, tokens):
				if board[i][j] != board[i][j + k] or board[i][j] == 0:
					break
			else:
				return True

	# Check for (token) of the same digit backward leaning
	for i in range(rows - (tokens - 1)):
		for j in range(columns - (tokens - 1)):
			for k in range(1, tokens):
				if board[i][j] != board[i + k][j + k] or board[i][j] == 0:
					break
			else:
				return True

	# Check for (token) of the same digit forward leaning
	for i in range(rows - (tokens - 1)):
		for j in range((tokens - 1), columns):
			for k in range(1, tokens):
				if board[i][j] != board[i + k][j - k] or board[i][j] == 0:
					break
			else:
				return True	
				
	return False

# MEDIUM CPU FUNCTION
def cpu_player_medium(board, player):
	# 4 steps involved.
	# Check if only one column left > Check for winning moves > Check for defending moves > Random move

	# Storing the number of rows and columns into variables 'row' and 'column'.
	row = len(board)
	column = len(board[0])

	# 1. Check if only one column left
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
		# Create a new board with the same rows
		temp = [row[:] for row in board]

		# If dropping is valid for cpu
		if drop_piece(temp, player, i):

			# If there is a winning move for cpu, play it
			if analyse_medium(temp, player):
				drop_piece(board, player, i)
				return i

    # 3. Check for blocking moves
	for i in range(1, column + 1):
		# Create a new board with the same rows
		temp = [row[:] for row in board]

		# If dropping is valid for player
		if drop_piece(temp, player_number + 1 - cpu_number, i):

			# If there is a winning move for player, block it
			if analyse_medium(temp, player_number + 1 - cpu_number):
				drop_piece(board, player, i)
				return i 

	# 4. If no winning/defending moves, and no single column, return a random column
	i = random.randint(1, column)
	if drop_piece(board, player, i):
		return i
	# i (The cell to play) is returned. 

# ANALYSE HARD FUNCTION
# Similar to analyse_medium but added a weight element to choose the best move. 
def analyse_hard(board, player):
	rows = len(board)
	columns = len(board[0])
	
	# Creates a dictionary of patterns for the cpu to check
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
		(0, 0, 0, player): 5,
		(0, 0, player, 0): 5,
		(0, player, 0, 0): 5,
		(player, 0, 0, 0): 5
	}

	# Check for vertical pattern
	for i in range(rows - 3):
		for j in range(columns):
			key = (board[i][j], board[i+1][j], board[i+2][j], board[i+3][j])
			if key in weight:
				# prioritise the highest weighing pattern
				if weight[key] > 50:
					return True
				elif key.count(player) == 3:
					if weight[key] > 10:
						return True
					elif key.count(player) == 2:
						return True
					elif key.count(player) == 1:
						return True

	# Check for horizontal pattern
	for i in range(rows):
		for j in range(columns - 3):
			key = (board[i][j], board[i][j+1], board[i][j+2], board[i][j+3])
			if key in weight:
				# prioritise the highest weighing pattern
				if weight[key] > 50:
					return True
				elif key.count(player) == 3:
					if weight[key] > 10:
						return True
					elif key.count(player) == 2:
						return True
					elif key.count(player) == 1:
						return True

	# Check for backward leaning pattern
	for i in range(rows - 3):
		for j in range(columns - 3):
			key =(board[i][j], board[i+1][j+1], board[i+2][j+2], board[i+3][j+3])
			if key in weight:
				# prioritise the highest weighing pattern
				if weight[key] > 50:
					return True
				elif key.count(player) == 3:
					if weight[key] > 10:
						return True
					elif key.count(player) == 2:
						return True
					elif key.count(player) == 1:
						return True

	# Check for forward leaning pattern
	for i in range(rows - 3):
		for j in range(3, columns):
			key = (board[i][j], board[i+1][j-1], board[i+2][j-2], board[i+3][j-3])
			if key in weight:
				# prioritise the highest weighing pattern
				if weight[key] > 50:
					return True
				elif key.count(player) == 3:
					if weight[key] > 10:
						return True
					elif key.count(player) == 2:
						return True
					elif key.count(player) == 1:
						return True

	return False

# BLOCK HORIZONTAL FUNCTION
# This prevents the player from connecting ks in a row.
def block_horizontal(board):
	rows = len(board)
	columns = len(board[0])
	
	weight = {
		(0, 0, 0, 1, 0, 0, 0): 100,
		(0, 0, 1, 0, 0, 0, 0): 80,
		(0, 1, 0, 0, 0, 0, 0): 80,
		(0, 0, 0, 0, 1, 0, 0): 80,
		(0, 0, 0, 0, 0, 1, 0): 80,
		(0, 0, 0, 0, 0, 0, 1): 80,
		(1, 0, 0, 0, 0, 0, 0): 80
	}

	# Iterate through the bottom row to see if 7 consecutive cells fit the pattern in 'weight'
	key = (board[rows-1][int(columns/2)-3], board[rows-1][int(columns/2)-2], board[rows-1][int(columns/2)-1], board[rows-1][int(columns/2)], board[rows-1][int(columns/2)+1], board[rows-1][int(columns/2)+2], board[rows-1][int(columns/2)+3])
	if key in weight:
		# If player placed the first piece in the middle, cpu places it next to it. 
		if weight[key] > 90:
			return board[rows-1][int(columns/2)+1]
		# If player placed the first piece anywhere else, cpu places it in the middle. 
		elif weight[key] > 70:
			return board[rows-1][int(columns/2)]

	return False

# HARD CPU FUNCTION
block_count = 0
# This makes sure block_horizontalfunction only runs once
def cpu_player_hard(board, player):
	# 6 steps involved.
	# Check if only one column left > Check for winning moves > Check for defending moves > Play high weighing moves > Prioritise center > Random move


	# Storing the number of rows and columns into variables 'row' and 'column'.
	row = len(board)
	column = len(board[0])

	# 1. Check if only one column left
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
		if drop_piece(temp, player_number + 1 - cpu_number, i):

			# If there is a winning move for player, block it
			if analyse_medium(temp, player_number + 1 - cpu_number):
				drop_piece(board, player, i)
				return i 

	# Check for horizontal patterns, preventing ks in horizontal for player
	global block_count
	# Only if column number is greater than 6 does the block function work
	if column_number >= 7:
		if block_count == 0:
			block = block_horizontal(board)
			if block_horizontal(board) != False:
				drop_piece(board, player, block)
				block_count += 1
				return block
	
	# 4. Play the move with the highest weighting pattern			
	for i in range(1, column + 1):
		# Create a new board with the same rows
		temp = [row[:] for row in board]

		# If dropping is valid
		if drop_piece(temp, player, i):

			# Play the highest weighting move
			if analyse_hard(temp, player):
				drop_piece(board, player, i)
				return i

	# 5. If not, prioritise the center
	temp = [row[:] for row in board]
	if drop_piece(temp, player, int(column_number / 2)) and temp[row - 3][int(column_number / 2)] == 0:
		drop_piece(board, player, int(column_number / 2))
		return int(column_number / 2)
	elif drop_piece(temp, player, int(column_number / 2) + 1) and temp[row - 3][int(column_number / 2) + 1] == 0:
		drop_piece(board, player, int(column_number / 2) + 1)
		return int(column_number / 2) + 1
	elif drop_piece(temp, player, int(column_number / 2) - 1) and temp[row - 3][int(column_number / 2) - 1] == 0:
		drop_piece(board, player, int(column_number / 2) - 1)
		return int(column_number / 2) - 1

	# 6. If no winning/defending moves, and no single column, return a random column
	i = random.randint(1, column)
	if drop_piece(board, player, i):
		return i

# CPU SELECTION FUNCTION
def cpu_selection(cpu_difficulty):
	clear_screen()
	board = create_board()
	print_board(board)

	while True:
		# Iterate over every human play and prompt for a move
		for i in range(1, player_number + 1):
			column = execute_player_turn(i, board)
			clear_screen()
			print_board(board)

			# Prints a statement of move just made
			print(f'Player {i} dropped a piece into column {column}')

			# Check for win, loss, draw of continued game. 
			result = end_of_game(board)
			winner = []
			for j in range(1, player_number + 1):
				winner.append(j)
			if result in winner:
				print(f'Player {result} has won!')
				return 1
			elif result == 3:
				print(f'This game is a draw!')
				return 1

		# Iterate over every cpu player and play a move
		for i in range(player_number + 1, cpu_number + player_number + 1):
			column = cpu_difficulty(board, i)
			clear_screen()
			print_board(board)

			# Prints a statement of move just made
			print(f'Player {i} dropped a piece into column {column}')

			# Check for win, loss, draw of continued game. 
			result2 = end_of_game(board)
			winner2 = []
			for j in range(player_number + 1, cpu_number + player_number + 1):
				winner2.append(j)
			if result2 in winner2:
				print(f'Player {result2} has won!')
				return 1
			elif result2 == 3:
				print(f'This game is a draw!')
				return 1

# GAME AGAINST CPU FUNCTION
def game_against_cpu():
	# Direct user to easy cpu if option is easy
	if cpu_level == 'easy':
		cpu_selection(cpu_player_easy)

	# Repeat for medium cpu
	elif cpu_level == 'medium':
		cpu_selection(cpu_player_medium)

	# Repeat for hard cpu
	elif cpu_level == 'hard':
		cpu_selection(cpu_player_hard)

# CONNECTK FUNCTION
def connectk():
	# If no cpu players, start local player game
	if cpu_number == 0:
		clear_screen()
		local_player_game()
		# Prompt user to play again
		repeat = input('Press k to play again: ')
		if repeat == 'k':
			connectk()
	# If there exists cpu players, start game agaisnt cpu
	elif cpu_number != 0:
		clear_screen()
		game_against_cpu()
		repeat = input('Press k to play again: ')
		if repeat == 'k':
			connectk()

# RUNNING THE GAME
if __name__ == "__main__":
	# Play the game connect k
	connectk()

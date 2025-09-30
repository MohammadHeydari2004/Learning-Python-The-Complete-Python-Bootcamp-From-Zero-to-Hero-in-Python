"""
pip install pyinstaller

pyinstaller --onefile --name "Tic-Tac-Toe" Tic-Tac-Toe.py
(pyinstaller --onefile --windowed --name "Tic-Tac-Toe" --icon=game.ico Tic-Tac-Toe.py)
(# اگر بازی بدون کنسول باشد
pyinstaller --onefile --windowed --name "Tic-Tac-Toe" Tic-Tac-Toe.py)
"""

import time  # Import time module for program delay at exit (وارد کردن ماژول زمان برای تاخیر در پایان برنامه)

# ======================
# SECTION 1: CONSTANTS
# ======================
BOARD_SIZE = 3  # Define board dimension constant (تعریف ثابت ابعاد صفحه بازی)
EMPTY_CELL = " --- "  # Define empty cell representation (تعریف نمایش خانه خالی)
WINNING_COMBINATIONS = [  # Define all winning position combinations (تعریف تمام ترکیبات برنده)
		# Rows (سطرها)
		[ (0 , 0) , (0 , 1) , (0 , 2) ] ,
		[ (1 , 0) , (1 , 1) , (1 , 2) ] ,
		[ (2 , 0) , (2 , 1) , (2 , 2) ] ,
		# Columns (ستون‌ها)
		[ (0 , 0) , (1 , 0) , (2 , 0) ] ,
		[ (0 , 1) , (1 , 1) , (2 , 1) ] ,
		[ (0 , 2) , (1 , 2) , (2 , 2) ] ,
		# Diagonals (اِریب‌ها)
		[ (0 , 0) , (1 , 1) , (2 , 2) ] ,
		[ (0 , 2) , (1 , 1) , (2 , 0) ]
]


# ============================
# SECTION 2: BOARD MANAGEMENT
# ============================

def initialize_board ( ) :  # Initialize a new empty game board (راه‌اندازی یک صفحه بازی جدید خالی)
	return [ [ EMPTY_CELL for _ in range ( BOARD_SIZE ) ] for _ in
	         range ( BOARD_SIZE ) ]  # Create 3x3 grid with empty cells (ایجاد شبکه 3x3 با خانه‌های خالی)


def display_board ( board ) :  # Display the current game board state (نمایش وضعیت فعلی صفحه بازی)
	for i in range ( BOARD_SIZE ) :  # Iterate through each row (پیمایش هر سطر)
		print ( " | ".join ( board [ i ] ) )  # Print row with separators (چاپ سطر با جداکننده‌ها)
		if i < BOARD_SIZE - 1 :  # Print separator between rows except last row (چاپ جداکننده بین سطرها به جز سطر آخر)
			print ( "-" * 21 )  # Print horizontal separator line (چاپ خط جداکننده افقی)


def position_to_coordinates (
		position
		) :  # Convert 1-9 position to (row, col) coordinates (تبدیل موقعیت 1-9 به مختصات (سطر، ستون))
	position = int ( position )  # Ensure position is integer (اطمینان از عدد صحیح بودن موقعیت)
	row = (position - 1) // BOARD_SIZE  # Calculate row index (محاسبه شاخص سطر)
	col = (position - 1) % BOARD_SIZE  # Calculate column index (محاسبه شاخص ستون)
	return row , col  # Return coordinate pair (بازگرداندن جفت مختصات)


def is_valid_position (
		board , position
		) :  # Check if position is valid and available (بررسی معتبر و خالی بودن موقعیت)
	if not position.isdigit ( ) :  # Verify position is numeric (بررسی عددی بودن موقعیت)
		print ( "Invalid Choice - Enter a number (انتخاب نامعتبر - یک عدد وارد کنید)" )
		return False  # Invalid input type (نوع ورودی نامعتبر)

	position = int ( position )  # Convert to integer (تبدیل به عدد صحیح)
	if position < 1 or position > 9 :  # Check range (بررسی محدوده)
		print ( "Out of range (1-9) (خارج از محدوده (1-9))" )
		return False  # Position out of bounds (موقعیت خارج از محدوده)

	row , col = position_to_coordinates ( position )  # Get coordinates (دریافت مختصات)
	if board [ row ] [ col ] != EMPTY_CELL :  # Check if cell is occupied (بررسی اشغال بودن خانه)
		print ( "Position already taken (موقعیت قبلاً انتخاب شده)" )
		return False  # Position already occupied (موقعیت اشغال شده)

	return True  # Valid position (موقعیت معتبر)


def place_mark ( board , position , symbol ) :  # Place player's mark on board (قرار دادن علامت بازیکن روی صفحه)
	row , col = position_to_coordinates ( position )  # Convert position to coordinates (تبدیل موقعیت به مختصات)
	board [ row ] [ col ] = f"  {symbol}  "  # Update board cell (به‌روزرسانی خانه صفحه)
	return board  # Return updated board (بازگرداندن صفحه به‌روزشده)


# ======================
# SECTION 3: GAME LOGIC
# ======================

def check_win ( board , symbol ) :  # Check if current player has won (بررسی برد بازیکن فعلی)
	mark = f"  {symbol}  "  # Format symbol for comparison (فرمت‌دهی نماد برای مقایسه)
	for combination in WINNING_COMBINATIONS :  # Check all winning combinations (بررسی تمام ترکیبات برنده)
		if all (
				board [ row ] [ col ] == mark for row , col in combination
				) :  # Verify all positions match (تأیید تطابق تمام موقعیت‌ها)
			return True  # Win condition met (شرایط برد برقرار است)
	return False  # No win found (بردی یافت نشد)


def is_board_full ( board ) :  # Check if board has no empty cells (بررسی پر بودن تمام خانه‌های صفحه)
	return all (  # Check all cells (بررسی تمام خانه‌ها)
			cell != EMPTY_CELL  # Verify cell is occupied (تأیید اشغال بودن خانه)
			for row in board  # Iterate rows (پیمایش سطرها)
			for cell in row  # Iterate cells (پیمایش خانه‌ها)
	)


# ===========================
# SECTION 4: PLAYER HANDLING
# ===========================

def get_player_symbol ( ) :  # Get player 1's symbol choice (دریافت انتخاب نماد بازیکن 1)
	while True :  # Keep asking until valid input (تکرار تا دریافت ورودی معتبر)
		print ( "Player 1, choose your symbol (X or O): " )  # Prompt for symbol (درخواست نماد)
		symbol = input ( ).strip ( ).upper ( )  # Get and normalize input (دریافت و نرمال‌سازی ورودی)
		if symbol in [ 'X' , 'O' ] :  # Validate symbol (اعتبارسنجی نماد)
			return symbol , 'O' if symbol == 'X' else 'X'  # Return both players' symbols (بازگرداندن نماد هر دو بازیکن)
		print ( "Invalid choice - enter X or O (انتخاب نامعتبر - X یا O وارد کنید)" )  # Error message (پیام خطا)


def get_position ( player ) :  # Get valid position from player (دریافت موقعیت معتبر از بازیکن)
	while True :  # Keep asking until valid position (تکرار تا دریافت موقعیت معتبر)
		print ( f"Player {player}, enter position (1-9): " )  # Prompt for position (درخواست موقعیت)
		print ( "1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9" )  # Show position reference (نمایش مرجع موقعیت‌ها)
		position = input ( ).strip ( )  # Get player input (دریافت ورودی بازیکن)
		if is_valid_position ( board , position ) :  # Validate position (اعتبارسنجی موقعیت)
			return position  # Return valid position (بازگرداندن موقعیت معتبر)


# =====================
# SECTION 5: MAIN GAME
# =====================

def main_game_loop ( ) :  # Main game execution loop (حلقه اصلی اجرای بازی)
	global board  # Use global board variable (استفاده از متغیر جهانی صفحه)
	board = initialize_board ( )  # Create new game board (ایجاد صفحه بازی جدید)

	# Get player symbols (دریافت نماد بازیکنان)
	player1_symbol , player2_symbol = get_player_symbol ( )  # Assign symbols to players (تخصیص نماد به بازیکنان)

	# Display initial board (نمایش صفحه اولیه)
	print ( "\nStarting game..." )  # Game start message (پیام شروع بازی)
	display_board ( board )  # Show empty board (نمایش صفحه خالی)

	# Main gameplay loop (حلقه اصلی بازی)
	for turn in range ( 9 ) :  # Maximum 9 turns (حداکثر 9 نوبت)
		current_player = 1 if turn % 2 == 0 else 2  # Determine current player (تعیین بازیکن فعلی)
		symbol = player1_symbol if current_player == 1 else player2_symbol  # Get current symbol (دریافت نماد فعلی)

		# Get and validate position (دریافت و اعتبارسنجی موقعیت)
		position = get_position ( current_player )  # Get player's move (دریافت حرکت بازیکن)
		board = place_mark ( board , position , symbol )  # Update board (به‌روزرسانی صفحه)

		# Display updated board (نمایش صفحه به‌روزشده)
		print (
			f"\nPlayer {current_player} placed '{symbol}' at position {position}"
			)  # Move confirmation (تأیید حرکت)
		display_board ( board )  # Show current state (نمایش وضعیت فعلی)

		# Check win condition (بررسی شرط پیروزی)
		if check_win ( board , symbol ) :  # Verify win (تأیید برد)
			print ( f"\nPlayer {current_player} wins! Congratulations!" )  # Win announcement (اعلام پیروزی)
			return True  # Game ended with win (بازی با پیروزی پایان یافت)

		# Check draw condition (بررسی شرط تساوی)
		if is_board_full ( board ) :  # Verify board full (تأیید پر بودن صفحه)
			print ( "\nGame ended in a draw!" )  # Draw announcement (اعلام تساوی)
			return False  # Game ended in draw (بازی با تساوی پایان یافت)

	return False  # Safety return (بازگشت ایمنی)


# ===========================
# SECTION 6: PROGRAM FLOW
# ===========================

def main ( ) :  # Main program controller (کنترل‌کننده اصلی برنامه)
	print ( "Welcome to Tic-Tac-Toe!" )  # Welcome message (پیام خوش‌آمدگویی)

	while True :  # Game session loop (حلقه جلسه بازی)
		game_ended = main_game_loop ( )  # Start new game (شروع بازی جدید)

		# Ask to replay (درخواست تکرار بازی)
		print ( "\nPlay again? (y/n): " )  # Replay prompt (درخواست تکرار)
		if input ( ).strip ( ).lower ( ) not in [ 'y' , 'yes' ] :  # Check response (بررسی پاسخ)
			print ( "Thanks for playing! Goodbye." )  # Farewell message (پیام خداحافظی)
			break  # Exit game loop (خروج از حلقه بازی)


# ===========================
# SECTION 7: PROGRAM ENTRY
# ===========================

if __name__ == "__main__" :  # Program entry point check (بررسی نقطه ورود برنامه)
	main ( )  # Start main program (شروع برنامه اصلی)
	time.sleep ( 30 )  # Delay before exit (تاخیر قبل از خروج)
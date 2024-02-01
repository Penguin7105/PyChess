class ChessGame:
    def __init__(self):
        self.board = self.initialize_board()
        self.current_player = 'White'

    def initialize_board(self):
        # Initialize an 8x8 chess board
        board = [[' ' for _ in range(8)] for _ in range(8)]

        # Set up pieces
        for i in range(8):
            board[1][i] = 'P'  # Black pawns
            board[6][i] = 'p'  # White pawns

        pieces = 'RNBQKBNR'
        for i in range(8):
            board[0][i] = pieces[i]  # Black pieces
            board[7][i] = pieces[i].lower()  # White pieces

        return board

    def print_board(self):
        for row in self.board:
            print(' '.join(map(str, row)))
        print()

    def is_valid_move(self, start, end):
        # Check if the move is within the board boundaries
        return 0 <= start[0] < 8 and 0 <= start[1] < 8 and 0 <= end[0] < 8 and 0 <= end[1] < 8

    def make_move(self, start, end):
        piece = self.board[start[0]][start[1]]

        # Check if it's the correct player's turn
        if (self.current_player == 'White' and piece.islower()) or \
           (self.current_player == 'Black' and piece.isupper()):
            print("It's not your turn!")
            return False

        # Check if the move is valid for the specific piece
        if self.is_valid_move(start, end) and self.is_valid_piece_move(start, end):
            # Make the move
            self.board[end[0]][end[1]] = piece
            self.board[start[0]][start[1]] = ' '

            # Switch player turn
            self.current_player = 'White' if self.current_player == 'Black' else 'Black'
            return True

        print("Invalid move!")
        return False

    def is_valid_piece_move(self, start, end):
        # Add logic for validating piece moves (not implemented in this simplified version)
        # This should be extended for each type of chess piece
        return True


# Example usage:
game = ChessGame()
game.print_board()

while True:
    try:
        start = tuple(map(int, input("Enter the start position (row col): ").split()))
        end = tuple(map(int, input("Enter the end position (row col): ").split()))
    except ValueError:
        print("Invalid input. Please enter two space-separated integers.")
        continue

    if game.make_move(start, end):
        game.print_board()

    # Add logic for game over conditions (not implemented in this simplified version)
    # Adding a check system

class ChessGame:
    # ... (previous code)

    def is_in_check(self, player):
        king_symbol = 'K' if player == 'White' else 'k'
        king_position = None

        # Find the position of the king
        for row in range(8):
            for col in range(8):
                if self.board[row][col] == king_symbol:
                    king_position = (row, col)

        # Check if any opponent's piece can attack the king
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if (player == 'White' and piece.islower()) or \
                   (player == 'Black' and piece.isupper()):
                    if self.is_valid_piece_move((row, col), king_position):
                        return True

        return False

    def make_move(self, start, end):
        # ... (previous code)

        # Check for check after the move
        if self.is_in_check(self.current_player):
            print(f"Check! {self.current_player} is in check.")

        return True

class ChessGame:
    # ... (previous code)

    def is_checkmate(self, player):
        # Check if the player is in check
        if not self.is_in_check(player):
            return False

        # Check if any move can get the player out of check
        for start_row in range(8):
            for start_col in range(8):
                piece = self.board[start_row][start_col]

                # Check if the piece belongs to the current player
                if (player == 'White' and piece.isupper()) or \
                   (player == 'Black' and piece.islower()):
                    for end_row in range(8):
                        for end_col in range(8):
                            if self.make_move((start_row, start_col), (end_row, end_col)):
                                # If the move is valid, check if the player is still in check
                                if not self.is_in_check(player):
                                    # Undo the move
                                    self.board[start_row][start_col] = piece
                                    self.board[end_row][end_col] = ' '
                                    return False

                                # Undo the move
                                self.board[start_row][start_col] = piece
                                self.board[end_row][end_col] = ' '

        return True

    def make_move(self, start, end):
        # ... (previous code)

        # Check for checkmate after the move
        if self.is_checkmate(self.current_player):
            print(f"Checkmate! {self.current_player} is checkmated.")
            # You may want to end the game or handle checkmate differently here
            # For simplicity, the game continues in this example.

        return True


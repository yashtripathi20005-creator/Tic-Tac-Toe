"""
Tic-Tac-Toe Game Logic
Handles the game state, moves, and win detection
"""

class TicTacToeGame:
    """Core game logic for Tic-Tac-Toe."""
    
    def __init__(self):
        """Initialize a new game."""
        self.board = [' '] * 9
        self.current_player = 'X'
        self.winner = None
        self.game_over = False
    
    def make_move(self, position):
        """
        Make a move on the board.
        
        Args:
            position (int): Board position (0-8)
            
        Returns:
            bool: True if move was successful, False otherwise
        """
        if position < 0 or position > 8:
            return False
        
        if self.board[position] != ' ':
            return False
        
        if self.game_over:
            return False
        
        # Place the mark
        self.board[position] = self.current_player
        
        # Check for win or draw
        if self.check_win():
            self.winner = self.current_player
            self.game_over = True
        elif self.is_board_full():
            self.game_over = True
        else:
            # Switch players
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        
        return True
    
    def check_win(self):
        """
        Check if the current player has won.
        
        Returns:
            bool: True if current player has won, False otherwise
        """
        win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]               # Diagonals
        ]
        
        for pattern in win_patterns:
            if (self.board[pattern[0]] == self.current_player and
                self.board[pattern[1]] == self.current_player and
                self.board[pattern[2]] == self.current_player):
                return True
        
        return False
    
    def is_board_full(self):
        """
        Check if the board is full.
        
        Returns:
            bool: True if board is full, False otherwise
        """
        return ' ' not in self.board
    
    def reset_game(self):
        """Reset the game to initial state."""
        self.board = [' '] * 9
        self.current_player = 'X'
        self.winner = None
        self.game_over = False
    
    def get_available_moves(self):
        """
        Get list of available positions.
        
        Returns:
            list: List of available board positions
        """
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def get_board_state(self):
        """
        Get a copy of the current board state.
        
        Returns:
            list: Copy of the board
        """
        return self.board.copy()
    
    def get_status_message(self):
        """
        Get the current game status message.
        
        Returns:
            str: Status message
        """
        if self.game_over:
            if self.winner:
                return f"Player {self.winner} wins!"
            else:
                return "It's a draw!"
        else:
            return f"Player {self.current_player}'s turn"

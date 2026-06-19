"""
Tic-Tac-Toe GUI
Graphical user interface using tkinter
"""

import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    """GUI for the Tic-Tac-Toe game."""
    
    def __init__(self, game):
        """
        Initialize the GUI.
        
        Args:
            game: TicTacToeGame instance
        """
        self.game = game
        self.buttons = []
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")
        self.root.resizable(False, False)
        self.root.configure(bg='#2c3e50')
        
        self._create_widgets()
        self._update_status()
    
    def _create_widgets(self):
        """Create all GUI widgets."""
        # Title
        title_label = tk.Label(
            self.root,
            text="Tic-Tac-Toe",
            font=('Arial', 24, 'bold'),
            fg='#ecf0f1',
            bg='#2c3e50'
        )
        title_label.grid(row=0, column=0, columnspan=3, pady=10)
        
        # Game board
        board_frame = tk.Frame(self.root, bg='#34495e')
        board_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        
        for i in range(9):
            button = tk.Button(
                board_frame,
                text=' ',
                font=('Arial', 32, 'bold'),
                width=4,
                height=2,
                bg='#ecf0f1',
                fg='#2c3e50',
                relief=tk.RAISED,
                bd=3,
                command=lambda idx=i: self._handle_click(idx)
            )
            button.grid(row=i // 3, column=i % 3, padx=3, pady=3)
            self.buttons.append(button)
        
        # Status bar
        self.status_label = tk.Label(
            self.root,
            text="",
            font=('Arial', 14),
            fg='#ecf0f1',
            bg='#2c3e50'
        )
        self.status_label.grid(row=2, column=0, columnspan=3, pady=5)
        
        # Control buttons
        control_frame = tk.Frame(self.root, bg='#2c3e50')
        control_frame.grid(row=3, column=0, columnspan=3, pady=10)
        
        reset_button = tk.Button(
            control_frame,
            text="New Game",
            font=('Arial', 12, 'bold'),
            bg='#3498db',
            fg='white',
            padx=20,
            pady=5,
            relief=tk.RAISED,
            bd=2,
            command=self._reset_game
        )
        reset_button.pack(side=tk.LEFT, padx=5)
        
        quit_button = tk.Button(
            control_frame,
            text="Quit",
            font=('Arial', 12, 'bold'),
            bg='#e74c3c',
            fg='white',
            padx=20,
            pady=5,
            relief=tk.RAISED,
            bd=2,
            command=self.root.quit
        )
        quit_button.pack(side=tk.LEFT, padx=5)
    
    def _handle_click(self, position):
        """
        Handle button click.
        
        Args:
            position (int): Board position (0-8)
        """
        if self.game.make_move(position):
            self._update_board()
            self._update_status()
            
            # Check for game over
            if self.game.game_over:
                self._show_game_over_message()
    
    def _update_board(self):
        """Update all buttons to reflect current board state."""
        board = self.game.get_board_state()
        for i, button in enumerate(self.buttons):
            button.config(text=board[i])
            # Color the X and O differently
            if board[i] == 'X':
                button.config(fg='#e74c3c')
            elif board[i] == 'O':
                button.config(fg='#3498db')
            else:
                button.config(fg='#2c3e50')
    
    def _update_status(self):
        """Update the status label."""
        self.status_label.config(text=self.game.get_status_message())
    
    def _show_game_over_message(self):
        """Show game over popup message."""
        if self.game.winner:
            messagebox.showinfo(
                "Game Over",
                f"🎉 Player {self.game.winner} wins! 🎉"
            )
        else:
            messagebox.showinfo(
                "Game Over",
                "🤝 It's a draw! 🤝"
            )
    
    def _reset_game(self):
        """Reset the game to initial state."""
        self.game.reset_game()
        self._update_board()
        self._update_status()
    
    def run(self):
        """Start the GUI main loop."""
        self.root.mainloop()

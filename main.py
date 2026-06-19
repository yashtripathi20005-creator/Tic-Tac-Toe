"""
Tic-Tac-Toe Game
Main entry point for the application
"""

from game import TicTacToeGame
from gui import TicTacToeGUI

def main():
    """Initialize and run the Tic-Tac-Toe game."""
    game = TicTacToeGame()
    gui = TicTacToeGUI(game)
    gui.run()

if __name__ == "__main__":
    main()

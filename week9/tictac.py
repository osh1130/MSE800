import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        # Initialize the main window, game state variables, and create the GUI widgets.
        self.master = master
        self.master.title("Tic-Tac-Toe")
        self.player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        # Create a 3x3 grid of buttons for the Tic-Tac-Toe board.
        # Each button represents one cell of the board.
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.master, text="", font=("Arial", 36), width=5, height=2,
                                command=lambda row=i, col=j: self.click(row, col))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn

    def click(self, row, col):
        # Mark the cell if it's empty and the game is not over.
        # Check for a winner or a tie after each move.
        # Show a message if someone wins or if it's a tie, and reset the board.
        if self.buttons[row][col]["text"] == "" and not self.check_winner():
            self.buttons[row][col]["text"] = self.player
            self.board[row][col] = self.player
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.player} wins!")
                self.reset_board()
            elif all(all(cell != "" for cell in row) for row in self.board):
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_board()
            else:
                self.player = "O" if self.player == "X" else "X"

    def check_winner(self):
        # Each row
        # Each column
        # Two diagonals
        b = self.board
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] != "":
                return True
            if b[0][i] == b[1][i] == b[2][i] != "":
                return True
        if b[0][0] == b[1][1] == b[2][2] != "":
            return True
        if b[0][2] == b[1][1] == b[2][0] != "":
            return True
        return False

    def reset_board(self):
        # Set all cells to empty
        # Set the current player to "X"
        # Clear the text of all buttons
        self.player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

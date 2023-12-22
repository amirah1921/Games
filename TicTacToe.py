import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

        self.buttons = [tk.Button(master, text=' ', font=('Helvetica', 24), width=4, height=2,
                                  command=lambda i=i: self.make_move(i)) for i in range(9)]

        for i, button in enumerate(self.buttons):
            row, col = divmod(i, 3)
            button.grid(row=row, column=col)

        self.reset_button = tk.Button(master, text="Reset", font=('Helvetica', 16), command=self.reset_game)
        self.reset_button.grid(row=3, column=1, pady=10)

    def make_move(self, index):
        if self.board[index] == ' ' and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, state=tk.DISABLED)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"{self.current_player} wins!")
                self.reset_game()
            elif ' ' not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.switch_player()
                self.ai_move()

    def ai_move(self):
        if not self.check_winner():
            empty_indices = [i for i, mark in enumerate(self.board) if mark == ' ']
            if empty_indices:
                index = self.minimax(self.board, 'O')['index']
                self.board[index] = 'O'
                self.buttons[index].config(text='O', state=tk.DISABLED)
                if self.check_winner():
                    messagebox.showinfo("Game Over", "AI wins!")
                    self.reset_game()
                elif ' ' not in self.board:
                    messagebox.showinfo("Game Over", "It's a draw!")
                    self.reset_game()
                else:
                    self.switch_player()

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        for button in self.buttons:
            button.config(text=' ', state=tk.NORMAL)

    def minimax(self, new_board, player):
        available_spots = [i for i, mark in enumerate(new_board) if mark == ' ']

        if self.check_winner(new_board, 'X'):
            return {'score': -1}
        elif self.check_winner(new_board, 'O'):
            return {'score': 1}
        elif not available_spots:
            return {'score': 0}

        moves = []

        for spot in available_spots:
            move = {}
            move['index'] = spot
            new_board[spot] = player

            if player == 'O':
                result = self.minimax(new_board, 'X')
                move['score'] = result['score']
            else:
                result = self.minimax(new_board, 'O')
                move['score'] = result['score']

            new_board[spot] = ' '
            moves.append(move)

        if player == 'O':
            best_move = max(moves, key=lambda x: x['score'])
        else:
            best_move = min(moves, key=lambda x: x['score'])

        return best_move

    def check_winner(self, board=None, player=None):
        if board is None:
            board = self.board
        if player is None:
            player = self.current_player

        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]

        for combo in winning_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
                return True

        return False

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self, master):
        self.master = master
        self.master.geometry("200x400")
        self.master.title("Rock, Paper, Scissors")
        self.choices = ['Rock', 'Paper', 'Scissors']

        self.user_choice = tk.StringVar()
        self.ai_choice = tk.StringVar()

        self.label = tk.Label(self.master, text="Choose Rock, Paper, or Scissors:")
        self.label.pack(pady=10)

        for choice in self.choices:
            tk.Radiobutton(self.master, text=choice, variable=self.user_choice, value=choice).pack()

        self.result_label = tk.Label(self.master, text="", font=('Helvetica', 16))
        self.result_label.pack(pady=10)

        self.play_button = tk.Button(self.master, text="Play", command=self.play)
        self.play_button.pack()

    def play(self):
        user_choice = self.user_choice.get()
        ai_choice = random.choice(self.choices)

        self.ai_choice.set(f"AI chooses: {ai_choice}")

        result = self.determine_winner(user_choice, ai_choice)
        self.result_label.config(text=f"{result}\nAI chose: {ai_choice}")

    def determine_winner(self, user_choice, ai_choice):
        if user_choice == ai_choice:
            return "It's a tie!"
        elif (
            (user_choice == 'Rock' and ai_choice == 'Scissors') or
            (user_choice == 'Paper' and ai_choice == 'Rock') or
            (user_choice == 'Scissors' and ai_choice == 'Paper')
        ):
            return "You win!"
        else:
            return "AI wins!"

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()

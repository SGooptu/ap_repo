import tkinter as tk

class MancalaGame:
    def __init__(self):
        self.board = [4] * 14  # 6 pits for each player and 2 mancalas (index 6 and 13)
        self.current_player = 0  # 0 for player A, 1 for player B

    def move(self, pit_index):
        stones = self.board[pit_index]
        self.board[pit_index] = 0

        while stones > 0:
            pit_index = (pit_index + 1) % 14
            if pit_index != 13 or (self.current_player == 0 and pit_index == 6) or (self.current_player == 1 and pit_index == 13):
                self.board[pit_index] += 1
                stones -= 1

        self.check_game_over()
        self.switch_player()

    def check_game_over(self):
        if all(stones == 0 for stones in self.board[0:6]) or all(stones == 0 for stones in self.board[7:13]):
            self.board[6] += sum(self.board[0:6])
            self.board[13] += sum(self.board[7:13])
            for i in range(6):
                self.board[i] = 0
                self.board[i + 7] = 0

    def switch_player(self):
        if self.current_player == 0:
            self.current_player = 1
        else:
            self.current_player = 0

class MancalaGUI:
    def __init__(self, root, game):
        self.root = root
        self.root.title("Mancala")
        self.game = game
        self.buttons = []
        self.create_board()

    def create_board(self):
        for i in range(14):
            if i == 6:
                label_text = "Player 1's Mancala"
            elif i == 13:
                label_text = "Player 2's Mancala"
            elif i < 6:
                label_text = f"Player 1 - Pit {i + 1}"
            else:
                label_text = f"Player 2 - Pit {i - 6}"

            label = tk.Label(self.root, text=label_text, font=("Arial", 10, "bold"), pady=10, padx=10)
            label.grid(row=0, column=i)

            button = tk.Button(self.root, text=str(self.game.board[i]), width=3, height=2, font=("Arial", 14, "bold"), command=lambda i=i: self.on_pit_click(i), bg="#FFD700" if i in range(7) else "#FF5733", fg="#333333")
            button.grid(row=1, column=i, padx=5, pady=5)
            self.buttons.append(button)

    def update_board(self):
        for i in range(14):
            self.buttons[i].config(text=str(self.game.board[i]))

    def on_pit_click(self, pit_index):
        if (self.game.current_player == 0 and 0 <= pit_index <= 5) or (self.game.current_player == 1 and 7 <= pit_index <= 12):
            self.game.move(pit_index)
            self.update_board()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x300")
    root.configure(bg="#2E86C1")
    game = MancalaGame()
    gui = MancalaGUI(root, game)
    root.mainloop()
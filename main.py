import random
import tkinter as tk


class TicTacToe:
    def __init__(self):
        self.player_score = 0
        self.pc_score = 0
        self.window = None
        self.score_label = None
        self.win_label = None
        self.default_color = None
        self.squares_list = []

    def update_score(self):
        self.score_label.config(
            text=f"You: {self.player_score}     Computer: {self.pc_score}",
            font=("Arial", 24),
        )

    def check_winner(self, xo):
        xo_list = [i.cget("text") for i in self.squares_list]

        if (
            (xo_list[0] == xo and xo_list[1] == xo and xo_list[2] == xo)
            or (xo_list[3] == xo and xo_list[4] == xo and xo_list[5] == xo)
            or (xo_list[6] == xo and xo_list[7] == xo and xo_list[8] == xo)
            or (xo_list[0] == xo and xo_list[3] == xo and xo_list[6] == xo)
            or (xo_list[1] == xo and xo_list[4] == xo and xo_list[7] == xo)
            or (xo_list[2] == xo and xo_list[5] == xo and xo_list[8] == xo)
            or (xo_list[0] == xo and xo_list[4] == xo and xo_list[8] == xo)
            or (xo_list[2] == xo and xo_list[4] == xo and xo_list[6] == xo)
        ):
            return True

    def win_color(self, xo):
        xo_list = [i.cget("text") for i in self.squares_list]

        if xo_list[0] == xo and xo_list[1] == xo and xo_list[2] == xo:
            return [
                self.squares_list[0],
                self.squares_list[1],
                self.squares_list[2],
            ]

        elif xo_list[3] == xo and xo_list[4] == xo and xo_list[5] == xo:
            return [
                self.squares_list[3],
                self.squares_list[4],
                self.squares_list[5],
            ]

        elif xo_list[6] == xo and xo_list[7] == xo and xo_list[8] == xo:
            return [
                self.squares_list[6],
                self.squares_list[7],
                self.squares_list[8],
            ]

        elif xo_list[0] == xo and xo_list[3] == xo and xo_list[6] == xo:
            return [
                self.squares_list[0],
                self.squares_list[3],
                self.squares_list[6],
            ]

        elif xo_list[1] == xo and xo_list[4] == xo and xo_list[7] == xo:
            return [
                self.squares_list[1],
                self.squares_list[4],
                self.squares_list[7],
            ]

        elif xo_list[2] == xo and xo_list[5] == xo and xo_list[8] == xo:
            return [
                self.squares_list[2],
                self.squares_list[5],
                self.squares_list[8],
            ]

        elif xo_list[0] == xo and xo_list[4] == xo and xo_list[8] == xo:
            return [
                self.squares_list[0],
                self.squares_list[4],
                self.squares_list[8],
            ]

        elif xo_list[2] == xo and xo_list[4] == xo and xo_list[6] == xo:
            return [
                self.squares_list[2],
                self.squares_list[4],
                self.squares_list[6],
            ]

        else:
            return None

    def restart_game(self):
        self.win_label.config(text=" ")

        for i in self.squares_list:
            i.config(text=" ", font=("Arial", 50), state=tk.NORMAL)
            if self.default_color:
                i.config(bg=self.default_color)

        self.update_score()

    def lock_buttons(self):
        for i in self.squares_list:
            i.config(state=tk.DISABLED)

    def unlock_buttons(self):
        for i in self.squares_list:
            if i.cget("text") == " ":
                i.config(state=tk.NORMAL)

    def player_move(self, button):
        button.config(text="X", font=("Arial", 50), disabledforeground="Black")
        button.config(state=tk.DISABLED)
        win_buttons = self.win_color("X")

        if self.check_winner("X") == True:
            self.player_score += 1
            self.win_label.config(text="x wins!", font=("Arial", 32))
            self.update_score()
            self.lock_buttons()

            if win_buttons is not None:
                for i in win_buttons:
                    i.config(bg="#00FA9A")

            return True

        empty_buttons = [i for i in self.squares_list if i.cget("text") == " "]

        if not empty_buttons:
            self.win_label.config(text="Tie, no winner!", font=("Arial", 32))
            self.lock_buttons()

            for i in self.squares_list:
                i.config(bg="#FF0000")

            return True

        return False

    def pc_move(self):
        available_buttons = [i for i in self.squares_list if i.cget("text") == " "]

        if len(available_buttons) > 0:
            random_button = random.choice(available_buttons)
            random_button.config(
                text="O", font=("Arial", 50), disabledforeground="Black"
            )
            random_button.config(state=tk.DISABLED)

        win_buttons = self.win_color("O")

        if self.check_winner("O") == True:
            self.pc_score += 1
            self.win_label.config(text="o wins!", font=("Arial", 32))
            self.update_score()
            self.lock_buttons()

            if win_buttons is not None:
                for i in win_buttons:
                    i.config(bg="#00FA9A")

            return True

        if not [i for i in self.squares_list if i.cget("text") == " "]:
            self.win_label.config(text="Tie, no winner!", font=("Arial", 32))
            self.lock_buttons()

            for i in self.squares_list:
                i.config(bg="#FF0000")

            return True

        self.unlock_buttons()

    def button_click(self, button):
        if self.player_move(button) == False:
            self.lock_buttons()
            self.window.after(300, self.pc_move)

    def GUI(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe Almdrasa")
        self.window.geometry("500x600")

        frame = tk.Frame(self.window)
        frame.place(relx=0.5, anchor=tk.N)

        self.score_label = tk.Label(
            frame,
            text=f"You: {self.player_score}   Computer: {self.pc_score}",
            font=("Arial", 24),
        )
        self.score_label.grid(row=0, column=0)

        self.win_label = tk.Label(frame, text=" ", font=("Arial", 32))
        self.win_label.grid(row=1, column=0)

        restart_button = tk.Button(
            frame,
            command=self.restart_game,
            text="restart",
            font=("Arial", 16),
            width=10,
            height=1,
        )
        restart_button.grid(row=2, column=0)

        space_label = tk.Label(frame, text=" ", font=("Arial", 6))
        space_label.grid(row=3, column=0)

        frame_squares = tk.Frame(frame)
        frame_squares.grid(row=4, column=0)

        self.sqr1 = tk.Button(
            frame_squares, width=3, height=1, text=" ", font=("Arial", 50)
        )
        self.default_color = self.sqr1.cget("bg")
        self.sqr1.config(command=lambda btn=self.sqr1: self.button_click(btn))
        self.sqr1.grid(row=0, column=0)

        self.sqr2 = tk.Button(
            frame_squares, width=3, height=1, text=" ", font=("Arial", 50)
        )
        self.sqr2.config(command=lambda btn=self.sqr2: self.button_click(btn))
        self.sqr2.grid(row=0, column=1)

        self.sqr3 = tk.Button(
            frame_squares, width=3, height=1, text=" ", font=("Arial", 50)
        )
        self.sqr3.config(command=lambda btn=self.sqr3: self.button_click(btn))
        self.sqr3.grid(row=0, column=2)

        self.sqr4 = tk.Button(
            frame_squares, width=3, height=1, text=" ", font=("Arial", 50)
        )
        self.sqr4.config(command=lambda btn=self.sqr4: self.button_click(btn))
        self.sqr4.grid(row=1, column=0)

        self.sqr5 = tk.Button(
            frame_squares, width=3, height=1, text=" ", font=("Arial", 50)
        )
        self.sqr5.config(command=lambda btn=self.sqr5: self.button_click(btn))
        self.sqr5.grid(row=1, column=1)

        self.sqr6 = tk.Button(
            frame_squares, width=3, height=1, text=" ", font=("Arial", 50)
        )
        self.sqr6.config(command=lambda btn=self.sqr6: self.button_click(btn))
        self.sqr6.grid(row=1, column=2)

        self.sqr7 = tk.Button(
            frame_squares, width=3, height=1, text=" ", font=("Arial", 50)
        )
        self.sqr7.config(command=lambda btn=self.sqr7: self.button_click(btn))
        self.sqr7.grid(row=2, column=0)

        self.sqr8 = tk.Button(
            frame_squares, width=3, height=1, text=" ", font=("Arial", 50)
        )
        self.sqr8.config(command=lambda btn=self.sqr8: self.button_click(btn))
        self.sqr8.grid(row=2, column=1)

        self.sqr9 = tk.Button(
            frame_squares, width=3, height=1, text=" ", font=("Arial", 50)
        )
        self.sqr9.config(command=lambda btn=self.sqr9: self.button_click(btn))
        self.sqr9.grid(row=2, column=2)

        self.squares_list = [
            self.sqr1,
            self.sqr2,
            self.sqr3,
            self.sqr4,
            self.sqr5,
            self.sqr6,
            self.sqr7,
            self.sqr8,
            self.sqr9,
        ]

        self.window.mainloop()


start_game = TicTacToe()
start_game.GUI()

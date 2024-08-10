import tkinter as tk
from random import shuffle


class MyButton(tk.Button):

    def __init__(self, master, x, y, number=0, *args, **kwargs):
        super(MyButton, self).__init__(
            master,
            width=3,
            font='Calibri 15 bold',
            *args,
            **kwargs
        )
        self.x = x
        self.y = y
        self.number = number
        self.is_mine = False

    def __repr__(self):
        return f'MyButton{self.x} {self.y} {self.number} {self.is_mine}'


class MineSweeper:
    window = tk.Tk()
    ROW = 4
    COLUMN = 4
    MINES = 10

    def __init__(self):
        self.buttons = []
        for i in range(MineSweeper.ROW+2):
            temp = []
            for j in range(MineSweeper.COLUMN+2):
                btn = MyButton(MineSweeper.window, x=i, y=j)
                btn.config(command=lambda button=btn: self.click(button))
                temp.append(btn)
            self.buttons.append(temp)

    def click(self, clicked_button: MyButton):
        if clicked_button.is_mine:
            clicked_button.config(
                text='*',
                background='red',
                disabledforeground='black'
            )
        else:
            clicked_button.config(
                text=clicked_button.number,
                disabledforeground='black'
            )
        clicked_button.config(state='disabled')

    def create_widgets(self):
        for i in range(MineSweeper.ROW+2):
            for j in range(MineSweeper.COLUMN+2):
                btn = self.buttons[i][j]
                btn.grid(row=i, column=j)

    def open_all_buttons(self):
        for i in range(MineSweeper.ROW+2):
            for j in range(MineSweeper.COLUMN+2):
                btn = self.buttons[i][j]
                if btn.is_mine:
                    btn.config(
                        text='*',
                        background='red',
                        disabledforeground='black'
                    )
                else:
                    btn.config(
                        text=btn.number,
                        disabledforeground='black'
                    )

    def start(self):
        self.create_widgets()
        self.insert_mines()
        self.print_buttons()
        self.open_all_buttons()
        MineSweeper.window.mainloop()

    def print_buttons(self):
        for row_btn in self.buttons:
            print(row_btn)

    @staticmethod
    def get_mines_places():
        indexes = list(range(1, MineSweeper.COLUMN * MineSweeper.ROW + 1))
        shuffle(indexes)
        return indexes[:MineSweeper.MINES]

    def insert_mines(self):
        index_mines = self.get_mines_places()
        print(index_mines)
        count = 1
        for i in range(1, MineSweeper.ROW + 1):
            for j in range(1, MineSweeper.COLUMN + 1):
                btn = self.buttons[i][j]
                btn.number = count
                if btn.number in index_mines:
                    btn.is_mine = True
                count += 1


game = MineSweeper()
game.start()

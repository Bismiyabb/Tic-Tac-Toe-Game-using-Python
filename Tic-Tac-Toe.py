# TIC-TAC-TOE GAME
from tkinter import *
import random

def next_turn(row, column):
    global player
   
    if buttons[row][column]['text'] == "" and check_winner() is False:
        if player == players[0]:  # players[0] is "x"
            buttons[row][column]['text'] = player

            if check_winner() is False:  
                player = players[1]  
                label.config(text=(players[1] + " turn"))

            elif check_winner() is True:
                label.config(text=(players[0] + " wins"))

            elif check_winner() == "Tie":
                label.config(text=("It's a Tie"))

        else:  # for player [1]
            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + " turn"))

            elif check_winner() is True:
                label.config(text=(players[1] + " wins"))

            elif check_winner() == "Tie":
                label.config(text="It's a Tie")



def check_winner():
    # check all the win conditions and return true if there is a winner or false if there is not
    # horizontal win condition:
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
    # vertical win condition
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True
    # diagonal win condition
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    # other diagonal win condition
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:  
        return False


def empty_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True
def new_game():
    global player
    player = random.choice(players)
    label.config(text=(player + " turn"))
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")


window = Tk()

window.title("TIC-TAC-TOE")
players = ["x", "o"]  # list of players
player = random.choice(players)

# 2D LIST OF 9 BUTTONS - BOARD
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(text=player + " turn", font=("consolas", 40))  
label.pack(side="top")

reset_button = Button(text="Restart", font=("consolas", 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=("consolas", 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)


window.mainloop()

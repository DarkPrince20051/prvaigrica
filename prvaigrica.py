# moduli
from tkinter import *
import random
from tkinter import messagebox

# centriranje glavnog prozora u sredini
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")


# gumb za igru titactoe i pokretanje igrice
def open_tic_tac_toe():
    tic_tac_toe_window = Toplevel(main_window)
    tic_tac_toe_window.title("Tic Tac Toe")
    tic_tac_toe_window.resizable(False, False)
    tic_tac_toe_window.configure(bg="blue")

    center_window(tic_tac_toe_window, 1000, 690)

    players = ["X", "O"]
    player = random.choice(players)
    buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    x_wins = 0
    o_wins = 0

    def next_turn(row, column):
        nonlocal player

        if buttons[row][column]["text"] == "" and check_winner() is False:
            buttons[row][column]["text"] = player

            if check_winner() is False:
                player = players[1] if player == players[0] else players[0]
                label.config(text=("Player " + player + " Turn"))

    def check_winner():
        nonlocal x_wins, o_wins

        for row in range(3):
            if (
                buttons[row][0]["text"]
                == buttons[row][1]["text"]
                == buttons[row][2]["text"]
                != ""
            ):
                buttons[row][0].config(bg="green")
                buttons[row][1].config(bg="green")
                buttons[row][2].config(bg="green")
                if buttons[row][0]["text"] == "X":
                    x_wins += 1
                    x_wins_label.config(text="X Wins: {}".format(x_wins))
                else:
                    o_wins += 1
                    o_wins_label.config(text="O Wins: {}".format(o_wins))
                return True

        for column in range(3):
            if (
                buttons[0][column]["text"]
                == buttons[1][column]["text"]
                == buttons[2][column]["text"]
                != ""
            ):
                buttons[0][column].config(bg="green")
                buttons[1][column].config(bg="green")
                buttons[2][column].config(bg="green")
                if buttons[0][column]["text"] == "X":
                    x_wins += 1
                    x_wins_label.config(text="X Wins: {}".format(x_wins))
                else:
                    o_wins += 1
                    o_wins_label.config(text="O Wins: {}".format(o_wins))
                return True

        if (
            buttons[0][0]["text"]
            == buttons[1][1]["text"]
            == buttons[2][2]["text"]
            != ""
        ):
            buttons[0][0].config(bg="green")
            buttons[1][1].config(bg="green")
            buttons[2][2].config(bg="green")
            if buttons[0][0]["text"] == "X":
                x_wins += 1
                x_wins_label.config(text="X Wins: {}".format(x_wins))
            else:
                o_wins += 1
                o_wins_label.config(text="O Wins: {}".format(o_wins))
            return True

        elif (
            buttons[0][2]["text"]
            == buttons[1][1]["text"]
            == buttons[2][0]["text"]
            != ""
        ):
            buttons[0][2].config(bg="green")
            buttons[1][1].config(bg="green")
            buttons[2][0].config(bg="green")
            if buttons[0][2]["text"] == "X":
                x_wins += 1
                x_wins_label.config(text="X Wins: {}".format(x_wins))
            else:
                o_wins += 1
                o_wins_label.config(text="O Wins: {}".format(o_wins))
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
                if buttons[row][column]["text"] != "":
                    spaces -= 1
        return spaces != 0

    def new_game():
        nonlocal player
        player = "X"
        label.config(text=player + " Turn")

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(text="", bg="#F0F0F0")

    top_frame = Frame(tic_tac_toe_window, bg="green", width=1000, height=250)
    top_frame.place(x=0, y=0)

    game_title = Label(
        top_frame, bg="green", fg="white", text="Tic Tac Toe", font=("", 48)
    )
    game_title.place(x=320, y=0)

    label = Label(
        top_frame,
        text="Player " + player + " Turn",
        font=("arial", 50),
        bg="green",
        fg="white",
    )
    label.place(x=320, y=150)

    x_wins_label = Label(
        top_frame, text="X Wins: 0", font=("arial", 16), bg="green", fg="white"
    )
    x_wins_label.place(x=10, y=50)

    o_wins_label = Label(
        top_frame, text="O Wins: 0", font=("arial", 16), bg="green", fg="white"
    )
    o_wins_label.place(x=10, y=80)

    reset_button = Button(
        top_frame,
        text="Reset",
        font=("arial", 12),
        bg="black",
        fg="white",
        command=new_game,
    )
    reset_button.place(x=10, y=10)

    back_button = Button(
        top_frame,
        text="Back to Main Menu",
        font=("arial", 12),
        bg="black",
        fg="white",
        command=lambda: back_to_main_menu(tic_tac_toe_window),
    )
    back_button.place(x=120, y=10)

    bottom_frame = Frame(tic_tac_toe_window, bg="#FFFFFF", width=400, height=400)
    bottom_frame.place(x=265, y=300)

    for row in range(3):
        for column in range(3):
            buttons[row][column] = Button(
                bottom_frame,
                text="",
                font=("consolas", 40),
                width=5,
                height=1,
                command=lambda row=row, column=column: next_turn(row, column),
            )
            buttons[row][column].grid(row=row, column=column)


# pravila igre
def show_rules():
    rules_window = Toplevel(main_window)
    rules_window.title("Rules")
    rules_window.resizable(False, False)

    center_window(rules_window, 400, 200)

    rules_label = Label(
        rules_window,
        text="Tic Tac Toe Rules:\n\n1. Players take turns placing their symbol (X or O) in an empty cell.\n2. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.\n3. If all cells are filled and no player has won, the game is a tie.",
        justify=LEFT,
        wraplength=380,
    )
    rules_label.pack(padx=10, pady=10)

    back_button = Button(
        rules_window,
        text="Back to Main Menu",
        font=("arial", 12),
        bg="black",
        fg="white",
        command=lambda: back_to_main_menu(rules_window),
    )
    back_button.pack(pady=10)


# povratak na glavni prozor
def back_to_main_menu(window):
    window.destroy()


# funkcija za zatvaranje glavnog prozora
def confirm_exit():
    answer = messagebox.askyesno("Exit", "Do you really want to exit?")
    if answer:
        main_window.destroy()


# glavni prozor
main_window = Tk()
main_window.title("Tictactoe game")
main_window.configure(bg="blue")
main_window.geometry("400x200")
main_window.resizable(False, False)

center_window(main_window, 400, 200)

play_button = Button(
    main_window, text="Play Tic Tac Toe", font=("arial", 12), command=open_tic_tac_toe
)
play_button.pack(pady=20)

rules_button = Button(main_window, text="Rules", font=("arial", 12), command=show_rules)
rules_button.pack(pady=20)

exit_button = Button(main_window, text="Exit", font=("arial", 12), command=confirm_exit)
exit_button.pack(pady=20)

main_window.mainloop()

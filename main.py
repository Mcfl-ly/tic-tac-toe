import tkinter as tk
from functools import partial
window = tk.Tk()

window.title("Tic Tac Toe")
window.config(padx=20, pady=20)

turns = ['O', 'X']

text = tk.Canvas(window, width=250, height=50)
text_id = text.create_text(125, 25, text=f'{turns[1]} turn.', font=("Arial", 24))
text.grid(row=0, column=0, columnspan=3,pady=20, sticky='ew')
for i in range(3):
    window.columnconfigure(i, weight=1)
    window.rowconfigure(i + 1, weight=1)

buttons = []
t_time = 1
def marcar(indice):
    global t_time
    if t_time % 2 == 0:
        new_turn = 'O'
        color = 'cyan'
        text.itemconfig(text_id, text=f'X turn.')
    elif t_time % 2 == 1:
        new_turn = 'X'
        color = 'yellow'
        text.itemconfig(text_id, text=f'O turn.')
    buttons[indice].config(text=new_turn, font=("Arial", 20), bg=color)
    t_time += 1
    check(buttons, new_turn)


def check(buttons, turn):
    player1 = []
    player2 = []
    cond_win = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontais
                (0, 3, 6), (1, 4, 7), (2, 5, 8),  # verticais
                (0, 4, 8), (2, 4, 6)  # diagonais
                ]
    for i, btn in enumerate(buttons):
        if btn['text'] == 'X':
            player1.append(i)
            # print(i, btn['text'])
        elif btn['text'] == 'O':
            player2.append(i)
    resultado_p1 = any(all(num in player1 for num in tupla) for tupla in cond_win)
    resultado_p2 = any(all(num in player2 for num in tupla) for tupla in cond_win)
    if resultado_p1 is True:
        print(f'Player 1 wins!')
        text.itemconfig(text_id, text=f'Player 1 wins!')
        quit_text = tk.Label(text="clique para fechar", font=("Arial", 15))
        quit_text.grid(row=4, column=0, columnspan=3,sticky='ew')
        window.bind("<Button-1>", fechar_janela)

    elif resultado_p2 is True:
        print(f'Player 2 wins!')
        text.itemconfig(text_id, text=f'Player 2 wins!')
        quit_text = tk.Label(text="clique para fechar", font=("Arial", 15))
        quit_text.grid(row=4, column=0, columnspan=3,sticky='ew')
        window.bind("<Button-1>", fechar_janela)

def fechar_janela(event):
    window.destroy()




for r in range(3):
    for c in range(3):
        indice = r * 3 + c
        btn = tk.Button(window, font=("Arial", 24), command=partial(marcar, indice))
        btn.grid(row=r+1, column=c, sticky="nsew")
        buttons.append(btn)

window.mainloop()



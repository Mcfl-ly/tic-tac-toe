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
    print(buttons[indice]['text'])

for r in range(3):
    for c in range(3):
        indice = r * 3 + c
        btn = tk.Button(window, font=("Arial", 24), command=partial(marcar, indice))
        btn.grid(row=r+1, column=c, sticky="nsew")
        buttons.append(btn)

window.mainloop()



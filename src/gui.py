import tkinter as tk
import board
import game

# create window and icon
window = tk.Tk()
window.title("Pydoku")
window.resizable(True, True)
window.iconbitmap('./assets/icon.ico')
window.configure(bg='#1E1E1E')

#difficulty selection
diffSelectLabel = tk.Label(window, text="Select difficulty:")
diffSelectLabel.configure(bg='#1E1E1E', fg='#D5D5D5')
diffSelectLabel.grid(row=0, column=0)

diffSelection = tk.StringVar(window, "Easy")
diffRow = 0
for difficulty in board.difficulty:
    tk.Radiobutton(window, text = difficulty['level'],
                   variable=diffSelection, value=difficulty['level'],
                   background='#1E1E1E', foreground='#D5D5D5'
                   ).grid(row=diffRow, column=1, sticky=tk.W)
    diffRow += 1

cellInput = []
for i in range(1, (len(board.cells)+1)):
    cellInput.append(tk.Entry(window, width=3, justify='center', bg='#1E1E1E', fg='#D5D5D5'))
    cellInput[i-1].grid(row=board.cells[i]['row']+2, column=(board.cells[i]['column']+1))

window.mainloop()

def newGame():
    pass
import tkinter
import random

root = tkinter.Tk()
root.geometry('600x600')
root.title('Roll Dice')

label = tkinter.Label(root, text='', font=('Helvetica', 260))
def roll_dice1():
    dice1 = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.configure(text=f'{random.choice(dice1)} ')
    label.place(x=100,y=50)
button1 = tkinter.Button(root, text='roll dice 1', foreground='blue',command=roll_dice1)
button1.place(x=190, y=50)

label2 = tkinter.Label(root, text='', font=('Helvetica', 260))
def roll_dice2():
    dice2 = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label2.configure(text=f'{random.choice(dice2)}')
    label2.place(x=400,y=50)
button2 = tkinter.Button(root, text='roll dice 2', foreground='red',command=roll_dice2)
button2.place(x=490, y=50)

label3 = tkinter.Label(root, text='', font=('Helvetica', 260))
def roll_dice3():
    dice3 = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label3.configure(text=f'{random.choice(dice3)} ')
    label3.place(x=700,y=50)
button3 = tkinter.Button(root, text='roll dice 3', foreground='green',command=roll_dice3)
button3.place(x=790, y=50)

label4 = tkinter.Label(root, text='', font=('Helvetica', 260))
def roll_dice4():
    dice4 = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label4.configure(text=f'{random.choice(dice4)}')
    label4.place(x=1000,y=50)
button4 = tkinter.Button(root, text='roll dice 4', foreground='purple',command=roll_dice4)
button4.place(x=1090, y=50)

root.mainloop()


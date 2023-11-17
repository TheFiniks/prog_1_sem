from tkinter import *
from tkinter import ttk


def calculate(*args):
    try:
        s_color = color.get()
        canvas.itemconfig(rec, fill=s_color)
        Red = int(s_color[1:3], 16)
        Green = int(s_color[3:5], 16)
        Blue = int(s_color[5:], 16)

        compl_Red = str(hex(255 - Red))[2:]
        compl_Green = str(hex(255 - Green))[2:]
        compl_Blue = str(hex(255 - Blue))[2:]

        if compl_Red == '0': compl_Red = '00'
        if compl_Green == '0': compl_Green = '00'
        if compl_Blue == '0': compl_Blue = '00'

        full_compl_color = f'#{compl_Red}{compl_Green}{compl_Blue}'
        canvas.itemconfig(compl_rec, fill=full_compl_color)
        compl_color.set(full_compl_color)


    except Exception as e:
        compl_color.set('Error!')


root = Tk()
root.title('Complementary color')
root.geometry('600x350')

color = StringVar()
compl_color = StringVar()

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, stick='wens')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text='Enter color in hex:', font=('Arial 16 bold'))
entry = ttk.Entry(mainframe, justify='center', width='50', textvariable=color)
ttk.Button(mainframe, text='Output complementary color', width='50', command=calculate)

canvas = Canvas(mainframe, width=600, height=100)
ttk.Label(root, textvariable=color, font=('Arial 16 bold')).place(x=180, y=230)
rec = canvas.create_rectangle(150, 20, 150 + 150, 20 + 100, outline='')

ttk.Label(root, textvariable=compl_color, font=('Arial 16 bold')).place(x=340, y=230)
compl_rec = canvas.create_rectangle(300, 20, 300 + 150, 20 + 100, outline='')

for child in mainframe.winfo_children():
    child.grid_configure(padx=0, pady=5)

root.bind('<Return>', calculate)
entry.focus()

root.mainloop()

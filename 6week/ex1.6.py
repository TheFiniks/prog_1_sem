import tkinter as tk

win = tk.Tk()
win.title('Calculator')
win['bg'] = '#33ffe6'
win.geometry('223x183+100+200')


def add_digit(digit):
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc.delete(0, 'end')
    calc.insert(0, value + str(digit))


def add_operation(operation):
    value = calc.get()
    if value[-1] in ['+', '-', '*', '/']:
        value = value[:-1]
    calc.delete(0, 'end')
    calc.insert(0, value + operation)


def calculate():
    value = calc.get()
    calc.delete(0, 'end')
    calc.insert(0, eval(value))


def clear():
    calc.delete(0, 'end')
    calc.insert(0, '0')


calc = tk.Entry(win, font=('Arial', 15))
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=4, stick='we')
tk.Button(text='1', bd=5, font=('Arial', 13), command=lambda: add_digit(1)).grid(row=1, column=0, stick='wens')
tk.Button(text='2', bd=5, font=('Arial', 13), command=lambda: add_digit(2)).grid(row=1, column=1, stick='wens')
tk.Button(text='3', bd=5, font=('Arial', 13), command=lambda: add_digit(3)).grid(row=1, column=2, stick='wens')
tk.Button(text='4', bd=5, font=('Arial', 13), command=lambda: add_digit(4)).grid(row=2, column=0, stick='wens')
tk.Button(text='5', bd=5, font=('Arial', 13), command=lambda: add_digit(5)).grid(row=2, column=1, stick='wens')
tk.Button(text='6', bd=5, font=('Arial', 13), command=lambda: add_digit(6)).grid(row=2, column=2, stick='wens')
tk.Button(text='7', bd=5, font=('Arial', 13), command=lambda: add_digit(7)).grid(row=3, column=0, stick='wens')
tk.Button(text='8', bd=5, font=('Arial', 13), command=lambda: add_digit(8)).grid(row=3, column=1, stick='wens')
tk.Button(text='9', bd=5, font=('Arial', 13), command=lambda: add_digit(9)).grid(row=3, column=2, stick='wens')
tk.Button(text='0', bd=5, font=('Arial', 13), command=lambda: add_digit(0)).grid(row=4, column=0, stick='wens')
tk.Button(text='=', bd=5, font=('Arial', 13), command=calculate).grid(row=4, column=2, stick='wens')
tk.Button(text='+', bd=5, font=('Arial', 13), command=lambda: add_operation('+')).grid(row=1, column=3, stick='wens')
tk.Button(text='-', bd=5, font=('Arial', 13), command=lambda: add_operation('-')).grid(row=2, column=3, stick='wens')
tk.Button(text='*', bd=5, font=('Arial', 13), command=lambda: add_operation('*')).grid(row=3, column=3, stick='wens')
tk.Button(text='/', bd=5, font=('Arial', 13), command=lambda: add_operation('/')).grid(row=4, column=3, stick='wens')
tk.Button(text='C', bd=5, font=('Arial', 13), command=clear).grid(row=4, column=1, stick='wens')
win.mainloop()


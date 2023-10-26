import tkinter as tk


def get_result():
    m = weight.get()
    h = height.get()
    I = float(m) / float(h) ** 2 * 1e4
    tk.Label(text=f'Ваш индекс массы тела: {I:.{4}}', font=('Arial', 15)).grid(row=5, column=0, columnspan=2, stick='w')
    if I <= 16:
        txt = 'Выраженный дефицит массы тела'
    elif I > 16 and I <= 18.5:
        txt = 'Недостаточная масса тела'
    elif I > 18.5 and I <= 25:
        txt = 'Норма'
    elif I > 25 and I <= 30:
        txt = 'Избыточная масса тела'
    elif I > 30 and I <= 35:
        txt = 'Ожирение 1 степени'
    elif I > 35 and I <= 40:
        txt = 'Ожирение 2 степени'
    else:
        txt = 'Ожирение 3 степени'
    tk.Label(text=f'Результат: {txt}', font=('Arial', 15)).grid(row=6, column=0, columnspan=2, stick='w')


win = tk.Tk()
win.title('IMT')
win.geometry('400x300+100+200')
tk.Label(text='Ваш вес, кг', font=('Arial', 15)).grid(row=0, column=0, columnspan=2, stick='w')
weight = tk.Entry(win, font=('Arial', 15))
weight.grid(row=1, column=0, columnspan=3, stick='we')
tk.Label(text='Ваш рост, см', font=('Arial', 15)).grid(row=2, column=0, columnspan=2, stick='w')
height = tk.Entry(win, font=('Arial', 15))
height.grid(row=3, column=0, columnspan=2, stick='we')
tk.Button(text='Готово', font=('Arial', 15), command=get_result).grid(row=4, column=0, columnspan=2, stick='we')
win.mainloop()

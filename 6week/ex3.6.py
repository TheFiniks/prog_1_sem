from tkinter import *
from tkinter import ttk
from random import randint
import csv

with open('imdb_top_250.csv', encoding='utf-8') as f:
    data = list(csv.reader(f, delimiter=',', quotechar='"'))[1:]
    films = [[x[1], x[3]] for x in data[1:]]
    genres_l = [x[3].split('|') for x in data[1:]]
    genres = []
    for complex_g in genres_l:
        for g in complex_g:
            if g.strip() not in genres: genres.append(g.strip())
    print(genres)


def find(*args):
    try:
        g = genre.get()
        good_films = [x[0] for x in films if g in x[1]]
        number = randint(0, len(good_films) - 1)
        film.set(good_films[number])
    except Exception as e:
        film.set('This genre not exists')


root = Tk()
root.title('Films generator')
root.geometry('750x260')

genre = StringVar()
film = StringVar()

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, stick='wens')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

genres_string = ''
for i in range(len(genres)):
    if i % 10 == 0 and i > 0:
        genres_string += '\n'
    if i != len(genres) - 1:
        genres_string += genres[i] + ', '
    else:
        genres_string += genres[i] + '.'

ttk.Label(mainframe, text='Genres:', font=('Arial 16 bold'))
ttk.Label(mainframe, text=genres_string, font=('Arial 12 bold'))

ttk.Label(mainframe, text='Enter genre: ', font=('Arial 16 bold'))
entry = ttk.Entry(mainframe, justify='center', width='50', textvariable=genre)
ttk.Button(mainframe, text='Show film!', width='50', command=find)
ttk.Label(mainframe, textvariable=film, font=('Arial 12 bold'))

for child in mainframe.winfo_children():
    child.grid_configure(padx=50, pady=5)

root.bind('<Return>', find)
entry.focus()

root.mainloop()

from random import randint, choice
from tkinter import *
import time

WIDTH = 1280
HEIGHT = 640


class Ball:
    def __init__(self, x_start, y_start):
        speeds = [i / 20 for i in range(-50, 50)]
        self.color = '#' + (str(hex(randint(1, 16000000))) + '000000')[2:8]
        speeds.remove(0)
        self.R = randint(20, 70)
        self.x, self.y = x_start, y_start
        self.dx, self.dy = (
            choice(speeds), choice(speeds))
        self.ball_id = canvas.create_oval(self.x - self.R,
                                          self.y - self.R,
                                          self.x + self.R,
                                          self.y + self.R, fill=self.color)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > WIDTH or self.x - self.R <= 0:
            self.dx = -self.dx
        if self.y + self.R > HEIGHT or self.y - self.R <= 0:
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)

    def delete(self):
        canvas.delete(self.ball_id)


class Ball1:
    def __init__(self, x_start, y_start, y_speed, x_speed, color, r):
        self.color = color
        self.R = r * 0.5
        self.x, self.y = x_start, y_start
        self.dx, self.dy = (
            x_speed, y_speed)
        self.ball_id = canvas.create_oval(self.x - self.R,
                                          self.y - self.R,
                                          self.x + self.R,
                                          self.y + self.R, fill=self.color)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > WIDTH or self.x - self.R <= 0:
            self.dx = -self.dx
        if self.y + self.R > HEIGHT or self.y - self.R <= 0:  # отр
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)

    def delete(self):
        canvas.delete(self.ball_id)


def click_handler(event):
    balls.append(Ball(event.x, event.y))


def click_handler1(event):
    for i in balls:
        if (event.x - i.x) ** 2 + (event.y - i.y) ** 2 < i.R ** 2:
            for j in range(-1, 2, 2):
                balls.append(Ball1(i.x, i.y, i.dx + j * randint(1, 9) / 3, i.dy + j * randint(1, 9) / 2,
                                   '#' + str(hex(randint(0, 15))[2:]) + i.color[2:], i.R))
            balls.remove(i)
            i.delete()
            break


def del_randoms(event):
    temp = []
    for i in balls:
        if i.R < 30:
            i.delete()
            temp.append(i)
    for i in temp:
        balls.remove(i)


def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(10, tick)


if __name__ == "__main__":
    root = Tk()
    root.geometry(f'{WIDTH}x{HEIGHT}')
    canvas = Canvas(root, width=WIDTH, height=HEIGHT)
    canvas.pack()
    canvas.bind('<Button-1>', click_handler)
    canvas.bind('<Button-3>', click_handler1)
    canvas.bind("<Shift-Button-1>", del_randoms)
    balls = [Ball(500, 500)]
    tick()
    root.mainloop()


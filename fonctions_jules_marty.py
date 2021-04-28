import tkinter as tk


def screen_test():
    root = tk.Tk()
    screen = tk.Canvas(root, width=800, height=800, bg='black')
    screen.grid(column=0, row=0)

    # points
    screen.create_rectangle(0, 0, 40, 40, fill='red')
    screen.create_rectangle(380, 0, 420, 40, fill='red')
    screen.create_rectangle(760, 0, 800, 40, fill='red')
    screen.create_rectangle(0, 380, 40, 420, fill='red')
    screen.create_rectangle(380, 380, 420, 420, fill='red')
    screen.create_rectangle(760, 380, 800, 420, fill='red')
    screen.create_rectangle(0, 760, 40, 800, fill='red')
    screen.create_rectangle(380, 760, 420, 800, fill='red')
    screen.create_rectangle(760, 760, 800, 800, fill='red')
    # lignes horizontales
    screen.create_rectangle(50, 0, 370, 40, fill='red')
    screen.create_rectangle(430, 0, 750, 40, fill='red')
    screen.create_rectangle(50, 380, 370, 420, fill='red')
    screen.create_rectangle(430, 380, 750, 420, fill='red')
    screen.create_rectangle(50, 760, 370, 800, fill='red')
    screen.create_rectangle(430, 760, 750, 800, fill='red')
    # lignes verticales
    screen.create_rectangle(0, 50, 40, 370, fill='red')
    screen.create_rectangle(0, 430, 40, 750, fill='red')
    screen.create_rectangle(380, 50, 420, 370, fill='red')
    screen.create_rectangle(380, 430, 420, 750, fill='red')
    screen.create_rectangle(760, 50, 800, 370, fill='red')
    screen.create_rectangle(760, 430, 800, 750, fill='red')
    # diagonales
    screen.create_rectangle()

    screen.bind('<Button-1>', mouseover_item)
    root.mainloop()


def mouseover_item(event):
    x, y = event.x, event.y
    print(x, y)


screen_test()

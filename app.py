import tkinter as tk


def position(width, height):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # pozycja na ekranie
    x = -10
    y = 1000
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))


root = tk.Tk()
position(1920, 20)
root.wm_attributes('-fullscreen', 'True')
root.attributes('-topmost',1)

root.mainloop()

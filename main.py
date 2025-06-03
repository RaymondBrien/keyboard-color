import tkinter as tk

import src.keyboard as keyboard
import src.visualiser as visualiser

REFRESH_TIME = 1


def update_from_input(canvas):
    try:
        rgb = keyboard.run(input())
        visualiser.update_color(canvas=canvas, rgb=rgb)
    except EOFError:
        return
    canvas.after(REFRESH_TIME, lambda: update_from_input(canvas))


def main():
    # set up canvas
    root = tk.Tk()
    root.title('Real time color rgb')
    canvas = tk.Canvas(root, width=200, height=200)
    canvas.pack()

    # Start the update cycle
    update_from_input(canvas)
    root.mainloop()


if __name__ == "__main__":
    main()
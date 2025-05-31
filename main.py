import tkinter as tk

import keyboard
import visualiser

REFRESH_TIME = 1


def main():
    # set up canvas
    root = tk.Tk()
    root.title('Real time color rgb')
    canvas = tk.Canvas(root, width=20, height=200)


    while True:
        rgb = keyboard.run(input())
        visualiser.update_color(canvas=canvas, rgb=rgb)
        root.after(REFRESH_TIME, visualiser.update_color(canvas=canvas, rgb=rgb))
        root.mainloop()

if __name__ == "__main__":
    main()
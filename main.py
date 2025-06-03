import tkinter as tk

import src.keyboard as keyboard
import src.visualiser as visualiser

def on_key_press(event, canvas):
    try:
        rgb = keyboard.run(event.char)
        visualiser.update_color(canvas=canvas, rgb=rgb)
    except Exception as e:
        print(f"Error: {e}")


def main():
    # set up canvas
    root = tk.Tk()
    root.title('Real time color rgb')
    canvas = tk.Canvas(root, width=200, height=200)
    canvas.pack()

    # Bind key press event
    root.bind('<Key>', lambda event: on_key_press(event, canvas))

    root.mainloop()


if __name__ == "__main__":
    main()
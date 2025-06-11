import tkinter as tk

import src.keyboard as keyboard
import src.visualiser as visualiser
from src.tuner_audio.audio_analyzer import AudioAnalyzer
from src.tuner_audio.threading_helper import ProtectedList


def update_color(event, canvas):
    try:
        rgb = keyboard.run(event)
        # rgb = keyboard.run(event.char)  # TODO differentiate for keyboard input vs live audio?
        visualiser.update_color(canvas=canvas, rgb=rgb)
    except Exception as e:
        print(f"Error: {e}")

def process_audio(root, canvas, queue, audio):
    q_data = queue.get()
    if q_data is not None:
        note_name = audio.frequency_to_note_name(q_data, 440)  # TODO have as arg (could change to 442 etc)
        print("loudest frequency:", q_data, "nearest note:", note_name)
        update_color(note_name, canvas)

    # Schedule the next check
    # TODO change time to be dynamic
    root.after(500, lambda: process_audio(root, canvas, queue, audio))

def main():
    # Set up canvas
    root = tk.Tk()
    root.title('Real time color rgb')
    canvas = tk.Canvas(root, width=200, height=200)
    canvas.pack()

    # Initialize audio processing
    queue = ProtectedList()
    audio = AudioAnalyzer(queue)
    audio.start()

    # Start the audio processing loop
    process_audio(root, canvas, queue, audio)

    # Bind key press event for keyboard input
    root.bind('<Key>', lambda event: update_color(event, canvas))

    # Start the Tkinter event loop
    root.mainloop()

    # TODO only enable for keyboard inputs
    # Bind key press event
    # root.bind('<Key>', lambda event: update_color(event, canvas))



if __name__ == "__main__":
    main()
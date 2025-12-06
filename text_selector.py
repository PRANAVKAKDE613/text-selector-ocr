import time
import ctypes
import cv2
import numpy as np
import pytesseract
import pyperclip
import keyboard
from PIL import ImageGrab
from plyer import notification
import winsound
import tkinter as tk

# ---------------- DPI AWARE (IMPORTANT ON WINDOWS) ----------------
try:
    ctypes.windll.user32.SetProcessDPIAware()
except Exception:
    pass

# ---------------- TESSERACT PATH ----------------
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# ---------------- GLOBALS ----------------
root = None
canvas = None

start_x_canvas = start_y_canvas = 0
start_x_screen = start_y_screen = 0


# ---------------- OCR ----------------
def process_selection(x1, y1, x2, y2):
    """Grab selected region, run OCR, copy to clipboard."""
    time.sleep(0.1)

    image = ImageGrab.grab(bbox=(x1, y1, x2, y2), all_screens=True)

    gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    text = pytesseract.image_to_string(gray, config="--oem 3 --psm 6")
    text = "\n".join(line.strip() for line in text.splitlines() if line.strip())

    if text:
        pyperclip.copy(text)
        try:
            notification.notify(
                title="Text Extracted",
                message="Copied to clipboard",
                timeout=2
            )
        except Exception:
            pass

        try:
            winsound.Beep(1000, 150)
        except Exception:
            pass

        print("Copied text:\n", text)
    else:
        print("No text detected.")


# ---------------- MOUSE EVENTS ----------------
def on_press(event):
    """Mouse down: record start position (canvas + screen coords)."""
    global start_x_canvas, start_y_canvas, start_x_screen, start_y_screen

    start_x_canvas = event.x
    start_y_canvas = event.y

    start_x_screen = event.x + root.winfo_rootx()
    start_y_screen = event.y + root.winfo_rooty()


def on_drag(event):
    """While dragging: draw the red rectangle."""
    canvas.delete("rect")
    canvas.create_rectangle(
        start_x_canvas,
        start_y_canvas,
        event.x,
        event.y,
        outline="red",
        width=3,
        tags="rect"
    )


def on_release(event):
    """Mouse up: compute end coords, close overlay, run OCR."""
    end_x_screen = event.x + root.winfo_rootx()
    end_y_screen = event.y + root.winfo_rooty()

    # Close overlay window
    root.destroy()

    x1 = min(start_x_screen, end_x_screen)
    y1 = min(start_y_screen, end_y_screen)
    x2 = max(start_x_screen, end_x_screen)
    y2 = max(start_y_screen, end_y_screen)

    if x1 == x2 or y1 == y2:
        print("Zero-size selection, ignoring.")
        return

    process_selection(x1, y1, x2, y2)


# ---------------- OVERLAY ----------------
def start_selection():
    """Create fullscreen transparent overlay and let user draw a box."""
    global root, canvas

    print("Selection started...")

    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)
    root.attributes("-alpha", 0.3)
    root.configure(bg="black")

    canvas = tk.Canvas(root, bg="black", cursor="cross", highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)

    canvas.bind("<ButtonPress-1>", on_press)
    canvas.bind("<B1-Motion>", on_drag)
    canvas.bind("<ButtonRelease-1>", on_release)

    # ESC cancels selection
    def cancel(event=None):
        print("Selection cancelled.")
        root.destroy()

    root.bind("<Escape>", cancel)

    # This blocks until user finishes or cancels
    root.mainloop()


# ---------------- MAIN LOOP ----------------
if __name__ == "__main__":
    print("Text Selector running.")
    print("Press Ctrl + Caps Lock to select text.\n")

    while True:
        # Wait for hotkey
        keyboard.wait("ctrl+caps lock")
        # Launch selection overlay (blocks until done)
        start_selection()

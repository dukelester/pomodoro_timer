
import tkinter as tk
from tkinter import PhotoImage
from timer import PomodoroTimer
from constants import GREEN, YELLOW, FONT_NAME
import os

# Timer instance
timer_logic = PomodoroTimer(work_min=1, short_break_min=5, long_break_min=20)
timer = None


def reset_timer():
    global timer
    window.after_cancel(timer)
    time_text, title_text, marks = timer_logic.reset_timer()
    canvas.itemconfig(timer_text, text=time_text)
    title_label.config(text=title_text)
    check_marks.config(text=marks)


def start_timer():
    global timer
    duration, title_text, color = timer_logic.get_next_timer()
    title_label.config(text=title_text, fg=globals()[color])
    count_down(duration)


def count_down(count):
    global timer
    formatted_time = timer_logic.format_time(count)
    canvas.itemconfig(timer_text, text=formatted_time)
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check_marks.config(text="✔" * (timer_logic.reps // 2))


# UI Setup
window = tk.Tk()
window.title('Pomodoro Timer')
window.config(padx=100, pady=50, bg=YELLOW)

# Title Label
title_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45))
title_label.grid(column=1, row=0)

# Timer Canvas
ASSET_DIR = os.path.join(os.path.dirname(__file__), 'assets')
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=os.path.join(ASSET_DIR, 'tomato.png'))
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Buttons
start_button = tk.Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)
stop_button = tk.Button(text="Reset", command=reset_timer)
stop_button.grid(column=2, row=2)

# Check Marks
check_marks = tk.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30))
check_marks.grid(column=1, row=3)

window.mainloop()

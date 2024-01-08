from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    checkmarks_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    window.bell()

    if reps%8 == 0:
        duration = LONG_BREAK_MIN * 60
        timer_label.config(text="Long break", fg=RED)
    elif reps%2 == 1:
        timer_label.config(text="WORK WORK WROK", fg=GREEN)
        duration = WORK_MIN * 60
    else:
        duration = SHORT_BREAK_MIN * 60
        timer_label.config(text="shorty break", fg=PINK)
    count_down(duration)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global timer

    minutes = str(math.floor(count/60)).zfill(2)
    seconds = str(count%60).zfill(2)

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        if reps%2==1: # just finished a work session
            checks = checkmarks_label.cget("text")
            checks = checks + "✓"
            checkmarks_label.config(text=checks)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
# window set up
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# timer label
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25))

# start button
start_button = Button(text="Start", command=start_timer, highlightthickness=0)

# reset button
reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)

# tomato set up
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 50, "bold"))

# checkmark label
checkmarks_label = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, 'bold'))

# grid it up
timer_label.grid(row=1, column=2)
canvas.grid(row=2, column=2)
start_button.grid(row=3, column=1)
reset_button.grid(row=3, column=3)
checkmarks_label.grid(row=4, column=2)

window.mainloop()
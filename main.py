from tkinter import *
# * imports everything from the specified library
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
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60) # returns largest whole number that's less than specified number(rounds down)
    count_sec = count % 60 # returns remainder
    if count_sec == 0:
        count_sec = "0"
        # dynamic typing - allows you to change data type in a variable. In our case, count_sec
        # if a variable is STRONGLY typed, then it has a set data type
    if int(count_sec) < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}") # use itemconfig for canvas, instead of config for window
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW) # adjust once canvas is on screen

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) # Canvas is a widget
# set canvas to same size as image size
# Canvas allows things to overlap
# highlightthickness=0 removes boarder around canvas
tomato_img = PhotoImage(file="tomato.png") # converts png to photo image - will need file path if not in same folder
canvas.create_image(100, 112, image=tomato_img) # width 100, height 200 puts image in center of canvas
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")) # screen starts 0, 0 from top left corner
canvas.grid(column=1, row=1) # puts canvas on the window

# title label
title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold")) # use fg= to colour text
title_label.grid(column=1, row=0)

# tick labels
check_marks = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold")) # copy the check mark across from wikipedia
check_marks.grid(column=1, row=3)

# start button
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)
# can use highlightthickness=0 to remove white boarders if there are any

# reset button
reset_button = Button(text="Reset", command=reset_timer) # command=reset_timer
reset_button.grid(column=2, row=2)

window.mainloop()

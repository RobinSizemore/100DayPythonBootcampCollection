import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
WHITE = "#EEEEEE"
GREY = "#686D76"
DARKGREY = "#373A40"
ORANGE = "#DC5F00"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- GLOBAL VARIABLES -------------------------- #
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def restart_timer():
    global reps
    global timer
    reps = 0
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text=f"00:00")
    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    if reps % 2 == 0:  # 0, 2, 4, 6
        time = WORK_MIN
        timer_label.config(text="Work")
        reps += 1
    elif reps % 7 == 0:  # 7
        time = LONG_BREAK_MIN
        timer_label.config(text="LONG BREAK")
        reps = 0
    else:  # 1, 3, 5
        time = SHORT_BREAK_MIN
        timer_label.config(text="Short Break")
        reps += 1
    countdown(time * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    minutes = int(count/60)
    secs = int(count % 60)
    canvas.itemconfig(timer_text, text=f"{minutes}:{secs:02d}")
    if (count > 0):
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        global reps
        checks = int((reps + 1) / 2)
        check_text = "✔"
        check_marks.config(text=check_text * checks)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=GREY)

canvas = tkinter.Canvas(width=200, height=224, bg=GREY, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(200, 0, image=tomato_img, anchor="ne")
timer_text = canvas.create_text(100, 130, text="00:00", fill=WHITE, font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

timer_label = tkinter.Label(text="Timer", fg=WHITE, bg=GREY, font=(FONT_NAME, 30, "bold"))
timer_label.grid(column=1, row=0)

start_btn = tkinter.Button(text="Start", fg=ORANGE, bg=DARKGREY, highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = tkinter.Button(text="Reset", fg=ORANGE, bg=DARKGREY, highlightthickness=0, command=restart_timer)
reset_btn.grid(column=2, row=2)

check_marks = tkinter.Label(text="", fg=WHITE, bg=GREY)
check_marks.grid(column=1, row=3)

window.mainloop()

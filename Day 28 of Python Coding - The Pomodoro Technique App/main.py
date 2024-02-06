from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer_num = 0
timer = ""


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global timer_num
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")
    timer_num = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global timer_num

    timer_num += 1
    if timer_num % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN*60)
    elif timer_num % 2 == 1:
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN*60)
    elif timer_num % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN*60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer
    count_min = int(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min}:{"{:02d}".format(count_sec)}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        checkmarks = ""
        work_sessions = int(timer_num / 2)
        for no_of_checkmarks in range(work_sessions):
            checkmarks += "✓"
            checkmark_label.config(text=checkmarks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Technique Timer!")
window.config(padx=100, pady=50, bg=YELLOW)

# Setting up canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text=f"00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.pack()

# Setting up timer label
timer_label = Label(text="Timer", font=(FONT_NAME, 30, "normal"), fg=GREEN, bg=YELLOW)
timer_label.place(x=40, y=-50)

# Setting up tick label
checkmark_label = Label(font=("Arial", 20, "normal"), fg=GREEN, bg=YELLOW)
checkmark_label.place(x=30, y=230)

# Setting up buttons
start_button = Button(text="Start", font=("Arial", 10, "normal"), command=start_timer)
start_button.place(x=-50, y=200)

reset_button = Button(text="Reset", font=("Arial", 10, "normal"), command=reset_timer)
reset_button.place(x=210, y=200)

window.mainloop()

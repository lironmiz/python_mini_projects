import tkinter
import math

# CONSTANTS

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Global Variables

reps = 0
timer = None


def main():
    global window, canvas, title_label, check_marks, timer_text

    # UI SETUP

    window = tkinter.Tk()
    window.title("Pomodoro")
    window.config(padx=100, pady=50, bg=YELLOW)

    # Labels

    title_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
    title_label.grid(column=1, row=0)

    check_marks = tkinter.Label(fg=GREEN, bg=YELLOW)
    check_marks.grid(column=1, row=3)

    # Canvas

    canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
    tomato_img = tkinter.PhotoImage(file="tomato.png")
    canvas.create_image(100, 112, image=tomato_img)
    timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    canvas.grid(column=1, row=1)

    # Buttons

    start_button = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
    start_button.grid(column=0, row=2)

    reset_button = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
    reset_button.grid(column=2, row=2)

    window.mainloop()


# TIMER RESET

def reset_timer() -> None:
    """
    Reset the time the text reps and check marks
    Parameters: None
    Returns: None
    """
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


#  TIMER MECHANISM

def start_timer() -> None:
    """
    Start the timer and identifying which session it is
    Parameters: None
    Returns: None
    """
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


#  COUNTDOWN MECHANISM

def count_down(count: int) -> None:
    """
    Counts down the time and show to screen
    Parameters: count - the time  of the current session in sec
    Returns: None
    """
    # calculate, the num of min and sec of the session
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    # check when the time of the session is done
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:  # adding check marks
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


if __name__ == "__main__":
    main()

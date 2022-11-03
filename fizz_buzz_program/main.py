import math
import tkinter
from tkinter import messagebox
import threading

# CONSTANTS

FONT_NAME = "Courier"
img_icon = "images/favicon.ico"


def main():
    #  UI SETUP

    root = tkinter.Tk()
    root.title("Program Menu")
    root.config(padx=20, pady=20)
    root.geometry("600x250")
    root.bitmap(img_icon)
    root['background'] = '#FFF89C'

    # Labels

    root_label = tkinter.Label(root, text="Welcome to Liron Fizz Buzz Program", font=(FONT_NAME, 20), bg="#FFF89C")
    root_label.grid(column=0, row=0, columnspan="3")

    explanation_button = tkinter.Button(root, text="Program explanation", highlightthickness=0, width=20, bd="10",
                                        bg="#D75281", command=explanation_progra)
    explanation_button.grid(column=1, row=1, pady=30)

    play_button = tkinter.Button(root, text="Play", highlightthickness=0, width=20, bd="10", bg="#D75281",command=start_program)
    play_button.grid(column=1, row=2)

    root.mainloop()


def start_program() -> None:
    global entry_number, output_label
    """
    Start the program
    Parameters: None
    Returns: None
    """
    second_root = tkinter.Toplevel()
    second_root.title(" Liron Buzz Program")
    second_root.iconbitmap(img_icon)
    second_root.geometry("600x300")
    second_root['background'] = '#CA955C'

    # Labels

    enter_num_label = tkinter.Label(second_root, text="Enter Number:", font=(FONT_NAME, 10), bg="#CA955C")
    enter_num_label.grid(column=0, row=0, columnspan="1")

    output_label = tkinter.Label(second_root, text=f"The numbers:", font=(FONT_NAME, 10), bg="#CA955C")
    output_label.grid(column=0, row=1, columnspan="1")

    # Entry

    entry_number = tkinter.Entry(second_root, width=20, selectborderwidth="5")
    entry_number.insert(tkinter.END, string="")
    entry_number.focus()
    entry_number.grid(column=1, row=0, columnspan=1, padx=20, pady=30)

    number_button = tkinter.Button(second_root, text="Send", highlightthickness=0, width=10, bd="10",bg="#EDDFB3", command=new_thread)
    number_button.grid(column=2, row=0, columnspan=1, padx=10, pady=30)


def new_thread() -> None:
    global send_number
    """
    Make new thread
    Parameters: None
    Returns: None
    """
    thread1 = threading.Thread(target=send_number)
    thread1.start()

def explanation_progra() -> None:
    """
    Start the program
    Parameters: None
    Returns: None
    """
    tkinter.messagebox.showinfo(title="Pogram Explanation",
                                message="Hi, in this software you enter a number and it shows you which of the numbers from one to 10 is divided by it without a remainder, let's say 10, the result will be 1 2 5 and 10.")


def send_number() -> None:
    global entry_number, output_label, send_number
    """
    Get the number
    Parameters: None
    Returns: None
    """
    arr_div_number = []
    input_num = 5
    try:
        input_num = int(entry_number.get())
    except ValueError:
        tkinter.messagebox.showerror(title="Input Error", message="Please enter number")

    if input_num < 0:
        tkinter.messagebox.showerror(title="Input Error", message="Please enter non negative number")
    elif input_num == 0:
        output_label.config(text=f"The numbers: {0}")
    else:
        for num in range(1, math.ceil(input_num / 2) + 2, 1):
            print(num)
            if input_num % num == 0:
                arr_div_number.append(num)
        arr_div_number.append(input_num)
    number_string = " ".join(str(e) for e in arr_div_number)
    as1 = number_string.split(" ")
    for i in range(0, len(as1), 5):
        as1[i] += '\n'
    number_string1 = " ".join(as1)
    output_label.config(text=f"The numbers: \n {number_string1}")


if __name__ == "__main__":
    main()

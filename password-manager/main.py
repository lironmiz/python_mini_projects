import tkinter
from tkinter import messagebox
import string
import random
import pyperclip
import json
import os

# CONSTANTS
NUM_DIGIT_RANDOM_PASSWORD = 10
FONT_NAME = "Courier"
FILE_NAME = "data.json"

def main():
    global canvas, entry_website_input, entry_email_input, entry_password_input

    #  UI SETUP

    window = tkinter.Tk()
    window.title("liron Password Manager")
    window.config(padx=20, pady=20)

    # Canvas

    canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
    logo_img = tkinter.PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=logo_img)
    canvas.grid(column=1, row=0)

    # Labels

    website_label = tkinter.Label(text="Website:", font=(FONT_NAME, 10))
    website_label.grid(column=0, row=1)

    user_name_label = tkinter.Label(text="Email/Username:", font=(FONT_NAME, 10))
    user_name_label.grid(column=0, row=2)

    password_label = tkinter.Label(text="Password:", font=(FONT_NAME, 10))
    password_label.grid(column=0, row=3)

    # Entry

    entry_website_input = tkinter.Entry(width=32)
    entry_website_input.insert(tkinter.END, string="")
    entry_website_input.focus()
    entry_website_input.grid(column=1, row=1, columnspan=1)

    entry_email_input = tkinter.Entry(width=50)
    entry_email_input.insert(tkinter.END, string="")
    entry_email_input.insert(index=0, string="liri25112003@gmail.com")
    entry_email_input.grid(column=1, row=2, columnspan=2)

    entry_password_input = tkinter.Entry(width=32)
    entry_password_input.insert(tkinter.END, string="")
    entry_password_input.grid(column=1, row=3)

    # Buttons

    password_button = tkinter.Button(text="Generate Password", highlightthickness=0, command=generate_password,
                                     width=14)
    password_button.grid(column=2, row=3)

    add_button = tkinter.Button(text="Add", highlightthickness=0, width=43, command=save_password)
    add_button.grid(column=1, row=4, columnspan=2)

    search_button = tkinter.Button(text="Search", highlightthickness=0, command=find_password, width=14)
    search_button.grid(column=2, row=1)

    window.mainloop()


def find_password() -> None:
    """
    Looking if the input in website entry mach  one of the existing data in data.jason
    Parameters: None
    Returns: None
    """
    website = entry_website_input.get()
    try:
        with open(FILE_NAME, 'r') as data_file:
            # Reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        tkinter.messagebox.showwarning(title="Data not found", message="No details exists for the website.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            tkinter.messagebox.showinfo(title="info",
                                        message=f"the name of the website is {website} \n and the email is {email} and the password is {password}")
        else:
            tkinter.messagebox.showwarning(title="Data not found", message="No details for the website exists.")


def generate_password() -> None:
    """
    Generate random password to the user
    Parameters: None
    Returns: None
    """
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    all = lower + upper + num + symbols
    password = "".join(random.sample(all, NUM_DIGIT_RANDOM_PASSWORD))
    entry_password_input.insert(index=0, string=password)
    pyperclip.copy(password)


def save_password() -> None:
    """
    Add user data to data.txt file
    Parameters: None
    Returns: None
    """
    password = entry_password_input.get()
    email = entry_email_input.get()
    website = entry_website_input.get()
    data = {
        website: {
            "email": email,
            "password": password
        }
    }
    # making sure that that none of the filed empty and that the user sure with the data
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        tkinter.messagebox.showerror(title="Oops", message="please make sure you not left any filed empty")
    else:
        is_ok = tkinter.messagebox.askokcancel(title=website,
                                               message=f"These are the details entered: \nWebsite: {website}\nEmail: {email}\nPassword: {password} is this ok?")
        if is_ok:
            # write to the file
            try:
                with open(FILE_NAME, 'r') as data_file:
                    # Reading old data
                    data.update(json.load(data_file))
            except FileNotFoundError:
                pass
            finally:
                with open(FILE_NAME, "w") as data_file:
                    json.dump(data, data_file, indent=4)
                # delete the data entered
                entry_website_input.delete(first=0, last=tkinter.END)
                entry_password_input.delete(first=0, last=tkinter.END)


if __name__ == "__main__":
    main()

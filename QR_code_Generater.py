import pyqrcode
from tkinter import messagebox
from tkinter import Tk, Label, StringVar, Entry, Button, BitmapImage

FONT = ("Courier", 30)

# Tk object
tk = Tk()
# Define the settings of the window
tk.title("liron QR_generator")
tk.config(bg="#E8DFCA")

def generate_qr()->None:
    """
        the function generator QR code
        param: none
        return: none
    """
    global qr, image
    # Checking user input
    if len(user_input.get()) != 0:
        qr = pyqrcode.create(user_input.get())
        image = BitmapImage(data=qr.xbm(scale=10))
    else:
        messagebox.showwarning("warning", "fields are required!!")
    try:
        display_code()
    except:
        pass

def display_code()->None:
    """
        the function display the qr code
        param: none
        return: none
    """
    image_label.config(image=image)
    output.config(text=f"Qr code : {user_input.get()}")

label = Label(tk, text="enter Text or Url", bg="#F25252", padx=30, pady=20, font=FONT)
label.pack(pady=15)

user_input = StringVar()
entry = Entry(tk, textvariable=user_input, width=50, font=FONT)
entry.pack(padx=40, pady=30)

button = Button(tk, text="generate qr", width=20, command=generate_qr, font=FONT)
button.pack(padx=15, pady=15)

image_label = Label(tk, bg="#e6e6e6")
image_label.pack()

output = Label(tk, text="", bg="#F25252")
output.pack(pady=15)

tk.mainloop()
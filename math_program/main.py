import tkinter
import threading
import numpy as np
import sympy
from matplotlib import pyplot as plt
import math
from PIL import ImageTk, Image
from tkinter import ttk, messagebox, filedialog
from tkVideoPlayer import TkinterVideo
from sympy import limit, Symbol
from sympy import init_printing


img_icon = "images/favicon.ico"
math_icon = "images/math-modified1.png"
FONT_NAME = "Courier"
trig_image = "images/trig-modified1.png"
lim_image = "images/lim_icon.png"
trig_banner = "images/trig_banner3.png"
cos_img = "images/cos-modified.png"
send_img = "images/send-modified1.png"
cheat_sheet = "images/cheat_sheet-modified1.png"
lim_img = "images/def_limt2.png"
integral_img = "images/integral2.png"

init_printing()


def main():
    #  UI SETUP

    root = tkinter.Tk()
    root.title("Liron Math Program")
    root.config(padx=20, pady=20)
    root.geometry("950x650")
    root.iconbitmap(img_icon)
    root['background'] = '#E4DCCF'

    # Canvas

    canvas_logo = tkinter.Canvas(root, width=60, height=60, highlightthickness=0, bg="#E4DCCF")
    logo_img = tkinter.PhotoImage(file=math_icon)
    canvas_logo.create_image(30, 30, image=logo_img)
    canvas_logo.place(x=460, y=10)

    canvas_menue = tkinter.Canvas(root, width=870, height=500, highlightthickness=0, bg="#7D9D9C")
    trig_img = tkinter.PhotoImage(file=trig_image)
    lim_img = tkinter.PhotoImage(file=lim_image)
    integral_img1 = tkinter.PhotoImage(file=integral_img)
    canvas_menue.place(x=20, y=100)

    # Labels

    root_label = tkinter.Label(root, text="Welcome to Liron", font=("Helvetica", 35, "bold"), bg="#E4DCCF")
    root_label.place(x=20, y=10)

    root_label1 = tkinter.Label(root, text="Math Program", font=("Helvetica", 35, "bold"), bg="#E4DCCF")
    root_label1.place(x=570, y=10)

    trig_label = tkinter.Label(root, text="Trig World", fg="#05595B", font=("Helvetica", 20, "bold"), bg="#7D9D9C")
    trig_label.place(x=140, y=145)

    lim_label = tkinter.Label(root, text="Limits World", fg="#05595B", font=("Helvetica", 20, "bold"), bg="#7D9D9C")
    lim_label.place(x=140, y=210)

    integral_label = tkinter.Label(root, text="Integral World", fg="#05595B", font=("Helvetica", 20, "bold"),
                                   bg="#7D9D9C")
    integral_label.place(x=140, y=280)

    # Buttons

    trig_button = tkinter.Button(root, image=trig_img, highlightthickness=0, width=60, bg="#7D9D9C",
                                 command=trig_window)
    trig_button.place(x=60, y=130)

    lim_button = tkinter.Button(root, image=lim_img, highlightthickness=0, width=60, bg="#7D9D9C",
                                command=lim_window)
    lim_button.place(x=60, y=200)

    integral_button = tkinter.Button(root, image=integral_img1, highlightthickness=0, width=60, bg="#7D9D9C",
                                     command=integral_window)
    integral_button.place(x=60, y=270)

    root.mainloop()


def trig_window() -> None:
    """
    Start the trig window
    Parameters: None
    Returns: None
    """
    global trig_banner_image, send1_img, videoplayer, entry_angle_input, trig_root, radian_label, cheat_sheet1, entry_engle_input1, show_function_value

    trig_root = tkinter.Toplevel()
    trig_root.title(" Trig World")
    trig_root.iconbitmap(img_icon)
    trig_root.geometry("800x600")
    trig_root.iconbitmap(img_icon)
    trig_root['background'] = '#ECB390'

    trig_banner_image = ImageTk.PhotoImage(Image.open(trig_banner))
    send1_img = ImageTk.PhotoImage(Image.open(send_img))
    cheat_sheet1 = ImageTk.PhotoImage(Image.open(cheat_sheet))
    trig_root_label = tkinter.Label(trig_root, image=trig_banner_image)
    trig_root_label.place(x=0, y=0)

    vlist = ["cos", "sin", "tan",
             "cosh", "sinh", "arccos", "arcsin", "arctan"]

    Combo_func = tkinter.ttk.Combobox(trig_root, values=vlist)
    Combo_func.set("Pick an Function")
    Combo_func.place(x=40, y=330)

    pick_trig_function = tkinter.Label(trig_root,
                                       text="Enter a b and c and pick a graph \nthe parmeters is like this A*fun(B*x) + C \n when finish press send button",
                                       font=("Helvetica", 8, "bold"), bg="#ECB390")
    pick_trig_function.place(x=1, y=270)

    # Entry

    entry_a_input = tkinter.Entry(trig_root, width=23)
    entry_a_input.insert(tkinter.END, string="Enter A:")
    entry_a_input.place(x=40, y=370)

    entry_b_input = tkinter.Entry(trig_root, width=23)
    entry_b_input.insert(tkinter.END, string="Enter B:")
    entry_b_input.place(x=40, y=400)

    entry_c_input = tkinter.Entry(trig_root, width=23)
    entry_c_input.insert(tkinter.END, string="Enter C:")
    entry_c_input.place(x=40, y=430)

    send_button = tkinter.Button(trig_root, image=send1_img, highlightthickness=0, width=60, bg="#ECB390",
                                 command=lambda: send_graph_data(Combo_func.get(), entry_a_input.get(),
                                                                 entry_b_input.get(), entry_c_input.get()))
    send_button.place(x=80, y=485)

    play_button = tkinter.Button(trig_root, text="play trig video", highlightthickness=0, width=21, bg="#ECB390",
                                 command=play_trig)
    play_button.place(x=600, y=270)

    pause_button = tkinter.Button(trig_root, text="pause trig video", highlightthickness=0, width=21, bg="#ECB390",
                                  command=pause_trig)
    pause_button.place(x=600, y=300)

    videoplayer = TkinterVideo(master=trig_root, scaled=True)
    videoplayer.load(r"trig (1).mp4")
    videoplayer.place(x=600, y=330)

    entry_angle_input = tkinter.Entry(trig_root, width=24)
    entry_angle_input.insert(tkinter.END, string="Enter angle:")
    entry_angle_input.place(x=600, y=450)

    send1_button = tkinter.Button(trig_root, text="Send", highlightthickness=0, width=20, bg="#ECB390",
                                  command=convert_radian)
    send1_button.place(x=600, y=485)

    radian_label = tkinter.Label(trig_root, text="engle is  a num in radian.",
                                 font=("Helvetica", 10, "bold"), bg="#ECB390")

    cheat_sheet_button = tkinter.Button(trig_root, image=cheat_sheet1, highlightthickness=0, width=60, bg="#ECB390",
                                        command=open_file_root)
    cheat_sheet_button.place(x=380, y=270)

    # Entry

    entry_engle_input1 = tkinter.Entry(trig_root, width=15)
    entry_engle_input1.insert(tkinter.END, string="Enter angle:")
    entry_engle_input1.place(x=365, y=350)

    send2_button = tkinter.Button(trig_root, text="Send angle", highlightthickness=0, width=15, bg="#ECB390",
                                  command=show_value_function)
    send2_button.place(x=355, y=400)

    show_function_value = tkinter.Label(trig_root, text="", font=("Helvetica", 10, "bold"), bg="#ECB390")
    show_function_value.place(x=360, y=430)


def integral_window() -> None:
    """
    Start the integral  window
    Parameters: None
    Returns: None
    """
    global img_icon, cheat_sheet1, cheat_sheet, insert_label1, send_img, send1_img, entry_function_input1, start_x, end_x
    intgral_root = tkinter.Toplevel()
    intgral_root.title("integral window world")
    intgral_root.iconbitmap(img_icon)
    intgral_root.geometry("1000x600")
    send1_img = ImageTk.PhotoImage(Image.open(send_img))
    intgral_root.iconbitmap(img_icon)
    intgral_root['background'] = '#3F4E4F'
    cheat_sheet1 = ImageTk.PhotoImage(Image.open(cheat_sheet))
    cheat_sheet_button = tkinter.Button(intgral_root, image=cheat_sheet1, highlightthickness=0, width=60, bg="#3F4E4F",
                                        command=open_file_root)
    cheat_sheet_button.place(x=890, y=80)

    weclome_lim_label = tkinter.Label(intgral_root, text="welcome to liron integral world", font=("Modern", 35, "bold"),
                                      bg="#3F4E4F")
    weclome_lim_label.place(x=230, y=10)

    insert_integral_label = tkinter.Label(intgral_root,
                                          text="Enter function you want to integrate: \n and ** is ^ exp is e and log is ln \n if you want definte integral enter the start x and end x if no dont fil them ",
                                          font=("Modern", 15, "bold"), bg="#3F4E4F")
    insert_integral_label.place(x=20, y=80)

    entry_function_input1 = tkinter.Entry(intgral_root, width=24)
    entry_function_input1.insert(tkinter.END, string="f(x) = ")
    entry_function_input1.place(x=40, y=180)

    start_x = tkinter.Entry(intgral_root, width=24)
    start_x.insert(tkinter.END, string="start x:")
    start_x.place(x=40, y=210)

    end_x = tkinter.Entry(intgral_root, width=24)
    end_x.insert(tkinter.END, string="end x:")
    end_x.place(x=40, y=240)

    send_data_button1 = tkinter.Button(intgral_root, image=send1_img, highlightthickness=0, width=60, bg="#3F4E4F",
                                       command=calculate_integral)
    send_data_button1.place(x=80, y=280)

    insert_label1 = tkinter.Label(intgral_root, text="", font=("Modern", 15, "bold"), bg="#3F4E4F")
    insert_label1.place(x=15, y=350)


def calculate_integral() -> None:
    """
    calculate the integral of the user
    Parameters: None
    Returns: None
    """
    global insert_label1, entry_function_input1, start_x, end_x
    x = Symbol('x')
    try:
        float(start_x.get())
        float(end_x.get())
        f = entry_function_input1.get()
        integral1 = sympy.integrate(f, (x, float(start_x.get()), float(end_x.get()))).simplify()
        insert_label1.config(
            text=f"the output of {entry_function_input1.get()} from {float(start_x.get())} to {float(end_x.get())} is {integral1}")
    except ValueError:
        f = entry_function_input1.get()
        try:
            integral = sympy.integrate(f, x).simplify()
            insert_label1.config(text=f"the integral of {entry_function_input1.get()} is {integral} + c")
        except:
            tkinter.messagebox.showerror(title="Bad input", message="enter the function and the Arithmetic ")


def lim_window() -> None:
    """
    Start the limit window
    Parameters: None
    Returns: None
    """
    global img_icon, cheat_sheet1, send1_img, send_img, entry_point_input, entry_function_input, insert_label, lim_def_img
    lim_root = tkinter.Toplevel()
    lim_root.title(" lim World")
    lim_root.iconbitmap(img_icon)
    lim_root.geometry("800x600")
    lim_root.iconbitmap(img_icon)
    lim_root['background'] = '#607EAA'
    cheat_sheet1 = ImageTk.PhotoImage(Image.open(cheat_sheet))
    lim_def_img = ImageTk.PhotoImage(Image.open(lim_img))
    cheat_sheet_button = tkinter.Button(lim_root, image=cheat_sheet1, highlightthickness=0, width=60, bg="#607EAA",
                                        command=open_file_root)
    cheat_sheet_button.place(x=690, y=80)

    send1_img = ImageTk.PhotoImage(Image.open(send_img))

    weclome_lim_label = tkinter.Label(lim_root, text="welcome to liron limit world", font=("Terminal", 25, "bold"),
                                      bg="#607EAA")
    weclome_lim_label.place(x=50, y=10)

    insert_label = tkinter.Label(lim_root,
                                 text="Enter function and the point you want to calclute the lim for \n if you want infinty write oo:",
                                 font=("Terminal", 9, "bold"),
                                 bg="#607EAA")
    insert_label.place(x=20, y=80)

    entry_function_input = tkinter.Entry(lim_root, width=24)
    entry_function_input.insert(tkinter.END, string="f(x) = ")
    entry_function_input.place(x=20, y=150)

    entry_point_input = tkinter.Entry(lim_root, width=24)
    entry_point_input.insert(tkinter.END, string="x =  ")
    entry_point_input.place(x=20, y=190)

    send_data_button = tkinter.Button(lim_root, image=send1_img, highlightthickness=0, width=60, bg="#607EAA",
                                      command=calclute_limit)
    send_data_button.place(x=40, y=220)

    insert_label = tkinter.Label(lim_root, text="", font=("Terminal", 9, "bold"), bg="#607EAA")
    insert_label.place(x=15, y=290)

    limit_label = tkinter.Label(lim_root, text="Limit Definition", font=("Terminal", 14, "bold"), bg="#607EAA")
    limit_label.place(x=460, y=170)

    canvas_limit = tkinter.Canvas(lim_root, width=500, height=600, highlightthickness=0, bg="#607EAA")
    canvas_limit.create_image(250, 200, image=lim_def_img)
    canvas_limit.place(x=290, y=200)


def calclute_limit() -> None:
    """
    calclute the limit and show the graph
    Parameters: None
    Returns: None
    """
    global entry_point_input, entry_function_input, insert_label
    x = Symbol('x')
    y = entry_function_input.get()
    point = entry_point_input.get()
    try:
        lim = limit(y, x, point)
        insert_label.config(text=f"the lim of the {y}\nin the point {point} is\n{lim}")
    except:
        tkinter.messagebox.showerror(title="Bad input", message="enter the function and the Arithmetic ")


def show_value_function() -> None:
    """
    update the show function value to the screen in trig root
    Parameters: None
    Returns: None
    """
    global entry_engle_input1, trig_root, show_function_value
    try:
        float(entry_engle_input1.get())
        tkinter.Label.config(show_function_value,
                             text=f"cos is {round(math.cos(float(entry_engle_input1.get()) * (math.pi / 180)), 2)} \n sin is {round(math.sin(float(entry_engle_input1.get()) * (math.pi / 180)), 2)} \n tan is {round(math.tan(float(entry_engle_input1.get()) * (math.pi / 180)), 2)}")
    except ValueError:
        tkinter.messagebox.showerror(title="Bed Input", message="Enter number please!")


def open_file_root() -> None:
    """
    Open file root gui
    Parameters: None
    Returns: None
    """
    global file_root, text, img_icon
    file_root = tkinter.Tk()
    # Set the Geometry
    file_root.geometry("680x520")
    file_root.title("Liron Cheat Sheets")
    file_root.iconbitmap(img_icon)
    file_root['background'] = '#354259'
    text = tkinter.Text(file_root, width=80, height=30)
    text.place(x=20, y=20)

    # Create a Menu
    my_menu = tkinter.Menu(file_root)
    file_root.config(menu=my_menu)
    # Add dropdown to the Menus
    file_menu = tkinter.Menu(my_menu, tearoff=False)

    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_command(label="Clear", command=clear_text)
    file_menu.add_command(label="Quit", command=quit_file_root)


def quit_file_root() -> None:
    """
    quit the file root
    Parameters: None
    Returns: None
    """
    global file_root
    file_root.destroy()


def open_file() -> None:
    """
    Open the pdf file
    Parameters: None
    Returns: None
    """
    file_name = filedialog.askopenfilename(
        initialdir=r'\math_cheat_sheet'
        , title="cheat sheets",
        filetypes=(("txt files", "*.txt"),))
    if file_name:
        txt_file = file_name
        with open(txt_file, encoding="utf8") as file:
            text1 = file.read()
        # Select a Page to read
        # Add the content to TextBox
        text.insert(1.0, text1)


def clear_text() -> None:
    """
    clear the text of the file
    Parameters: None
    Returns: None
    """
    global text
    text.delete(1.0, tkinter.END)


def convert_radian() -> None:
    """
    Convert angle input to radian and show to user
    Parameters: None
    Returns: None
    """
    global entry_angle_input, trig_root, radian_label
    try:
        float(entry_angle_input.get())
        radian = float(entry_angle_input.get()) * (math.pi / 180)
        tkinter.Label.config(radian_label, text=f"{entry_angle_input.get()} is a {radian} in radian.")
        radian_label.place(x=550, y=550)
    except ValueError:
        tkinter.messagebox.showerror(title="Bed Input", message="Enter number please!")


def play_trig() -> None:
    """
    Play the trig video in the trig window
    Parameters: None
    Returns: None
    """
    global videoplayer
    videoplayer.play()  # play the video


def pause_trig() -> None:
    """
    Pause the video in the trig window
    Parameters: None
    Returns: None
    """
    global videoplayer
    videoplayer.pause()  # play the video


def send_graph_data(graph: str, a: float, b: float, c: float) -> None:
    """
    check user data and send to make graph
    Parameters: None
    Returns: None
    """
    if graph == "sin" or graph == "cos" or graph == "tan" or graph == "cosh" or graph == "sinh" or graph == "arccos" or graph == "arcsin" or graph == "arctan":
        try:
            float(a)
            float(b)
            float(c)
            if graph == "cos":
                make_cos_graph(float(a), float(b), float(c))
            elif graph == "sin":
                make_sin_graph(float(a), float(b), float(c))
            elif graph == "tan":
                make_tan_graph(float(a), float(b), float(c))
            elif graph == "cosh":
                make_cosh_graph(float(a), float(b), float(c))
            elif graph == "sinh":
                make_sinh_graph(float(a), float(b), float(c))
            elif graph == "arccos":
                make_arccos_graph(float(a), float(b), float(c))
            elif graph == "arcsin":
                make_arcsin_graph(float(a), float(b), float(c))
            else:
                make_arctan_graph(float(a), float(b), float(c))

        except ValueError:
            tkinter.messagebox.showerror(title="Bed Input", message="please enter numbers for A, B and C")
    else:
        tkinter.messagebox.showerror(title="Bed Input", message="please chose function!")


def make_cos_graph(a: float, b: float, c: float) -> None:
    """
    Make and show to the screen the cos graph
    Parameters: None
    Returns: None
    """

    x = np.arange(-10 * np.pi, 10 * np.pi, 0.01)  # start,stop,step
    z = a * np.cos(b * x) + c

    plt.plot(x, z)
    plt.xlabel('x values from -10pi to 10pi')  # string must be enclosed with quotes '  '
    plt.ylabel('cos')
    plt.title('Plot of cos from -10pi to 10pi')
    plt.legend(['cos(x)'])  # legend entries as seperate strings in a list
    plt.show()


def make_sin_graph(a: float, b: float, c: float) -> None:
    """
    Make and show to the screen the sin graph
    Parameters: None
    Returns: None
    """

    x = np.arange(-10 * np.pi, 10 * np.pi, 0.01)  # start,stop,step
    z = a * np.sin(b * x) + c

    plt.plot(x, z)
    plt.xlabel('x values from -10pi to 10pi')  # string must be enclosed with quotes '  '
    plt.ylabel('sin')
    plt.title('Plot of sin from -10pi to 10pi')
    plt.legend(['sin(x)'])  # legend entries as seperate strings in a list
    plt.show()


def make_tan_graph(a: float, b: float, c: float) -> None:
    """
    Make and show to the screen the tan graph
    Parameters: None
    Returns: None
    """

    x = np.linspace(-10 * np.pi, 10 * np.pi, 1000)
    plt.plot(x, a * np.tan(b * x) + c)
    plt.ylim(-5, 5)
    plt.xlabel('x values from -10pi to 10pi')  # string must be enclosed with quotes '  '
    plt.ylabel('tan')
    plt.title('Plot of tan from -10pi to 10pi')
    plt.legend(['tan(x)'])  # legend entries as seperate strings in a list
    plt.show()


def make_cosh_graph(a: float, b: float, c: float) -> None:
    """
    Make and show to the screen the cosh graph
    Parameters: None
    Returns: None
    """

    x = np.arange(-10 * np.pi, 10 * np.pi, 0.01)  # start,stop,step
    z = a * np.cosh(b * x) + c

    plt.plot(x, z)
    plt.xlabel('x values from -10pi to 10pi')  # string must be enclosed with quotes '  '
    plt.ylabel('cosh')
    plt.title('Plot of cosh from -10pi to 10pi')
    plt.legend(['cosh(x)'])  # legend entries as seperate strings in a list
    plt.show()


def make_sinh_graph(a: float, b: float, c: float) -> None:
    """
    Make and show to the screen the sinh graph
    Parameters: None
    Returns: None
    """

    x = np.arange(-10 * np.pi, 10 * np.pi, 0.01)  # start,stop,step
    z = a * np.sinh(b * x) + c

    plt.plot(x, z)
    plt.xlabel('x values from -10pi to 10pi')  # string must be enclosed with quotes '  '
    plt.ylabel('sinh')
    plt.title('Plot of sinh from -10pi to 10pi')
    plt.legend(['sinh(x)'])  # legend entries as seperate strings in a list
    plt.show()


def make_arccos_graph(a: float, b: float, c: float) -> None:
    """
    Make and show to the screen the arccos graph
    Parameters: None
    Returns: None
    """

    x = np.arange(-10 * np.pi, 10 * np.pi, 0.01)  # start,stop,step
    z = a * np.arccos(b * x) + c

    plt.plot(x, z)
    plt.xlabel('x values from -10pi to 10pi')  # string must be enclosed with quotes '  '
    plt.ylabel('arccos')
    plt.title('Plot of arccos from -10pi to 10pi')
    plt.legend(['arccos(x)'])  # legend entries as seperate strings in a list
    plt.show()


def make_arcsin_graph(a: float, b: float, c: float) -> None:
    """
    Make and show to the screen the arcsin graph
    Parameters: None
    Returns: None
    """

    x = np.arange(-10 * np.pi, 10 * np.pi, 0.01)  # start,stop,step
    z = a * np.arcsin(b * x) + c

    plt.plot(x, z)
    plt.xlabel('x values from -10pi to 10pi')  # string must be enclosed with quotes '  '
    plt.ylabel('arcsin')
    plt.title('Plot of arcsin from -10pi to 10pi')
    plt.legend(['arcsin(x)'])  # legend entries as seperate strings in a list
    plt.show()


def make_arctan_graph(a: float, b: float, c: float) -> None:
    """
    Make and show to the screen the arctan graph
    Parameters: None
    Returns: None
    """

    x = np.arange(-10 * np.pi, 10 * np.pi, 0.01)  # start,stop,step
    z = a * np.arctan(b * x) + c
    plt.plot(x, z)
    plt.xlabel('x values from -10pi to 10pi')  # string must be enclosed with quotes '  '
    plt.ylabel('arctan')
    plt.title('Plot of arctan from -10pi to 10pi')
    plt.legend(['arctan(x)'])  # legend entries as seperate strings in a list
    plt.show()


if __name__ == "__main__":
    main()

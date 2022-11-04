import tkinter

window = tkinter.Tk()

# Constants

LABEL_FONT = ("Ariel", 10)
MILE_TO_KILOMETERS = 1.609

def main():
    window.title("liron mile to kilometers program")
    window.minsize(width=350, height=200)

    # label in left middle of the screen
    label_is_equal_to = tkinter.Label(text="is equal to ", font=LABEL_FONT, padx=30, pady=20)
    label_is_equal_to.grid(column=0, row=1)

    # label in right upper screen
    label_miles = tkinter.Label(text="Miles ", font=LABEL_FONT, padx=30, pady=20)
    label_miles.grid(column=3, row=0)

    # label in right middle screen
    label_km = tkinter.Label(text="Km ", font=LABEL_FONT, padx=30, pady=20)
    label_km.grid(column=3, row=1)

    # user input in middle up screen
    entry_mile_input = tkinter.Entry(width=10)
    entry_mile_input.insert(tkinter.END, string="0")
    entry_mile_input.grid(column=2, row=0)

    # output to user
    label_km_output = tkinter.Label(text="0 ", font=LABEL_FONT, padx=30, pady=20)
    label_km_output.grid(column=2, row=1)

    def mile_to_kilometer() -> None:
        """
        convert mile to kilometers  round the number and show on screen
        Parameters: None
        Returns: None
        """
        miles_value = float(entry_mile_input.get())
        km_value = round(miles_value * MILE_TO_KILOMETERS)
        label_km_output.config(text=f"{km_value}")

    #  button that calls convert_mile_to_kilometers() when pressed
    button = tkinter.Button(text="Convert", command=mile_to_kilometer)
    button.grid(column=2, row=2)

    window.mainloop()


if __name__ == "__main__":
    main()

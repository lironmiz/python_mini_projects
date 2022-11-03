import tkinter
import requests


def main():
    global canvas, quote_text

    window = tkinter.Tk()
    window.title("Kanye Says...")
    window.config(padx=50, pady=50)

    canvas = tkinter.Canvas(width=300, height=414)
    background_img = tkinter.PhotoImage(file="background.png")
    canvas.create_image(150, 207, image=background_img)
    quote_text = canvas.create_text(150, 207, text="Kanya quotes goes here", width=250, font=("Arial", 20, "bold"), fill="white")
    canvas.grid(row=0, column=0)

    kanye_img = tkinter.PhotoImage(file="kanye.png")
    kanye_button = tkinter.Button(image=kanye_img, highlightthickness=0, command=get_quote)
    kanye_button.grid(row=1, column=0)

    window.mainloop()


def get_quote():
    global canvas, quote_text
    response = requests.get(url="https://api.kanye.rest")
    print(response)
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)


if __name__ == "__main__":
    main()

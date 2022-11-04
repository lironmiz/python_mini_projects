import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("liron quiz app")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Canvas

        self.canvas = tkinter.Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(140, 125, text="question", fill="black",
                                                     font=("arial", 20, "italic"), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Labels

        self.score_label = tkinter.Label(text="Score: 0", font=("ariel", 10, "bold"), bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0, ipady=20)

        false_image = tkinter.PhotoImage(file="images/false.png")
        self.false_button = tkinter.Button(image=false_image, highlightthickness=0, bg="red",
                                           command=self.false_pressed)
        self.false_button.grid(column=1, row=2, pady=10)

        true_image = tkinter.PhotoImage(file="images/true.png")
        self.true_button = tkinter.Button(image=true_image, highlightthickness=0, bg="green",
                                          command=self.true_pressed)
        self.true_button.grid(column=0, row=2, pady=10)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self) -> None:
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="End of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true_pressed(self) -> None:
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self) -> None:
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool) -> None:
        if is_right:
            self.canvas.configure(bg="green")
            self.window.after(1000, lambda: self.canvas.configure(bg="white"))
            self.score_label.configure(text=f"score: {self.quiz.score}")
        else:
            self.canvas.configure(bg="red")
            self.window.after(1000, lambda: self.canvas.configure(bg="white"))


        self.window.after(1000, self.get_next_question)

from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class UI:
    def __init__(self, quiz: QuizBrain):
        self.window = Tk()
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        self.score = Label(text=f"Score: 0", background=THEME_COLOR, foreground="white")
        self.score.grid(row=0, column=1)
        self.canvas = Canvas(width=400, height=250, background="white")
        self.text = self.canvas.create_text(150, 40, width=200, text="HELLO WORLD", fill="black",
                                            font=('Arial 10 italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.quiz = quiz
        right_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=right_image, highlightthickness=0, command=self.check_ans_right)
        self.true_button.grid(row=2, column=0, padx=20)

        wrong_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=wrong_image, padx=20, highlightthickness=0, command=self.check_ans_wrong)
        self.false_button.grid(row=2, column=1)
        self.generate_text()
        self.window.mainloop()

    def generate_text(self):
        if self.quiz.still_has_questions():
            self.canvas.configure(bg='white')
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=question)
        else:
            self.false_button["state"] = "disabled"
            self.true_button["state"] = "disabled"

    def change_canvas_color(self, answer):
        if answer:
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.configure(bg='green')
        else:
            self.canvas.configure(bg='red')

        self.window.after(1000, self.generate_text)

    def check_ans_right(self):
        answer = self.quiz.check_answer("True")
        self.change_canvas_color(answer)

    def check_ans_wrong(self):
        answer = self.quiz.check_answer("False")
        self.change_canvas_color(answer)

import tkinter
from quiz_brain import QuizBrain
from tkinter import messagebox
from qdata import get_new_questions
from question_model import Question
import html

THEME_COLOR = "#375362"


class quizzler_ui:
    def __init__(self, quiz_brain: QuizBrain):
        self.ui = tkinter.Tk()
        self.quiz = quiz_brain
        self.question_txt = None
        self.canvas = None
        self.true_btn = None
        self.false_btn = None
        self.score_lbl = None
        self.true_image = tkinter.PhotoImage(file="images/true.png")  # Load the true image
        self.false_image = tkinter.PhotoImage(file="images/false.png")  # Load the false image
        self.setup_ui()

    def setup_ui(self):
        self.ui.config(padx=20, pady=20, bg=THEME_COLOR)
        self.ui.title("Quizzler GUI")

        self.score_lbl = tkinter.Label(text="Score: 0", bg=THEME_COLOR, fg="White")
        self.score_lbl.grid(column=1, row=0)

        self.canvas = tkinter.Canvas(height=250, width=300)
        self.canvas.grid(column=0, row=1, columnspan=2)
        self.question_txt = self.canvas.create_text(150, 125, width=280
                                                    , text="Dummy Text")

        self.true_btn = tkinter.Button(image=self.true_image,
                                       command=self.answer_true)
        self.true_btn.grid(column=0, row=2, padx=10, pady=10)

        self.false_btn = tkinter.Button(image=self.false_image,
                                        command=self.answer_false)
        self.false_btn.grid(column=1, row=2, padx=10, pady=10)

        self.get_next_question()

        self.ui.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_txt, text=question_text)
        else:
            messagebox.showinfo(title="Game Over", message=f"You've reached the end of the quiz. Your "
                                                           f"final score was: {self.quiz.score}")
            replay = messagebox.askyesno(title="Replay", message="Do you want to play again?")
            if replay:
                question_bank = []
                question_data = get_new_questions()
                for question in question_data:
                    question_bank.append(Question(q_text=html.unescape(question["question"])
                                                  , q_answer=question["correct_answer"]))

                self.quiz = QuizBrain(question_bank)  # Reinitialize QuizBrain
                self.score_lbl.config(text="Score: 0")
                self.get_next_question()  # Start the game again
            else:
                self.ui.quit()  # Close the application

    def answer_true(self):
        self.feedback(self.quiz.check_answer("True"))

    def answer_false(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.ui.after(250, lambda: self.canvas.config(bg="white"))
        self.score_lbl.config(text=f"Score: {self.quiz.score}")
        self.get_next_question()

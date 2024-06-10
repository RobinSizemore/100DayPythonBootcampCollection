import tkinter
import pandas
import random

# Constants
BACKGROUND_COLOR = "#B1DDC6"


# Main App Class
class FlashcardsApp:
    def __init__(self):

        self.all_questions_df = None
        self.window = tkinter.Tk()

        self.question_bg = None
        self.unknown_btn_image = None
        self.known_btn_image = None
        self.card_canvas = None
        self.known_btn = None
        self.unknown_btn = None
        self.study_word = None
        self.study_label = None
        self.pick_item = None

        self.bg_img = None
        self.question_bg = None
        self.answer_bg = None

        self.all_questions = None
        self.flip_timer = None
        self.setup_ui()
        self.load_questions()
        self.ask_next()

    def setup_ui(self):
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
        self.window.title("Flashy")
        self.window.columnconfigure(0, uniform="a")
        self.window.columnconfigure(1, uniform="a")

        self.card_canvas = tkinter.Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
        self.question_bg = tkinter.PhotoImage(file="images/card_front.png")
        self.answer_bg = tkinter.PhotoImage(file="images/card_back.png")
        self.bg_img = self.card_canvas.create_image(400, 263, image=self.question_bg)
        self.card_canvas.grid(column=0, row=0, columnspan=2)

        self.study_label = self.card_canvas.create_text(400, 150, text="Language", font=("Ariel", 40, "italic"))
        self.study_word = self.card_canvas.create_text(400, 263, text="Language", font=("Ariel", 60, "bold"))

        self.unknown_btn_image = tkinter.PhotoImage(file="images/wrong.png")
        self.unknown_btn = tkinter.Button(image=self.unknown_btn_image, highlightthickness=0, relief="flat", bd=0,
                                          command=self.mark_unknown)
        self.unknown_btn.grid(column=0, row=1)

        self.known_btn_image = tkinter.PhotoImage(file="images/right.png")
        self.known_btn = tkinter.Button(image=self.known_btn_image, highlightthickness=0, relief="flat", bd=0,
                                        command=self.mark_known)
        self.known_btn.grid(column=1, row=1)

    def load_questions(self):
        try:
            # Try to load from to_be_asked.csv
            self.all_questions_df = pandas.read_csv(filepath_or_buffer="data/to_be_asked.csv")
            self.all_questions = self.all_questions_df.to_dict(orient="records")
            # If the file is empty, raise an exception to load from french_words.csv
            if not self.all_questions:
                raise FileNotFoundError
        except (FileNotFoundError, pandas.errors.EmptyDataError):
            # If to_be_asked.csv doesn't exist or is empty, load from french_words.csv
            self.all_questions_df = pandas.read_csv(filepath_or_buffer="data/french_words.csv")
            self.all_questions = self.all_questions_df.to_dict(orient="records")

    def ask_next(self):
        try:
            print(f"{len(self.all_questions)} left.")
            self.pick_item = random.randint(0, len(self.all_questions) - 1)
        except ValueError:  # We've run out of questions.  Start over.
            self.load_questions()
        self.card_canvas.itemconfig(self.bg_img, image=self.question_bg)
        self.card_canvas.itemconfig(self.study_label, text="French")
        study_word = self.all_questions[self.pick_item]["French"]
        self.card_canvas.itemconfig(self.study_word, text=study_word)
        self.flip_timer = self.window.after(ms=3000, func=self.flip_card)

    def flip_card(self):
        self.card_canvas.itemconfig(self.bg_img, image=self.answer_bg)
        self.card_canvas.itemconfig(self.study_label, text="English")
        self.card_canvas.itemconfig(self.study_word, text=self.all_questions[self.pick_item]["English"])

    def mark_known(self):
        self.window.after_cancel(self.flip_timer)
        # Remove the item indicated by self.pick_item from self.all_questions
        self.all_questions.pop(self.pick_item)

        # Convert the updated list of dictionaries to a DataFrame
        updated_df = pandas.DataFrame(self.all_questions)

        # Write the updated DataFrame to to_be_asked.csv
        updated_df.to_csv("data/to_be_asked.csv", index=False)

        # Continue to the next question
        self.ask_next()

    def mark_unknown(self):
        self.window.after_cancel(self.flip_timer)
        self.ask_next()


app = FlashcardsApp()
app.window.mainloop()

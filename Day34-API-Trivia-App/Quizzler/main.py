from question_model import Question
from quiz_brain import QuizBrain
import ui
from qdata import get_new_questions
import html

question_bank = []
question_data = get_new_questions()
for question in question_data:
    question_bank.append(Question(q_text=html.unescape(question["question"])
                                  , q_answer=question["correct_answer"]))

quiz = QuizBrain(question_bank)
quizzler = ui.quizzler_ui(quiz)

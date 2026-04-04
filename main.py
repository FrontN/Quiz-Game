from question_model import Questions
from data import question_data
from quiz_brain import QuizBrain
import time
import os

def clear_screen():
    """Clears the terminal screen.
    
    On Windows systems, this function executes the 'cls' command in the terminal.
    On Unix-based systems, this function executes the 'clear' command in the terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    question_bank = []

    for question in question_data:
        question_text = question["question"]
        question_answer = question["answer"]
        new_questions = Questions(question_text, question_answer)
        question_bank.append(new_questions)

    quiz = QuizBrain(question_bank)
    while quiz.still_has_questions():
        quiz.next_question()
        time.sleep(1.5)
        clear_screen()
    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_nb}")

if __name__ == "__main__":
    main()
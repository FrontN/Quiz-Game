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

def get_valid_input(text, options):
    """Asks the user for input and checks if it is one of the options provided.
    If the user's input is not one of the options, it will print "non valid answer. please try again"
    and ask for the input again."""
    while True:
        user_input = input(f"{text} ({options[0]}/{options[-1]}): ").lower()
        if user_input in options:
            return user_input
        else:
            print("non valid answer. please try again")
            time.sleep(1.5)
            clear_screen()

def main():
    """
    Starts the quiz game.

    This function creates a list of Question objects from the data in data.py,
    creates a QuizBrain object with the list of questions, and then
    starts the quiz game in a loop until the user decides to quit
    or all questions have been answered.

    Parameters:
    None

    Returns:
    None
    """
    question_bank = []

    for question in question_data:
        question_text = question["question"]
        question_answer = question["answer"]
        new_questions = Questions(question_text, question_answer)
        question_bank.append(new_questions)

    quiz = QuizBrain(question_bank)
    keep_going = True
    while keep_going:
        clear_screen()
        print("Welcome to the quiz game!")
        time.sleep(1.5)
        clear_screen()
        while quiz.still_has_questions():
            quiz.next_question()
            time.sleep(1.5)
            clear_screen()
        print("You've completed the quiz")
        print(f"Your final score was: {quiz.score}/{quiz.question_nb}")
        time.sleep(3)
        clear_screen()

        if get_valid_input("Do you want to play again?", ["yes", "y", "no", "n"]).startswith("n"):
            keep_going = False
            print("See You!!")

if __name__ == "__main__":
    main()

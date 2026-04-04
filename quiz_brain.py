import random
import time
import os

def clear_screen():
    """Clears the terminal screen.
    
    On Windows systems, this function executes the 'cls' command in the terminal.
    On Unix-based systems, this function executes the 'clear' command in the terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

class QuizBrain:
    OPTIONS = ["vero", "falso"]
    def __init__(self, question_list):
        """Initializes a QuizBrain object with a list of Question objects.
        The list is shuffled and the object's score and question number are set to 0.
        Parameters:
        question_list (list): a list of Question objects"""
        self.question_list = question_list
        random.shuffle(self.question_list)
        self.question_nb = 0
        self.score = 0

    def still_has_questions(self):
        """Returns True if there are still questions left, False otherwise."""
        return self.question_nb < len(self.question_list)
    
    def get_valid_input(self, nb, text, options):
        """Asks the user for input and checks if it is one of the options provided.
        If the user's input is not one of the options, it will print "non valid answer. please try again"
        and ask for the input again."""
        while True:
            user_input = input(f"Q.{nb}: {text} ({options[0]}/{options[-1]}): ").lower()
            if user_input in options:
                return user_input
            else:
                print("non valid answer. please try again")
                time.sleep(1.5)
                clear_screen()
    
    def next_question(self):
        """Shows the next question in the list and asks the user for the answer.
        Stores the user's answer and checks it against the correct answer.
        If the answer is correct, increments the score by 1.
        Prints out the correct answer and the current score."""
        self.question_nb += 1
        current_question = self.question_list[self.question_nb -1]
        user_answer = self.get_valid_input(self.question_nb, current_question.text, self.OPTIONS)
        self.check_answer(user_answer,current_question.answer)
    
    def check_answer(self, user_answer, correct_answer):
        """Checks if the user's answer is correct and updates the score accordingly."""
        if user_answer == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_nb}")
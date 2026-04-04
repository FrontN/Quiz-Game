Python Quiz Game 🧠
A robust, console-based Quiz game implemented in Python using Object-Oriented Programming (OOP) principles to manage questions, scoring, and game logic across a modular structure.

Features 🎮
Advanced OOP Logic: Clean separation of concerns with dedicated classes for data modeling and quiz management.

Robust Input Handling: Custom validation loop ensures the game only accepts "Vero" (True) or "Falso" (False), preventing crashes from invalid input.

Dynamic Shuffling: The question bank is automatically shuffled at game startup to ensure a unique experience every round.

Clean Interface: Automatic terminal clearing (clear_screen) and timed pauses provide optimal readability between questions.

Real-time Feedback: Immediately displays the correct answer and updates the current score after every turn.

Game Rules 📋
Objective: Correctly answer as many questions as possible from the database.

Scoring: Each correct answer grants 1 point. No points are deducted for incorrect answers.

Gameplay:

One question is presented at a time.

The user must enter "vero" or "falso" (case-insensitive).

The game reveals the correct answer and the current score immediately.

The quiz concludes once all questions in the bank have been exhausted.

Project Structure 📁
main.py: The main entry point that initializes the question bank and orchestrates the game loop.

quiz_brain.py: Contains the QuizBrain class, responsible for scoring, input validation, and flow control.

question_model.py: Defines the Questions class used to create uniform question objects.

data.py: A database containing 50 diverse questions and their respective correct answers.

Main Functions Overview:
clear_screen(): Clears the console based on the operating system (Windows/Unix).

still_has_questions(): Returns True if there are still questions remaining in the list.

get_valid_input(): A validation loop that ensures user input matches the permitted options.

next_question(): Retrieves the current question, handles user input, and triggers the answer check.

check_answer(): Compares the user's input with the correct answer and updates the global score.

Requirements ✅
Python 3.x

No external dependencies required (uses only the Python standard library).

Installation & Setup 🚀
Clone the repository:

Bash
git clone https://github.com/your-username/quiz-game-python.git
cd quiz-game-python
How to Play 🎯
Run the game:

Bash
python main.py
Read the question displayed on the terminal.

Type vero or falso and press Enter.

View the feedback and your updated score.

Complete all questions to see your final results.

Game Output Example 📺
Plaintext
Q.1: Il Sole è una stella. (vero/falso): vero
You got it right!
The correct answer was: Vero
Your current score is: 1/1

(Screen clears...)

Q.2: La capitale della Francia è Lione. (vero/falso): falso
You got it right!
The correct answer was: Falso
Your current score is: 2/2
Technical Highlights 💡
Scalability: The Questions class makes it easy to add new questions to data.py without modifying the game logic.

Robustness: Input error handling prevents the game from breaking if the user types unexpected characters.

Cross-Platform: The screen clearing function automatically detects if the environment is Windows or Unix-based.

Author 👨‍💻
FrontN - Created as a project to consolidate foundations in Python OOP and logic flow management.

Enjoy the quiz and good luck! 🧠⚡

# Quiz Game 🧠

A console-based true/false quiz game built with Python and Object-Oriented Programming principles. Test your knowledge with dynamically shuffled questions and instant feedback!

## ✨ Features

- **Object-Oriented Design** – Clean modular architecture with dedicated classes for questions, quiz logic, and game flow
- **Robust Input Validation** – Prevents crashes by ensuring only valid responses ("vero"/"falso") are accepted
- **Shuffled Questions** – Questions are randomized each game for a fresh experience
- **Real-Time Feedback** – Immediate answer reveals and score updates after each question
- **Cross-Platform** – Automatic terminal clearing works on Windows, macOS, and Linux
- **50+ Questions** – Diverse trivia database ready to expand

## 📋 How to Play

1. **Run the game**: `python main.py`
2. **Read each question** displayed on your terminal
3. **Enter your answer**: Type `vero` (true) or `falso` (false) and press Enter
4. **Get instant feedback**: See if you're correct and your current score
5. **Beat your score**: Complete all 50 questions and try to answer them all correctly!

### Scoring
- ✅ Each correct answer = 1 point
- ❌ Incorrect answers = 0 points (no penalty)
- 🏁 Final score displayed when the quiz ends

## 📺 Example Gameplay

```
Q.1: Il Sole è una stella. (vero/falso): vero
✓ You got it right!
The correct answer was: Vero
Your current score is: 1/1

Q.2: La capitale della Francia è Lione. (vero/falso): falso
✓ You got it right!
The correct answer was: Falso
Your current score is: 2/2
```

## 🚀 Installation

**Prerequisites:** Python 3.x (no external dependencies required)

```bash
# Clone the repository
git clone https://github.com/FrontN/Quiz-Game.git
cd Quiz-Game

# Run the game
python main.py
```

## 📁 Project Structure

| File | Purpose |
|------|---------|
| `main.py` | Entry point; initializes the game and manages the main loop |
| `quiz_brain.py` | `QuizBrain` class – handles scoring, validation, and game flow |
| `question_model.py` | `Questions` class – defines question object structure |
| `data.py` | Question database with 50+ trivia questions |

### Key Functions

- `clear_screen()` – Clears terminal (Windows/Unix compatible)
- `still_has_questions()` – Checks if questions remain
- `get_valid_input()` – Validates user input safely
- `next_question()` – Presents question and processes response
- `check_answer()` – Compares answer and updates score

## 💡 Technical Highlights

- **Scalable Design** – Add questions to `data.py` without touching game logic
- **Error Prevention** – Comprehensive input validation prevents crashes
- **Clean Code** – Modular structure makes the codebase easy to maintain and extend
- **Cross-Platform** – Automatic environment detection for terminal clearing

## 🤝 Contributing

Feel free to fork, improve, and submit pull requests!

## 👨‍💻 Author

**FrontN** – Created to master Python OOP principles and game logic management

---

Good luck and enjoy the quiz! 🧠⚡
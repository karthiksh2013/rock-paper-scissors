# Rock, Paper, Scissors 🎮

A beginner-friendly Rock, Paper, Scissors game built with Python. Play against a randomly controlled opponent, track scores, replay rounds, and rate the game!

Developed by **Karthik** as my first major Python project.

## 📌 About the Project

This project is a command-line implementation of the classic Rock, Paper, Scissors game. It was created to practice Python fundamentals, including user input, conditional statements, loops, dictionaries, variables, and the `random` module.

## ✨ Features

- 👤 **Personalized Gameplay:** Enter your name and your opponent's name.
- 🎲 **Random Opponent:** The opponent's choice is selected randomly.
- 🏆 **Score Tracking:** Keep track of wins for both players.
- 🔄 **Replay Option:** Play additional rounds without restarting the program.
- 📊 **Scoreboard:** View the current scores after each round.
- 📝 **Final Results:** See the final scores when you finish playing.
- ⭐ **Game Rating:** Submit a rating out of 5 stars.

## 🛠️ Built With

- **Python 3**
- Python standard library (`random` module)

No third-party packages are required.

## 🚀 Getting Started

### Prerequisites

Install Python 3 on your computer.

Check whether Python is installed by running:

```bash
python --version
```

If that command doesn't work, try:

```bash
py --version
```

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/karthiksh2013/rock-paper-scissors.git
   ```

2. Navigate to the project folder:

   ```bash
   cd rock-paper-scissors
   ```

3. Run the game:

   ```bash
   python main.py
   ```

   On Windows, you can also try:

   ```bash
   py main.py
   ```

## 🎮 How to Play

1. Enter your name.
2. Enter your opponent's name.
3. Choose one of the following options:
   - `R` — Rock
   - `P` — Paper
   - `S` — Scissors
4. View the choices and round result.
5. Check the scoreboard.
6. Enter `yes` or `y` to play another round, or enter `no` to finish.
7. View the final scores and submit your rating.

### Game Rules

| Your choice | Beats |
|---|---|
| Rock | Scissors |
| Paper | Rock |
| Scissors | Paper |

If both players choose the same option, the round is a tie.

## 📂 Project Structure

```text
rock-paper-scissors/
├── main.py
└── README.md
```

## 📚 What I Learned

While building this project, I practiced:

- Taking user input with `input()`
- Using variables and dictionaries
- Applying `if`, `elif`, and `else` statements
- Using `while` loops
- Generating random choices with `random.choice()`
- Updating and displaying scores
- Formatting output with f-strings

## 🔮 Future Improvements

- [ ] Improve input validation and error handling.
- [ ] Add a best-of-five game mode.
- [ ] Display win, loss, and tie statistics.
- [ ] Organize the code into reusable functions.
- [ ] Add a graphical user interface.

## 👨‍💻 Developer

**Karthik** — Student developer learning Python and working toward a career in Artificial Intelligence and Machine Learning.

This is my first major Python project, and I'm continuing to improve my programming skills by building practical projects.

---

*Learning by building, one project at a time.*

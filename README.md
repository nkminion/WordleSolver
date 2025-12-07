Wordle Solver


An automated tool that solves the New York Times Wordle game.
Made with Python and Selenium.

Features:

Fully autonomous: Opens a chromium window and solves the puzzle with no manual intervention.
Real-Time: Watch the program solve the puzzle in real time.

Pre-requisites:

Python 3.11
It is recommended to use a virtual environment.

Setup (Linux):

Clone the repository
```bash
git clone https://github.com/nkminion/WordleSolver
cd ./WordleSolver
```

Create and activate a virtual environment
```bash
python -m venv WordleSolver
source WordleSolver/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Working:

The script uses selenium for all I/O. It opens a chromium window (You do not have to install chromium).

It then picks a word from its word list (starts with 'audio' due to higher number of vowels).

The script scrapes the HTML of the page to check if it is was right or wrong and filters its wordlist accordingly.

# Higher or Lower Game 🎮

Welcome to the **Higher or Lower Game**, a fun and simple Python-based guessing game!

In this game, you'll be shown two popular people or entities with their descriptions. Your task is to guess **which one has more followers**. If you guess right, your score increases. If not, the game ends and your score is displayed.

---

## 📁 Project Structure

This game is made up of three main files:

```
higher-or-lower-game/
├── art.py          # ASCII art visuals
├── game_data.py    # Game data - names, follower counts, etc.
└── main.py         # Main game logic
```

---

## 🧠 How the Game Works

1. Two random "accounts" are shown.
2. You guess which one has more followers.
3. If you’re right, the game continues and your score increases.
4. If you're wrong, the game ends.

---

## 📝 Code Breakdown

---

### `art.py` - 🎨 Game ASCII Art

This file contains fun ASCII art that’s printed during the game.

```python
logo = r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
```

- `logo`: Shows at the start and after every correct answer.
- `vs`: Displays between the two options for comparison.

---

### `game_data.py` - 📊 Game Dataset

This file contains a list of dictionaries. Each dictionary represents a public figure or platform.

```python
data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    ...
]
```

Each entry includes:

- `name`: Person or entity name.
- `follower_count`: Their follower count (used for comparing).
- `description`: What they’re known for.
- `country`: Where they’re from.

---

### `main.py` - 🧩 Main Game Logic

This file ties everything together. Here's a breakdown of how it works:

#### 📦 Imports

```python
import random
from game_data import data
from art import logo, vs
from replit import clear
```

- `random`: To select random entries.
- `data`: The dataset with account info.
- `logo`, `vs`: ASCII visuals.
- `clear`: Clears the screen (works in Replit).

#### 🔁 Functions

```python
def get_random_account():
    return random.choice(data)
```

- Picks a random account from the dataset.

```python
def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"
```

- Formats the account info for display.

```python
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
```

- Compares follower counts and checks if your guess was correct.

#### 🕹 Game Loop

```python
score = 0
game_should_continue = True
account_a = get_random_account()
account_b = get_random_account()

while game_should_continue:
    account_a = account_b
    account_b = get_random_account()

    while account_a == account_b:
        account_b = get_random_account()

    print(logo)
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
```

---

## ▶️ How to Run

1. Clone the repository:
```bash
git clone https://github.com/psyccho00/Higher-OR-Lower-Game.git
cd Higher-OR-Lower-Game
```

2. Run the game:
```bash
python main.py
```

💡 You can run it on your terminal or in [Replit](https://replit.com).

---

## ✅ Requirements

- Python 3.x
- (Optional) [Replit](https://replit.com/) for running in browser

---

## 🙌 Credits

- Game inspired by the popular "Higher or Lower" concept
- ASCII art by [ascii.co.uk](https://ascii.co.uk)
- Built by [psyccho00](https://github.com/psyccho00)

---

Have fun guessing! 🧠💥

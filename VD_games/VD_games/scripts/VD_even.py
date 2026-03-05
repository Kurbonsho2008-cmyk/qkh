import random
import sys
import os

# Добавляем путь к корневой папке проекта
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Теперь импортируем
from cli import welcome_user, ask_question


def is_even(number: int) -> bool:
    """Return True if number is even."""
    return number % 2 == 0


def play_even_game() -> None:
    """Main game logic for even/odd game."""
    print("Welcome to the VD-games!")
    name = welcome_user()
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0
    while correct_answers < 3:
        number = random.randint(1, 100)
        correct_answer = "yes" if is_even(number) else "no"

        print(f"Question: {number}")
        user_answer = ask_question("Your answer: ")

        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print("Correct!")
        correct_answers += 1

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    play_even_game()

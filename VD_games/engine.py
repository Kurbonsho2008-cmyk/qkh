"""Общий движок для всех игр"""

from VD_games.cli import welcome_user

ROUNDS = 3

def run_game(game_module):
    # Приветствие
    name = welcome_user()
    print(game_module.DESCRIPTION)
    
    # 3 раунда
    for _ in range(ROUNDS):
        question, correct_answer = game_module.generate_round()
        print(f"Question: {question}")
        
        user_answer = input("Your answer: ")
        
        if user_answer == str(correct_answer):
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")

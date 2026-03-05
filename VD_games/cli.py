"""Модуль для работы с интерфейсом командной строки игры"""

def welcome_user():
    """Функция приветствия пользователя"""
    print("Welcome to the VD-games!")
    try:
        name = input("May I have your name? ")
        # Очистка имени от возможных артефактов
        name = name.strip()
    except (KeyboardInterrupt, EOFError):
        name = "Player"

    print(f"Hello, {name}!")
    return name


def ask_question(prompt):
    """Функция для запроса ответа у пользователя"""
    try:
        answer = input(prompt)
        return answer.strip().lower()
    except (KeyboardInterrupt, EOFError):
        return ""

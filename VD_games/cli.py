"""Модуль для работы с интерфейсом командной строки игры"""

def welcome_user():
    """Функция приветствия пользователя"""
    print("Welcome to the VD-games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")

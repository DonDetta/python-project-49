import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number: int) -> bool:
    return number % 2 == 0


def generate_round():
    number = random.randint(1, 100)
    correct_answer = 'yes' if is_even(number) else 'no'
    question = str(number)
    return question, correct_answer

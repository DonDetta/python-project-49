from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number: int) -> bool:
    if number < 2:
        return False

    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1

    return True


def generate_round():
    question_number = randint(1, 100)
    question = str(question_number)

    correct_answer = 'yes' if is_prime(question_number) else 'no'

    return question, correct_answer

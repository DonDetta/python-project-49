from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def generate_round():
    number1 = randint(1, 100)
    number2 = randint(1, 100)

    question = f'{number1} {number2}'
    correct_answer = str(gcd(number1, number2))

    return question, correct_answer

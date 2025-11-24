import random

DESCRIPTION = 'What is the result of the expression?'


def generate_round():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])

    match operation:
        case '+':
            result = number1 + number2
        case '-':
            result = number1 - number2
        case '*':
            result = number1 * number2
        case _:
            # на всякий случай, но до сюда мы не дойдём
            raise ValueError(f'Unknown operation: {operation}')

    question = f'{number1} {operation} {number2}'
    correct_answer = str(result)
    return question, correct_answer

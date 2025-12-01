from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def generate_progression(start: int, step: int, length: int) -> list[int]:
    return [start + index * step for index in range(length)]


def generate_round():
    length = 10

    start = randint(1, 20)
    step = randint(1, 10)

    progression = generate_progression(start, step, length)

    hidden_index = randint(0, length - 1)
    correct_answer = str(progression[hidden_index])

    progression_for_question = [
        '..' if index == hidden_index else str(num)
        for index, num in enumerate(progression)
    ]
    question = ' '.join(progression_for_question)

    return question, correct_answer

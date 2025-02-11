import random


def get_numbers_ticket(min: int, max: int, quantity: int):

    numbers = set()

    while len(numbers) < quantity:
        num = random.randint(min, max)
        numbers.add(num)

    return numbers


if __name__ == '__main__':
    get_numbers_ticket(1, 36, 6)

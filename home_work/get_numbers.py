import random


def get_numbers_ticket(min: int, max: int, quantity: int):

    numbers = set()
    count = 0

    while len(numbers) < quantity:
        num = random.randint(min, max)
        numbers.add(num)
        count += 1
    print(numbers, count)


if __name__ == '__main__':
    get_numbers_ticket(1, 48, 8)

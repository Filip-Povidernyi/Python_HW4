import random


def get_numbers_ticket(min: int, max: int, quantity: int):

    numbers = set()

    while len(numbers) < quantity:

        if (max - min) < quantity:

            print("Різниця між max і min числами повинна перевищувати quantity")
            return None

        num = random.randint(min, max)
        numbers.add(num)

    return numbers


if __name__ == '__main__':
    print(get_numbers_ticket(10, 16, 6))

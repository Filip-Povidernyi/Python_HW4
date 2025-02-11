def normalize_phone(phone_numbers: list):
    char_set = frozenset('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    normalize_number = ''
    normalize_numbers = []
    for number in (phone_numbers):
        for char in number:
            if char in char_set:
                normalize_number += char
        if len(normalize_number) == 12:
            normalize_numbers.append(f'+{normalize_number}')
        elif len(normalize_number) == 10:
            normalize_numbers.append(f'+38{normalize_number}')
        normalize_number = ''
    print(normalize_numbers)


if __name__ == '__main__':
    normalize_phone([
        "067\\t123 4567",
        "(095) 234-5678\\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ])

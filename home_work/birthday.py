from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list):

    upcoming_birthdays_list = []
    today = datetime.now().date()

    for user in users:

        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_date_this_year = datetime(
            year=today.year, month=birthday_date.month, day=birthday_date.day).date()

        if birthday_date_this_year < today:

            print(birthday_date_this_year)

        if today <= birthday_date_this_year <= (today + timedelta(days=6)):

            if birthday_date_this_year.weekday() < 5:

                message_dict = {}
                date_in_string = birthday_date_this_year.strftime("%Y.%m.%d")
                message_dict.update(
                    {'name': user.get('name'), 'congratulation_date': date_in_string})
                upcoming_birthdays_list.append(message_dict)

            else:

                message_dict = {}
                date_in_string = (birthday_date_this_year + timedelta(
                    days=(7 - birthday_date_this_year.weekday()))).strftime("%Y.%m.%d")
                message_dict.update(
                    {'name': user.get('name'), 'congratulation_date': date_in_string})
                upcoming_birthdays_list.append(message_dict)

    return upcoming_birthdays_list


users = [{'name': 'Kolya', 'birthday': "1991.02.10"},
         {'name': 'Ivan', 'birthday': "1987.02.11"},
         {'name': 'Peter', 'birthday': "1964.02.12"},
         {'name': 'Jack', 'birthday': "1999.02.13"},
         {'name': 'Olya', 'birthday': "1997.02.14"},
         {'name': 'Slava', 'birthday': "1986.02.15"},
         {'name': 'Serg', 'birthday': "1974.02.16"},
         {'name': 'Alex', 'birthday': "1996.02.17"},
         {'name': 'Pavel', 'birthday': "1998.02.18"}]


if __name__ == '__main__':
    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)

from datetime import datetime


def get_upcoming_birthdays(users):

    upcoming_birthdays_list = []
    today = datetime.now().date()

    for user in users:
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        date_diff = birthday_date - today

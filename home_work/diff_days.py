from datetime import datetime


def get_days_from_today(date: str):
    current_day = datetime.now().date()
    got_day = datetime.strptime(date, "%Y-%m-%d").date()
    days_diff = current_day.toordinal() - got_day.toordinal()
    return days_diff


if __name__ == '__main__':
    get_days_from_today('1951-03-27')

from collections import defaultdict
from datetime import datetime


def get_formatted_birthdays_list(users) -> str:
    week_days = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }

    formatted_list = []

    for i in range(6):
        if i in users:
            formatted_list.append(f'{week_days[i]}: { ", ".join(users[i])}')

    return '\n'.join(formatted_list)


def get_birthdays_per_week(users):
    users_to_congratulate = defaultdict(list)
    current_date = datetime.today().date()

    for user in users:
        default_week_day = 0
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=current_date.year)

        if birthday_this_year < current_date:
            birthday_this_year = birthday_this_year.replace(
                year=current_date.year + 1)

        delta_days = (birthday_this_year - current_date).days

        if delta_days < 7:
            day_of_week = birthday_this_year.weekday()

            if day_of_week in [5, 6]:
                users_to_congratulate[default_week_day].append(user["name"])
            else:
                users_to_congratulate[day_of_week].append(user["name"])

    print(get_formatted_birthdays_list(users_to_congratulate))

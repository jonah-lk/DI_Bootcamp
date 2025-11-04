# Daily challenge GOLD : Happy birthday
# Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
import re

birthday = input('What\'s your birthday? (DD/MM/YYYY)\t')
def draw_birthday_cake(string):
    pattern = r'^(\d{1,2})/(\d{1,2})/(\d{1,4})$'
    if not re.match(pattern, string):
        return 'Invalid date format!'
    day = re.findall(pattern, string)[0][0]
    month = re.findall(pattern, string)[0][1]
    year = re.findall(pattern, string)[0][2]
    if not day.isdigit() or not month.isdigit() or not year.isdigit() or 1 < int(day) > 31 or 1 < int(month) > 12:
        return 'Invalid date!'
    # Display a little cake as seen below:
    #        ___iiiii___
    #       |:H:a:p:p:y:|
    #     __|___________|__
    #    |^^^^^^^^^^^^^^^^^|
    #    |:B:i:r:t:h:d:a:y:|
    #    |                 |
    #    ~~~~~~~~~~~~~~~~~~~
    # The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.
    # Bonus : If they were born on a leap year, display two cakes !
    last_day_digit = int(str(day)[len(str(day)) - 1])
    candles = 'i' * last_day_digit
    first_row = f'{' ' * 3}{'_' * int((19 - len(candles)) / 2 - len(' ' * 3))}{candles}{'_' * int((19 - len(candles)) / 2 - len(' ' * 3))}{' ' * 3}'
    leap_year_multiple = 2 if int(year) % 4 == 0 and (int(year) % 400 == 0 or int(year) % 100 != 0) else 1
    return f"""
        {first_row}
        {' ' * 3}|:H:a:p:p:y:|{' ' * 3}
        {' ' * 3}|{' ' * (19 - len(f'{' ' * 3}||{' ' * 3}'))}|{' ' * 3}
        {'_' * 3}|{' ' * (19 - len(f'{'_' * 3}||{'_' * 3}'))}|{'_' * 3}
        |{'^' * (19 - len('||'))}|
        |:B:i:r:t:h:d:a:y:|
        |{' ' * (19 - len('||'))}|
        {'~' * 19}\n\n
    """ * leap_year_multiple
print(draw_birthday_cake(birthday))
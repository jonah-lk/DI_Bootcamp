# ex 1
import datetime, holidays

def today_is():
    today = datetime.date.today()
    morocco_holidays = holidays.Morocco(years = [today.year])
    print('Today:', today)
    next_holiday = next((d, name) for d, name in sorted(morocco_holidays.items()) if d >= today)
    next_holiday_date, next_holiday_name = next_holiday
    days_until = next_holiday_date - today
    print(f'Next holiday: {next_holiday_name} is in {days_until} days')

today_is()

# ex 2
today = datetime.datetime.now()
birthday = datetime.datetime.strptime('2000/10/09', '%Y/%m/%d')
age_in_seconds = (today - birthday).total_seconds()
def age_in_planets(age_in_seconds):
    print(f'Earth: {age_in_seconds / 60 / 60 / 24 / 365.25} years old')
    print(f'Mercury: {age_in_seconds / 60 / 60 / 24 / (365.25 * 0.2408467)} years old')
    print(f'Venus: {age_in_seconds / 60 / 60 / 24 / (365.25 * 0.61519726)} years old')
    print(f'Mars: {age_in_seconds / 60 / 60 / 24 / (365.25 * 1.8808158)} years old')
    print(f'Jupiter: {age_in_seconds / 60 / 60 / 24 / (365.25 * 11.862615)} years old')
    print(f'Saturn: {age_in_seconds / 60 / 60 / 24 / (365.25 * 29.447498)} years old')
    print(f'Uranus: {age_in_seconds / 60 / 60 / 24 / (365.25 * 84.016846)} years old')
    print(f'Neptune: {age_in_seconds / 60 / 60 / 24 / (365.25 * 164.79132)} years old')

age_in_planets(age_in_seconds)

# ex 3
import re

def return_numbers(string):
    return re.sub(r"\D", "", string)

print(return_numbers('k5k3q2g5z6x9bn'))

# ex 4
def check_full_name():
    full_name = input("Enter your full name (e.g., John Doe): ").strip()
    pattern = r"^[A-Z][a-z]+\s[A-Z][a-z]+$"
    if re.fullmatch(pattern, full_name):
        print("Valid full name!")
        return True
    else:
        print("Invalid full name!")
        return False

check_full_name()

# ex 5
import random, string

def generate_password():
    uppers = list(string.ascii_uppercase)
    lowers = list(string.ascii_lowercase)
    digits = list(string.digits)
    specials = list(string.punctuation)
    all = [*uppers, *lowers, *digits, *specials]
    random.shuffle(all)
    while True:
        try:
            length = int(input('password length: '))
            if length < 6 and length > 30:
                raise Exception('Length must be between 6 and 30!')
            upper = uppers[random.randint(0, len(uppers) - 1)]
            lower = lowers[random.randint(0, len(lowers) - 1)]
            digit = digits[random.randint(0, len(digits) - 1)]
            special = specials[random.randint(0, len(specials) - 1)]
            password = [upper, lower, digit, special]
            for i in range(0, length - len(password)):
                password.append(all[random.randint(0, len(all) - 1)])
            random.shuffle(password)
            password = ''.join(password)
            if not is_valid_password(password, length):
                raise Exception('Invalid password generation!')
            return (password, length)
        except Exception as e:
            print(e)
            continue

def is_valid_password(password, length, pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^\w\s]).+$'):
    if len(password) != length or not re.match(pattern, password):
        return False
    else:
        return True

print('Here\'s your password, keep it safe:', generate_password()[0])

for i in range(0, 100):
    password, length = generate_password()
    print('Here\'s your password, keep it safe:', password)
    print('Valid:', is_valid_password(password, length))
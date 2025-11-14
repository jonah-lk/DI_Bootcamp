# ex 2
import func

func.sum(1, 2)

# ex 3
import string, random

all_letters = list(string.ascii_lowercase)
random_5 = [all_letters[random.randint(0, len(all_letters) - 1)] for _ in range(0, 5)]
random_5_string = ''.join(random_5)

# ex 4
import datetime

current_date = datetime.datetime.now()
print(current_date)

# ex 5
jan_1 = datetime.datetime(current_date.year, 1, 1)
diff = current_date - jan_1
print(diff)

# ex 6
birthday = datetime.datetime.strptime('2000/10/09', '%Y/%m/%d')
bro_lived_for = current_date - birthday
print(bro_lived_for.total_seconds() / 60, 'minutes')

# ex 7
from faker import Faker

faker = Faker()

users = []

def add_users(how_many):
    for i in range(how_many):
        users.append({
            'name': faker.name(),
            'address': faker.address(),
            'language_code': faker.language_code()
        })

add_users(10)
for user in users:
    print(f'{user['name']} - {user['address']} - {user['language_code']}\n\n')
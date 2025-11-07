# Exercise 1
# Instructions
# Draw the following pattern using for loops:
#   *
#  ***
# *****
max_stars = 5
for i in range(1, max_stars + 1, 2):
    print(' ' * int((max_stars - i) / 2) + '*' * i + ' ' * int((max_stars - i) / 2))
# Draw the following pattern using for loops:
#     *
#    **
#   ***
#  ****
# *****
for i in range(1, max_stars + 1):
    print(' ' * (max_stars - i) + '*' * i)
# Draw the following pattern using for loops:
# *
# **
# ***
# ****
# *****
# *****
#  ****
#   ***
#    **
#     *
for i in range(1, max_stars * 2 + 1):
    if i <= max_stars:
        print('*' * i)
    else:
        print(' ' * (i - max_stars) + '*' * (max_stars * 2 + 1 - i))
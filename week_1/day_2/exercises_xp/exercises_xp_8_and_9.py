# Exercise 8: Pizza Toppings
# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print: "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.
pizza_cost = 10
toppings = []
while True:
    topping = input('Enter your pizza toppings. (Type quit if you\'re done)\t')
    if topping.lower() == 'quit':
        break
    pizza_cost += 2.5
    toppings.append(topping)
    print(f'Adding {topping} to your pizza.')
print(f'Your toppings {toppings}. Total: {pizza_cost}$\n')

# Exercise 9: Cinemax Tickets
# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
# Free for people under 3.
# $10 for people aged 3 to 12.
# $15 for anyone over 12.
# Print the total ticket cost.
ages = input('Welcome to the cinema. Give the ages of the ticket buyers. (Space seperated and integers)\t')
ages = ages.split(' ')
tickets_sum = 0
for age in ages:
    if not age.isdigit():
        print('You gave an invalid age!')
        ticket_sum = 0
        break
    age = int(age)
    if age < 3:
        continue
    elif age < 12:
        tickets_sum += 10
    else:
        tickets_sum += 15
print(f'Your total is {tickets_sum}$\n')

# Bonus:
# Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
# Write a program to:
# Ask for each person’s age.
# Remove anyone who isn’t allowed to watch.
# Print the final list of attendees.
print('This movie is age restricted. (Only for ages 16-21)')
ages = input('Welcome to the cinema. Give the ages of the ticket buyers. (Space seperated and integers)\t')
ages = ages.split(' ')
tickets_sum = 0
for age in ages:
    if not age.isdigit():
        print('You gave an invalid age!')
        ticket_sum = 0
        break
    age = int(age)
    if 16 <= age <= 21:
        tickets_sum += 15
    else:
        ages.remove(str(age))
print(f'Your total is {tickets_sum}')
print(f'Ages of watchers {ages}')

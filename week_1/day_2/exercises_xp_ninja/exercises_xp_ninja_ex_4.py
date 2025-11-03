# Exercise 4 : Frequency Of The Words
# Write a program that prints the frequency of the words from the input.
string = input('Give sentence\t')
unique = set(string.split(' '))
for word in unique:
    print(f'{word}:{string.split(' ').count(word)}')
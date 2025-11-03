# Exercise 3: Working on a paragraph
# Find an interesting paragraph of text online. (Please keep it appropriate to the social context of our class.)
# Paste it to your code, and store it in a variable.
# Let’s analyze the paragraph. Print out a nicely formatted message saying:
# How many characters it contains (this one is easy…).
# How many sentences it contains.
# How many words it contains.
# How many unique words it contains.
# Bonus: How many non-whitespace characters it contains.
# Bonus: The average amount of words per sentence in the paragraph.
# Bonus: the amount of non-unique words in the paragraph.
import re

fav_quote = """To be ignorant of what occurred before you were born is to remain always a child.
    For what is the worth of human life, unless it is woven into the life of our ancestors by the records of history?"""

print(f'My string has {len(fav_quote)} characters.')
print(f'My string has {len(re.split(r'[.?!]', fav_quote))} sentences.')
print(f'My string has {len(re.split(r'[^a-zA-Z]', fav_quote))} words.')
print(f'My string has {len(set(re.split(r'[^a-zA-Z]', fav_quote)))} unique words.')
print(f'My string has {len(fav_quote.replace(' ', ''))} none white space characters.')
sentences = re.split(r'[.?!]', fav_quote)
for sentence in sentences:
    print(f'The sentence {sentence} has {len(re.split(r'[^a-zA-Z]', sentence))} words.')
print(f'Average words per sentence: {int(len(re.split(r'[^a-zA-Z]', fav_quote)) / len(re.split(r'[.?!]', fav_quote)))}')
print(f'There are {len(re.split(r'[^a-zA-Z]', fav_quote)) - len(set(re.split(r'[^a-zA-Z]', fav_quote)))} none unique words in the paragraph.')
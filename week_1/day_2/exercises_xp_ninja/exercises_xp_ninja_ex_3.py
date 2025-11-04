import re

# Exercise 3: Working on a paragraph
# Find an interesting paragraph of text online. (Please keep it appropriate to the social context of our class.)
# Paste it to your code, and store it in a variable.
fav_quote = """To be ignorant of what occurred before you were born is to remain always a child.
    For what is the worth of human life, unless it is woven into the life of our ancestors by the records of history?"""
# Let’s analyze the paragraph. Print out a nicely formatted message saying:
# How many characters it contains (this one is easy…).
print(f'My string has {len(fav_quote)} characters.')
# How many sentences it contains.
sentences = re.split(r'[.?!]', fav_quote)
sentence_count = 0
for sentence in sentences:
    if len(sentence) < 1:
        sentences.remove(sentence)
        continue
    sentence_count += 1
print(f'My string has {sentence_count} sentences.')
# How many words it contains.
words = re.split(r'[^a-zA-Z]', fav_quote)
word_count = 0
for word in words:
    if not re.fullmatch(r'[a-zA-Z]+', word):
        print(repr(word))
        words.remove(word)
        continue
    word_count += 1
print(f'My string has {word_count} words.')
# How many unique words it contains.
unique_words = set(words)
print(f'My string has {len(unique_words)} unique words.')
# Bonus: How many non-whitespace characters it contains.
no_white_space = fav_quote.replace(' ', '')
print(f'My string has {len(no_white_space)} none white space characters.')
# Bonus: The average amount of words per sentence in the paragraph.
words_per_sentence = int(len(words) / len(sentences))
print(f'There are {words_per_sentence} words per sentence in the paragraph.')
# Bonus: the amount of non-unique words in the paragraph.
non_unique_word_count = len(words) - len(unique_words)
print(f'There are {non_unique_word_count} none unique words in the paragraph.')
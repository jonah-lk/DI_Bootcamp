import re
# Challenge 1: Sorting
# Write a Python program that takes a single string of words as input, where the words are separated by commas (e.g., ‘apple,banana,cherry’).
# The program should output these words sorted in alphabetical order, with the sorted words also separated by commas.
words = ''
while True:
    words = input('Give words. (comma separated)\t')
    if re.match(r'^[A-Za-z]+(,[A-Za-z]+)*$', words):
        words = re.split(r'\s*,\s*', words)
        break
    else:
        print('Follow the pattern')

words.sort()
sorted_words = ','.join(words)
print(sorted_words)

# Challenge 2: Longest Word
# Write a function that takes a sentence as input and returns the longest word in the sentence.
# If there are multiple longest words, return the first one encountered. Characters like apostrophes, commas, and periods should be considered part of the word.
def longest_word(sentence):
    longest = ''
    try:
        sentence = re.split(r'\s+', sentence)
        for word in sentence:
            if len(word) > len(longest):
                longest = word
    except:
        print('Something\'s wrong, and it\'s your fault!')
    return longest
sentence = 'Forgetfulness is by all means powerless!'
longest_in_sentence = longest_word(sentence)
print(longest_in_sentence)
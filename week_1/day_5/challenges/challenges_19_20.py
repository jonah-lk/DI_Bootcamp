# Exercise 19
# Write a function that mimics the builtin .split() method for strings.
# By default the function uses whitespace but it should be able to take an argument for any character and split with that argument.
def my_split(sentence, splitter = ' '):
    chunks = []
    try:
        word = ''
        for ch in sentence:
            if ch == splitter[0]:
                chunks.append(word)
                word = ''
            else:
                word += ch
        chunks.append(word)
    except:
        print('Something\'s off!')
    return chunks
sentence = 'None numeric value in list!'
split = my_split(sentence, 'n')

# Exercise 20
# Convert a string into password format.
def str_to_pass(password):
    hidden = ''
    try:
        hidden = '*' * len(password)
    except:
        print('Something\'s off!')
    return hidden
password = 'hjlknjhiugugiugu'
hidden_pass = str_to_pass(password)
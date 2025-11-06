import random, re

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)

hangman = list('*' * len(word))
guessed = []
the_damned = ['head', 'body', 'left arm', 'right arm', 'left leg', 'right leg']
the_damned.reverse()
attempts = len(the_damned)

while '*' in hangman and attempts > 0:
    attempts -= 1
    guess = input('Guess a letter!\t')[0]
    index = -1
    print(f"""
        pretend that you see a {' '.join(the_damned[attempts:])}
    """)

    if guess in guessed:
        print('Already guessed that letter! You wasted an attempt')
        print(f'You have {attempts} more attempts')
        continue

    guessed.append(guess)

    for i in range(word.count(guess)):
        index = word.index(guess.lower(), index + 1)
        hangman[index] = guess

    print(f'{''.join(hangman)}')
    print(f'You have {attempts} more attempts')

if '*' in hangman:
    print(f'You lost. Guessed: {''.join(hangman)}. The word: {word}')
else:
    print(f'You won. Attempts remaining: {attempts}.')
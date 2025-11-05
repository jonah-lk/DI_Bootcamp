# Instructions
# In cryptography, a Caesar cipher is one of the simplest and most widely known encryption techniques.
# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.
# For example, with a left shift of 3 –> D would be replaced by A,
# –> E would become B, and so on.
# The method is named after Julius Caesar, who used it in his private correspondence.
# Create a python program that encrypts and decrypts messages with ceasar cypher.
# The user enters the program, and then the program asks him if he wants to encrypt or decrypt, and then execute encryption/decryption on a given message and a given shift.
# Check out this tutorial
# Hint:
# for letter in text:
#     cypher_text += chr(ord(letter) + 3)
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
to_do = input('Want to cypher of decypher?\t')
while True:
    if to_do.lower() == 'cypher':
        cyphered = ''
        text = input('Text to encrypt:\t')
        shift = 0
        try:
            shift = int(input('Shift:\t'))
        except:
            shift = 3
        for i in range(len(text)):
            if text[i] not in alphabets:
                cyphered += text[i]
                continue
            position = alphabets.index(text[i])
            cyphered += alphabets[position - shift]
        print(cyphered)
        break
    elif to_do.lower() == 'decypher':
        decyphered = ''
        text = input('Text to decrypt:\t')
        shift = 0
        try:
            shift = int(input('Shift:\t'))
        except:
            shift = 3
        for i in range(len(text)):
            if text[i] not in alphabets:
                decyphered += text[i]
                continue
            position = alphabets.index(text[i])
            index = (position + shift) % 26
            decyphered += alphabets[index]
        print(decyphered)
        break
    else:
        print('Wrong functionality! Try again.')
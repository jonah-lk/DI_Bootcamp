string = ''
while len(string) < 1:
    string = input('Give sentence.\t')
char = ''
while len(char) < 1:
    char = input('Give character.\t')
count = list(string).count(char)
print(f'The char {char} is repeated {count} times in {string}')
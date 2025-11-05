# Input:
# You have entered a wrong domain
# Output:
# domain wrong a entered have You
string = input('Give a string\t')
string_list = string.split(' ')
string_list.reverse()
print(' '.join(string_list))
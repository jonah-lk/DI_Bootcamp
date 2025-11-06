import re
# Daily challenge Gold: Solve the Matrix
MATRIX_STR = '''
7ii
Tsx
h%?
i #
sM 
$a 
#t%'''

list_1d = MATRIX_STR.split('\n')
list_2d = []
max_cols = 0
matrix = ''
for row in list_1d:
    list_2d.append(list(row))
    if max_cols < len(row):
        max_cols = len(row)
for col in range(max_cols):
    for row in range(len(list_2d)):
        try:
            if re.match(r'[a-zA-Z]', list_2d[row][col]):
                matrix += list_2d[row][col]
            else:
                matrix += ' '
        except:
            continue
print(matrix)
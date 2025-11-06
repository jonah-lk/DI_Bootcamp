grid = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]
width = 40
section = int(((width - 2) / 3) / 2)
display_section = section - 1
def display_board():
    print(f"""
        {'*' * width}
        *{' ' * display_section}{grid[0][0]}{' ' * section}|{' ' * display_section}{grid[0][1]}{' ' * section}|{' ' * display_section}{grid[0][2]}{' ' * section}*
        *{'-' * section}{'-' * section}|{'-' * section}{'-' * section}|{'-' * section}{'-' * section}*
        *{' ' * display_section}{grid[1][0]}{' ' * section}|{' ' * display_section}{grid[1][1]}{' ' * section}|{' ' * display_section}{grid[1][2]}{' ' * section}*
        *{'-' * section}{'-' * section}|{'-' * section}{'-' * section}|{'-' * section}{'-' * section}*
        *{' ' * display_section}{grid[2][0]}{' ' * section}|{' ' * display_section}{grid[2][1]}{' ' * section}|{' ' * display_section}{grid[2][2]}{' ' * section}*
        {'*' * width}
    """)

def check_win():
    win = False
    size = len(grid)
    for i in range(size):
        horizontal = grid[i][0]
        vertical = grid[0][i]
        horiz_win = vert_win = True
        for j in range(size):
            if grid[i][j] != horizontal or grid[i][j] == ' ':
                horiz_win = False
            if grid[j][i] != vertical or grid[j][i] == ' ':
                vert_win = False
        if horiz_win or vert_win:
            win = True
            break
        
    if not win:
        diag1 = grid[0][0]
        diag2 = grid[0][size - 1]
        diag1_win = diag2_win = True
        for i in range(size):
            if grid[i][i] != diag1 or grid[i][i] == ' ':
                diag1_win = False
            if grid[i][size - i - 1] != diag2 or grid[i][size - i - 1] == ' ':
                diag2_win = False
        if diag1_win or diag2_win:
            win = True
    
    return win

def player_input(x_or_o):
    x = -1
    y = -1
    display_board()
    plays = 0
    while True:
        try:
            print(f'Player {x_or_o} turn')
            x = int(input('Give row index to play your move\t'))
            y = int(input('Give column index to play your move\t'))
            if grid[x][y] != ' ':
                raise Exception('Already filled!')
            else:
                grid[x][y] = x_or_o
                win = check_win()
                plays += 1
                if win:
                    print(f'Player {x_or_o} won.')
                    display_board()
                    break
                elif plays == 9:
                    print(f'It\'s a draw!')
                    display_board()
                    break
                else:
                    x_or_o = 'x' if x_or_o == 'o' else 'o'    
                display_board()
        except:
            print('Please select correct indeces! Try again.')
        
current_player = 'x'
def play():
    player_input(current_player)

play()
# Tic-Tac-Toe game
import numpy as np

GAME = True
n = 3
mat = []
a = 1
turn = [' x ', ' o ']
players = len(turn)
gamer = 0
position_name = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
position_choose = []
position = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}
turns = 0
gamer_win = np.array([[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]])


def tic_tav_toe(matrix):
    for i in range(n):
        for _ in range(n):
            break
        print(''.join(matrix[i]))


def check_winner(player):
    global GAME, gamer_win
    for win in range(players):
        vertical = np.sum(gamer_win[win, :, :], axis=0)
        horizontal = np.sum(gamer_win[win, :, :], axis=1)
        diagonal = np.sum(np.diagonal(gamer_win[win, :, :]))
        diagonal_rot = np.sum(np.diagonal(np.rot90(gamer_win[win, :, :])))
        check_v = np.array([vertical == 3]).any()
        check_h = np.array([horizontal == 3]).any()
        check_d = np.array([diagonal == 3]).any()
        check_d_r = np.array([diagonal_rot == 3]).any()
        if check_v or check_h or check_d or check_d_r:
            print(f'THE GAMER {player+1} IS THE WINNER')
            GAME = False
            break
    return GAME


def how_turn(player):
    global GAME, turns, gamer_win
    turns += 1
    if 4 <= turns <= 7:
        GAME = check_winner(player)
    elif turns > 7:
        print(f'THERE IS NOT WINNER!')
        GAME = False
    if player == 0:
        player = 1
    else:
        player = 0
    return player


def select():
    global position_name, gamer_win
    no = input('Enter position (1-9): ')

    while no not in position_name or no in position_choose:
        if no in position_choose:
            print('Error: Oops! This position is taken, choose new one')
        else:
            print('Error: enter a numeric digit')
        no = input('Enter position (1-9): ')
    position_choose.append(no)
    x = position[int(no)][0]
    y = position[int(no)][1]
    mat[x][y] = turn[gamer]
    gamer_win[gamer, y, x] = 1


# Game board
for i in range(0, n):
    t = []
    for j in range(0, n):
        t.append(f' {a} ')
        a += 1
    mat.append(t)

print('Tic Tac Toe game')
print('gamer 1: x ')
print('gamer 2: o ')
print('STAR GAME')
tic_tav_toe(mat)


while GAME:
    print(f'Gamer {gamer + 1} select position')
    select()
    tic_tav_toe(mat)
    gamer = how_turn(gamer)

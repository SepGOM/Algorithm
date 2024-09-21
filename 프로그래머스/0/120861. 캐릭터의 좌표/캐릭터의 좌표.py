def solution(keyinput, board):
    x, y = 0, 0
    x_lim, y_lim = board[0] // 2, board[1] // 2
    move = {'left':(-1, 0), 'right':(1, 0), 'up':(0, 1), 'down':(0, -1)}
    
    for k in keyinput:
        move_x, move_y = move[k]
        
        if abs(x + move_x) > x_lim or abs(y + move_y) > y_lim:
            continue
        else:
            x, y = x + move_x, y + move_y

    return [x,y]
board = [[2, 1, 2],
         [2, 1, 1],
         [1, 1, 0]]

def is_solved(board):
    check = [],[],[]
    cross = []
    revcross = []
    j = 0
    k = 0
    n = 2
    zero = 0
    for i in board:
        if (i == [1,1,1]):
            print('1')
        if (i == [2,2,2]):
            print('2')
        check[j].extend([board[0][j],board[1][j],board[2][j]])
        if 0 in check[j]: zero = 1
        cross.append(i[j])
        revcross.append(i[n])
        if check == [1,1,1]:
            print('1')
        if check == [2,2,2]:
            print('2')
        j += 1
        n -= 1
    print(check)
    if (cross == [1,1,1]):
        print('1')
    if (cross == [2,2,2]):
        print('2')
    if (revcross == [1,1,1]):
        print('1')
    if (revcross == [2,2,2]):
        print('2')
        
    while k < 3:
        print(check[k])
        if check[k] == [1,1,1]:
            return 1
        if check[k] == [2,2,2]:
            return 1
        k += 1
        
    if zero: return -1
    return 0
   
    
is_solved(board)
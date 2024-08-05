lst = [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]

def move_zeros(lst):
    x = 0
    y = 0
    while x < len(lst):
        if (lst[x] == 0):
            lst.pop(x)
            y = y + 1
            x = x - 1
        x = x + 1
        
    x = 0    
    while x < y:
        lst.append(0)
        x = x + 1
    print (lst)
    
move_zeros(lst)
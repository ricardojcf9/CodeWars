m = 4183059834009

def find_nb(m):
    res = 0
    num = 1
    while(m > res):
        res = res + (num ** 3)
        if (res == m):
            return num
        num = num + 1
        
    return -1
    pass

find_nb(m)
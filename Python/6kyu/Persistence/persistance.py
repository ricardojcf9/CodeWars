n = 999

def persistence(n):
    count = 0
    x = 0
    num = []
    num.insert(0,n)
    y = 1
    while(n > 9):
        y = 1
        x = 0
        num.insert(0,n)
        sepnum = list(map(int,str(num[0])))
        while x < (len(sepnum)):
            y = sepnum[x] * y
            x = x + 1
        count = count + 1
        n = y
        print(y)
    
    return count
        
    pass
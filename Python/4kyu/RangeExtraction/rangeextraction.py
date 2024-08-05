def solution(args):
    x = 0
    y = 0
    numor = []
    while x < len(args)-1:
        if args[x] == (args[x+1])-1:
            y = y + 1
        else:
            if y == 1:
                numor.append(0)
                numor.append(0)
                y = 0
            else:
                numor.append(y)
                y = 0
        x = x + 1
    numor.append(y)
    
    k = 0
    ans = ""
    x = 0
    while x < len(numor):
        if x > 0:
            ans = ans + ","
        v = args[k]
        ans = ans + str(v)
        k += numor[x]
        if args[k] != v:
            ans = ans +  '-' + str(args[k])
        k = k + 1
        x = x + 1
    return(ans)
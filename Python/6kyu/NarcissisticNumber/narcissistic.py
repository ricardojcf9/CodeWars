value = 371

def narcissistic( value ):
    k = 0
    i = 0
    n = 1
    num = str(value)
    while (value/n) > 1:
        n = n * 10
        i += 1
    n = 0
    while n < len(num):
        k += int(num[n]) ** i
        n += 1
        
    if(k == value):
        return(True)
    else:
        return(False)
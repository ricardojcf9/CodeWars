g = 2
m = 682853
n = 690000

def gap(g, m, n):
    i = m
    prime = []
    ret = []
    j = 1
    flag = 0
    while i <= n:
        k = 2
        while k < 100:
            if ((i % k) == 0):
                flag = 1
            k = k + 1
        if flag == 0:
            prime.append(i)
            if len(prime) >= 2:
                if(prime[j]-prime[j-1] == g):
                    ret.append(prime[j-1])
                    ret.append(prime[j])
                    print(ret)
                    return ret
                j += 1
        flag = 0
        i += 1
    return
        
        
gap(g,m,n)
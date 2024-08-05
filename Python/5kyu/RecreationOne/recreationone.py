m = 250
n = 500

# Working but not optimized enough for CodeWars (12000ms of timeout)

def list_squared(m, n):
    ret = []
    p = m
    while m < n:
        div = []
        i = 1
        while i <= 10000 and i <= m:
            if m % i == 0:
                div.append(i**2)
            i += 1
        k = sum(div)
        i = p
        l = []
        while i <= n*2:
            if i**2 == k:
                l.append(m)
                l.append(k)
                ret.append(l)
            i += 1
        m += 1
    print(ret)
    return ret
list_squared(m,n)
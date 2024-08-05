signature = [1,1,1]
n = 1

def tribonacci(signature, n):
    x = 0

    while x < n-3:
        sig = signature[x] + signature[x+1] + signature[x+2]
        signature.insert(x+3,sig)
        x = x + 1
       
    y = len(signature)
    print(y)

    while(y > n):
        signature.pop(-1)
        y = y - 1
        
    return (signature)
    pass
    
tribonacci(signature, n)
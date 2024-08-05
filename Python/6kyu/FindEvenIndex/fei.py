arr = [20,10,30,10,10,15,35]

def find_even_index(arr):
    n = -1
    x = 0
    y = 0
    left = 0
    right = 0
    while y < (len(arr)):
        x = 0
        left = 0
        right += arr[len(arr)-y-1]
        while x < (len(arr)):
            left += arr[x]
            if (((x+y)==(len(arr)-1)) and (left == right)):
                n = x
            x = x + 1
        y = y + 1
            
    print(n)
    pass
        

find_even_index(arr)
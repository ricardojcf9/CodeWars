num = 36

def is_prime(num):
    x = 0
    if num > 1:
        i = 2
        while i <= num ** 0.5:
          if ((num % i) == 0):
            return 0
          i = i + 1
    else:
        return 0

    return 1
        
    pass


is_prime(num)
s1 = 'mttercxruejfipaqkmt'
s2 = 'xtatamucqrm'

# Working but not optimized enough for CodeWars (12000ms timeout)

def scramble(s1, s2):
    j = 0
    for x in s2:
        i = 0
        for i in s1:
            if i == x:
                s1 = s1.replace(x, '', 1)
                j += 1
                break
            i += 1
        if j >= len(s2):
            return True
        else:
            return False
    
        
scramble(s1,s2)
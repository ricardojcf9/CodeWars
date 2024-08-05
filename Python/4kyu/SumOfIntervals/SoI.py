
intervals = [1,4],[3,5],[7,10]

def sum_of_intervals(intervals):
    k = 0
    ft = 1
    n = 0
    used = []
    for i in intervals:
        used.append(i[0])
        used.append(i[1])
    if (ft):
        k = used[1] - used[0]
    while n < len(used):
        at = [used[n],used[n+1]]
        print(at)
        j = 0
        while j < len(used)-2:
            if at[0] >= used[j] and at[1] >= used[j+1]: # [1,3] [2,4]
                k += (at[1] - used[j+1])
                
            elif at[0] <= used[j] and at[1] <= used[j+1]: # [2,4] [1,3]
                k += (used[j] - at[0])
                
            elif at[0] >= used[j] and at[1] <= used[j+1]: # [1,5] [3,4]
                k += 0
                
            else:
                k += (at[1] - at[0])
                
            print("loop")
            j += 2
        n += 2
        ft = 0
        
        print(k)
    return k

sum_of_intervals(intervals)
customers=[2,2,3,3,4,4]
n = 2

def queue_time(customers, n):
    queue = []
    i = 0
    next = 0
    if len(customers) == 0:
        y = 0
    elif len(customers) <= n:
        y = customers[0]
        while i < len(customers):
            if y <= customers[i]:
                y = customers[i]
            i += 1
    else:
        i = 0
        while len(customers) > 0:
            while i < n:
                queue.append(customers[0])
                customers.pop(0)
                i += 1
            i = 0
            y = queue[0]
            print(queue)
            while i < n:
                if y >= queue[i]:
                    y = queue[i]
                    next = i
                    print('lowest')
                i += 1
    
            queue[next] = queue[next] + customers[0]
            customers.pop(0)
        
        print(queue)
        
        i = 0
        y = 0
        while i < len(queue):
            if y < queue[i]:
                y = queue[i]
            i += 1
    
queue_time(customers, n)

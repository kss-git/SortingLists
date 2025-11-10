l=[4, 1, 7, 0, 2, 8, 5, 9, 3, 6,9,0,10,21,21,43,21234,12,33212,3,1,4,-1,-2.1,0]

def quicksort(l):
    if len(l) <= 1:
        return l
    
    p = l[-1]  
    w = []
    e = []
    
    for x in range(0,len(l) - 1):  
        if l[x] < p:
            w.append(l[x])
        else:
            e.append(l[x])
    
    return quicksort(w) + [p] + quicksort(e)

print(quicksort(l))

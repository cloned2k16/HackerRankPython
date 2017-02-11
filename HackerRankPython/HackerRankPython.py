import sys


def                                     _fmt                        (fmt, *args)                    :
    return fmt.format(*args);
    
def                                     getPairs                    (a)                             :
    sum = 0
    sz  = len(a)
    i =1
    while (i < sz):
        c   = 1
        while (i < sz and a[i] == a[i-1]):
            c+=1
            i+=1
        sum += (c * (c - 1))
        i+=1
    return sum
    
try:
    nT=int(raw_input())
    for tn in range(nT):
        N=int(raw_input())
        A=[int(x) for x in raw_input().split(' ')]
        A=sorted(A)
        r=getPairs(A)
        print r

except ValueError as e:
    print _fmt("Error: {}",e.message)


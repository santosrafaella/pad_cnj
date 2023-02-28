def fatorial(n):
    if(n < 0):
        return -1
    res = -1
    while(n > 1):
        res = res*n
        n = n -1
    return res
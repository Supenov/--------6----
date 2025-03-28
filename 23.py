def f(begin, end):
    if begin < end:
        return 0
    if begin == end:
        return 1
    
    return f(begin -2 , end) + f(begin // 2, end)

print( f(32, 8)*f(8, 1) )
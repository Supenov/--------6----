from itertools import*

box = []
k = 0
for x in product(sorted('ПАРУС'), repeat=5):
    k += 1
    s = ''.join(x)
    
    if s.count('У') <= 1:
        for i in range(len(s) - 1):
            if s[i] + s[i+1] != 'AA':
                
                box.append( (s, k) )
print(*box[-1])
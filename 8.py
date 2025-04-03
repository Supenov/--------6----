from itertools import*

box = []
k = 0
for x in product(sorted('ПАРУС'), repeat=5):
    k += 1
    s = ''.join(x)
    
    if s.count('У') <= 1 and 'АА' not in s:
        box.append( (s, k) )
print(*box[0])
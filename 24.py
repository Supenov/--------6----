s = open('24_15339.txt').readline()

s = s.replace('B', 'A').replace('C', 'A')

for x in '789':
    s = s.replace(x, '6')

while 'AA' in s or '66' in s:
    if 'AA' in s:
        s = s.replace('AA', 'A A')
    if '66' in s:
        s = s.replace('66', '6 6')

print( max(len(c) for c in s.split() ) )
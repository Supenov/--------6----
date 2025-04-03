s = open('24_15339.txt').readline()

s = s.replace('B', 'A').replace('C', 'A') # Заменяем все буквы на букву "А"

for x in '789':
    s = s.replace(x, '6')  # Заменяем все цифры на цифру "6"

while 'AA' in s or '66' in s: # ока нашлись нарушения в строке
    if 'AA' in s:
        s = s.replace('AA', 'A A') # Никакая буква не стоит рядом с буквой
    if '66' in s:
        s = s.replace('66', '6 6') # Никакая цифра не стоит рядом с цифрой

print( max(len(c) for c in s.split() ) )
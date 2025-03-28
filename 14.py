def f(number):
    number = 6**2030 + 6**100 - x
    d = []
    while number > 0:
        d.append(number % 6)
        number = number // 6

    return d[::-1].count(0)

#number = 6**2030 + 6**100 - x

box = []
for x in range(2031):
    box.append(f(x))


print(max(box))
box = []
for n in range(1, 501):
    b = bin(n)[2:]

    b += str(b.count('1') % 2)
    b += str(b.count('1') % 2)

    R = int(b, 2)

    if R > 123:
        box.append(R)

print(min(box))
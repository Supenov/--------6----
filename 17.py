lst = [int(x) for x in open('17_15333.txt')]

mx_19 = max(x for x in lst if x % 19 == 0) #; print(mx_19, mx_19 % 19)
box = []

for i in range(len(lst) - 1):
    a, b = lst[i:i+2]
    if (a > mx_19) or (b > mx_19):
        box.append(a+b)

print(len(box), max(box))
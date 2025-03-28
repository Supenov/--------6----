def f(x, a):
    return (x % 33 == 0) <= ( (x % a != 0) <= (x % 242 != 0) )

box = []
for A in range(1000, 0, -1):
    if all(f(x, A) == 1 for x in range(100000)):
        #print(A)
        box.append(A)

print(max(box))
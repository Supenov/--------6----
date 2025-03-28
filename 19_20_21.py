def game(s1, s2, m):
    if s1 + s2 >= 227:
        return m % 2 == 0
    if m == 0:
        return 0
    actions = [
        game(s1+1, s2, m - 1), game(s1, s2+1, m - 1),
        game(s1*2, s2, m - 1), game(s1, s2*2, m - 1)
    ]

    return any(actions) if (m -1) % 2 == 0 else all(actions)

print(19, [s2 for s2 in range(1, 210) if game(17, s2, 2)])
print(20, [s2 for s2 in range(1, 210) if game(17, s2, 3) and not game(17, s2, 1)])
print(20, [s2 for s2 in range(1, 210) if game(17, s2, 4) and not game(17, s2, 2)])
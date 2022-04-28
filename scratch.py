x = [1, 2, 3]
y = [4, 5, 6]
z = zip(x, y)

y, x = zip(*z)
x = list(x)
y = list(y)

print(x, y)


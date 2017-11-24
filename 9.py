
b = 1
c = (5e5 + b**2 - 1000*b)/(1000-b)

for b in range(1, 1000):
    c = (5e5 + b ** 2 - 1000 * b) / (1000 - b)
    if not c % 1:
        print(b, c, 1000 - b - c)
        print(b * c * (1000 - b - c))
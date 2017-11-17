a = 1
b = 2
lim = 4 * 10**6
sum = 0

while b < lim:
    if not b % 2:
        sum += b

    a, b = b, a+b

print(sum)
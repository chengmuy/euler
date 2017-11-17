def check_prime(n):
    for factor in range(2, int(n**.5) + 1):
        if not n % factor:
            return False
    return True

# generate composites up to n
def generate_composites(n):
    top = int(n ** 0.5)
    comps = set()
    for factor in range(2, top + 1):
        for mult in range(1, int(n / factor)):
            comps.add(factor * mult)
    return comps

num = 600851475143
comps = generate_composites(num // 2)
sorted_comps = sorted(list(comps))

index = len(sorted_comps) - 1
for div in range(num // 2, 1, -1):
    if div == sorted_comps[index]:
        # don't test this, because it's a prime
        index -= 1
    else:


# for div in range(num // 2 + 1, 1, -1):
#     if not div % 10**6:
#         print(div)
#     if not (num % div):
#         if check_prime(div):
#             print("prime factor: " + div)
#             break
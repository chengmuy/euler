def check_prime(n):
    for factor in range(2, int(n**.5) + 1):
        if not n % factor:
            return False
    return True

# generate primes up to n using sieve
def generate_primes(n):

num = 600851475143
for div in range(num // 2 + 1, 1, -1):
    if not div % 10**7:
        print(div)
    if not num % div:
        print(div)


# for div in range(num // 2 + 1, 1, -1):
#     if not div % 10**6:
#         print(div)
#     if not (num % div):
#         if check_prime(div):
#             print("prime factor: " + div)
#             break
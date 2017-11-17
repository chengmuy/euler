import timeit

# Sol 1 - even fib generator
def even_fib(limit):
    a = 1
    b = 2
    while (a < limit):
        if not a % 2:
            yield a
        a, b = b, a+b
print("Sol 1 - even fib generator")
print(sum(even_fib(4 * 10**6)))
print(timeit.timeit("sum(even_fib(4 * 10**6))", 'from __main__ import even_fib', number=1000))
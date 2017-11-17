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
print(timeit.timeit("sum(even_fib(4 * 10**20))", 'from __main__ import even_fib', number=1000))

# Sol 2 - even fib generator, no even check
def even_fib(limit):
    a = 0
    b = 1
    c = 2
    while (c < limit):
        yield c
        a = b + c
        b = c + a
        c = a + b
print("Sol 2")
print(sum(even_fib(4 * 10**6)))
print(timeit.timeit("sum(even_fib(4 * 10**20))", 'from __main__ import even_fib', number=1000))
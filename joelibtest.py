import joelib as jl
import timeit
import itertools
#
# print(timeit.timeit('sum((itertools.islice(jl.generatePrimesErat(), 1000)))', setup = 'import joelib as jl', number=10))
# print(sum((itertools.islice(jl.generatePrimesErat(), 1000))))
# print(timeit.timeit('sum((itertools.islice(jl.generatePrimesDivTest(), 100000)))', setup = 'import joelib as jl', number=1))
# print(sum((itertools.islice(jl.generatePrimesDivTest(), 1000))))
# print(timeit.timeit('sum((itertools.islice(jl.generatePrimesErat2(), 100000)))', setup = 'import joelib as jl', number=1))
# print(sum((itertools.islice(jl.generatePrimesDivTest(), 1000))))
print(timeit.timeit('sum((itertools.islice(jl.generatePrimesErat3(), 10000000)))', setup = 'import joelib as jl', number=1))
print(sum((itertools.islice(jl.generatePrimesErat3(), 1000))))

# for p in itertools.islice(jl.generatePrimesErat(), 1000):
#     print(p)


# sum([0,1,2,3])
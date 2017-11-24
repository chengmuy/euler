import joelib as jl
import numpy as np

# least common multiple
n = 20

lcm = 1
for p in jl.generatePrimesErat3():
    if p > n:
        break
    mult = 1
    while (mult * p) <= n:
        mult *= p
    print(mult)
    lcm *= mult

print(lcm)
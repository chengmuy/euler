import math

sum = sum([i*3 for i in range(0, math.ceil(1000/3))]) + \
      sum([i*5 for i in range(0, math.ceil(1000/5))]) - \
      sum([i*15 for i in range(0, math.ceil(1000/15))])

print(sum)

print(3 * (333 + 1) * 333 / 2
      + 5 * (199 + 1) * 199 / 2
      - 15 * (66 + 1) * 66 / 2)
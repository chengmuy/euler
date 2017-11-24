import numpy as np

seq = np.arange(100) + 1
seq.shape = (100, 1)

ans = sum(sum(seq.dot(seq.T))) - seq.T.dot(seq)
print(ans)

ans = 0
seqSum = sum(seq)
for i in range(1, 101):
    ans += seqSum * i - i**2
print(ans)
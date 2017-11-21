
maxPalindrome = 0
for i in range(100, 1000):
    for j in range(i, 1000):
        num = i * j
        if num > maxPalindrome and str(num) == str(num)[::-1]:
            maxPalindrome = num
            print(i, j, num)

print('max: ', maxPalindrome)

def factor_count(num, k):
    n = 0
    num /= k
    while num % 1.0 == 0:
        num /= k
        n += 1
    return n

def zeros(num):
    n2, n5 = 0, 0
    for i in range(1, num + 1, 1):
        n2 += factor_count(i, 2)
        n5 += factor_count(i, 5)
    return min(n2, n5)

print(zeros(21))

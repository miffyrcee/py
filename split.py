def split(m, n, cu):
    if m == n:
        print(cu)
    if m > n:
        for i in range(n):
            split(m - n, i, cu + 1)

split(3, 2, 1)

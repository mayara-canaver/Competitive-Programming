while True:
    valores = list(map(int, input().split()))
    m, n = valores
    soma = 0
    if m >= 1 and n >= 1:
        if m > n:
            for x in range(n, m+1, 1):
                soma = soma + x
            for y in range(n, m + 1, 1):
                print("%d" % y, end=" ")
        else:
            for x in range(m, n+1, 1):
                soma = soma + x
            for y in range(m, n + 1, 1):
                print("%d" % y, end=" ")

        print("Sum=%d" % soma)
    else:
        break

def hcfnaive(a, b):
    if (b == 0):
        return a
    else:
        return hcfnaive(b, a % b)


n = int(input())

for i in range(1, n + 1):
    a = int(input(), 2)
    b = int(input(), 2)

    if hcfnaive(a, b) != 1:
        a = 'All you need is love!'
    else:
        a = 'Love is not all you need!'

    print('Pair #%d: %s' % (i, a))

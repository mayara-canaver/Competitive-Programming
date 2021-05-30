vezes = int(input())

num_in, num_out, x = 0, 0, 0

while x < vezes:

    numero = int(input())

    if 10 <= numero <= 20:
        num_in = num_in + 1
    else:
        num_out = num_out + 1

    x = x + 1

print("%d in" % num_in)
print("%d out" % num_out)

vezes = int(input())

def is_prime(n):
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

for x in range(vezes):
    numero = int(input())
    if is_prime(numero):
        print("Prime")
    else:
        print("Not Prime")
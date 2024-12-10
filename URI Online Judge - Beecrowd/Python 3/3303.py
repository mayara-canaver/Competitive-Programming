vezes = int(input())

for x in range(vezes):
    joao, maria = 0, 0

    p1, d1 = list(map(int, input().split()))
    p2, d2 = list(map(int, input().split()))
    p3, d3 = list(map(int, input().split()))
    joao += p1 * d1 + p2 * d2 + p3 * d3

    p1, d1 = list(map(int, input().split()))
    p2, d2 = list(map(int, input().split()))
    p3, d3 = list(map(int, input().split()))
    maria += p1 * d1 + p2 * d2 + p3 * d3

    if maria > joao:
        print("MARIA")
    else:
        print("JOAO")
